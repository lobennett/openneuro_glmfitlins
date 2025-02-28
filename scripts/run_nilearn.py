import warnings
warnings.filterwarnings("ignore")
import sys
import os
import argparse
import pandas as pd
from glob import glob
from nilearn.glm.first_level import FirstLevelModel
import matplotlib.pyplot as plt
from nilearn.plotting import plot_design_matrix


def group_onesample(fixedeffect_paths: list, session: str, task_type: str,
                    contrast_type: str, group_outdir: str,
                    mask: str = None):
    """
    This function takes in a list of fixed effect files for a select contrast and
    calculates a group (secondlevel) model by fitting an intercept to length of maps.
    For example, for 10 subject maps of contrast A, the design matrix would include an intercept length 10.

    :param fixedeffect_paths: a list of paths to the fixed effect models to be used
    :param session: string session label, BIDS label e.g., ses-1
    :param task_type: string task label, BIDS label e.g., mid
    :param contrast_type: contrast type saved from fixed effect models
    :param group_outdir: path to folder to save the group level models
    :param mask: path to mask, default none
    :return: nothing return, files are saved
    """

    if not os.path.exists(group_outdir):
        os.makedirs(group_outdir)
        print("Directory created:", group_outdir)

    n_maps = len(fixedeffect_paths)
    # Create design matrix with intercept (1s) that's length of subjects/length of fixed_files
    design_matrix = pd.DataFrame([1] * n_maps, columns=['int'])
    if rt_array:
        design_matrix['rt'] = rt_array
        con_array = ['int','rt']
    else:
        con_array = ['int']

    # Fit secondlevel model
    sec_lvl_model = SecondLevelModel(mask_img=mask, smoothing_fwhm=None, minimize_memory=False)
    sec_lvl_model = sec_lvl_model.fit(second_level_input=fixedeffect_paths,
                                      design_matrix=design_matrix)
    # contrasts mean 'int' and corr with mRT 'rt
    for con in con_array:
        tstat_map = sec_lvl_model.compute_contrast(
            second_level_contrast=con,
            second_level_stat_type='t',
            output_type='stat'
        )
        tstat_out = f'{group_outdir}/subs-{n_maps}_ses-{session}_task-{task_type}_' \
                    f'contrast-{contrast_type}_stat-tstat_{con}.nii.gz'
        tstat_map.to_filename(tstat_out)

        
def fixed_effect(subject: str, session: str, task_type: str,
                 contrast_list: list, firstlvl_indir: str, fixedeffect_outdir: str,
                 modelsave_beta=False, save_var=False, save_tstat=True):
    """
    This function takes in a subject, task label, set of computed contrasts using nilearn,
    the path to contrast estimates (beta maps), the output path for fixed effec tmodels and
    specification of types of files to save, the beta estimates, associated variance and t-stat (which is calculated
    based on beta/variance values)
    Several path indices are hard coded, so should update as see fit
    e.g., '{sub}_ses-{ses}_task-{task}_effect-fixed_contrast-{c}_stat-effect.nii.gz'
    :param subject: string-Input subject label, BIDS leading label, e.g., sub-01
    :param session: string-Input session label, BIDS label e.g., ses-1
    :param task_type: string-Input task label, BIDS label e.g., mid
    :param contrast_list: list of contrast types that are saved from first level
    :param firstlvl_indir: string-location of first level output files
    :param fixedeffect_outdir: string-location to save fixed effects
    :param save_beta: Whether to save 'effects' or beta values, default = False
    :param save_var: Whether to save 'variance' or beta values, default = False
    :param save_tstat: Whether to save 'tstat', default = True
    :return: nothing return, files are saved
    """
    for contrast in contrast_list:
        try:
            print(f"\t\t\t Creating weighted fix-eff model for contrast: {contrast}")
            betas = sorted(glob(f'{firstlvl_indir}/{subject}_ses-{session}_task-{task_type}_run-*_'
                                f'contrast-{contrast}_stat-beta.nii.gz'))
            var = sorted(glob(f'{firstlvl_indir}/{subject}_ses-{session}_task-{task_type}_run-*_'
                              f'contrast-{contrast}_stat-var.nii.gz'))

            # conpute_fixed_effects options
            # (1) contrast map of the effect across runs;
            # (2) var map of between runs effect;
            # (3) t-statistic based on effect of variance;
            fix_effect, fix_var, fix_tstat = compute_fixed_effects(contrast_imgs=betas,
                                                                   variance_imgs=var,
                                                                   precision_weighted=True)
            if not os.path.exists(fixedeffect_outdir):
                os.makedirs(fixedeffect_outdir)
                print("Directory created:", fixedeffect_outdir)
            if save_beta:
                fix_effect_out = f'{fixedeffect_outdir}/{subject}_ses-{session}_task-{task_type}_' \
                                 f'contrast-{contrast}_stat-effect.nii.gz'
                fix_effect.to_filename(fix_effect_out)
            if save_var:
                fix_var_out = f'{fixedeffect_outdir}/{subject}_ses-{session}_task-{task_type}_' \
                              f'contrast-{contrast}_stat-var.nii.gz'
                fix_var.to_filename(fix_var_out)
            if save_tstat:
                fix_tstat_out = f'{fixedeffect_outdir}/{subject}_ses-{session}_task-{task_type}_' \
                                f'contrast-{contrast}_stat-tstat.nii.gz'
                fix_tstat.to_filename(fix_tstat_out)
        except Exception as e:
            print(f'Error processing Fixed Effect: {e} for {subject} and {contrast}')


plt.switch_backend('Agg') # turn off back end display to create plots
parser.add_argument("--sub", help="subject name, sub-XX, include entirety with 'sub-' prefix")
parser.add_argument("--task", help="task type -- e.g., mid, reward, etc")
parser.add_argument("--ses", help="session, include the session type without prefix, e.g., 1, 01, baselinearm1")
parser.add_argument("--numvols", help="The number of volumes for BOLD file, e.g numeric")
parser.add_argument("--boldtr", help="the tr value for the datasets in seconds, e.g. .800, 2.0, 3.0")
parser.add_argument("--beh_path", help="Path to the behavioral (.tsv) directory/files for the task")
parser.add_argument("--fmriprep_path", help="Path to the output directory for the fmriprep output")
parser.add_argument("--mask", help="path the to a binarized brain mask (e.g., MNI152 or "
                                   "constrained mask in MNI space, spec-network",
                    default=None)
parser.add_argument("--mask_label", help="label for mask, e.g. mni152, yeo-network, etc",
                    default=None)
parser.add_argument("--output", help="output folder where to write out and save information")
args = parser.parse_args()

# Now you can access the arguments as attributes of the 'args' object.
sample = args.sample
subj = args.sub
task = args.task
ses = args.ses
numvols = int(args.numvols)
boldtr = float(args.boldtr)
beh_path = args.beh_path
fmriprep_path = args.fmriprep_path
brainmask = args.mask
mask_label = args.mask_label
scratch_out = args.output


con_labs = {
    'ICSPvICSN': 'img_cspns - img_csm',
    'VCSPvVCSN': 'view_csp-noshk - view_csm',
}

contrasts = {
    'ICSPvICSN', 'VCSPvVCSN'
}

trial_type_map = {
    1: "view_csp-shk",
    2: "view_csp-noshk",
    3: "img_csp",
    4: "view_csm",
    5: "img_csm"
}

# Apply mapping
fwhm = 5
runs = ['1','2','3','4','5','6']


# first level
firstlvl_out = f'{scratch_out}/{subj}/{ses}'

if not os.path.exists(firstlvl_out):  
    os.makedirs(firstlvl_out)


for run in runs:
    print(f'\tStarting {subj} {run}.')
    # import behavior events .tsv from data path, fix issue with RT column & duration onsettoonset issues
    eventsdat = pd.read_csv(f'{beh_path}/{subj}/ses-{ses}/func/{subj}_ses-{ses}_task-{task}_run-{run}_events.tsv',
                            sep='\t')
    eventsdat["trial_type"] = eventsdat["trial_type"].map(trial_type_map)


    # get path to confounds from fmriprep, func data + mask, set image path
    conf_path = f'{fmriprep_path}/{subj}/ses-{ses}/func/{subj}_ses-{ses}_task-{task}_run-{run}' \
                f'_desc-confounds_timeseries.tsv'
    conf_df = pd.read_csv(conf_path, sep='\t')
    
    nii_path = glob(
        f'{fmriprep_path}/{subj}/ses-{ses}/func/{subj}_ses-{ses}_task-{task}_run-{run}'
        f'_space-MNI152NLin2009cAsym_res-2_desc-preproc_bold.nii.gz')[0]
    print('\t\t 1/3 Create Regressors & Design Matrix for GLM')
    
    # design matrix
    design_events = pd.DataFrame({'trial_type': eventsdat['trial_type'],
                                    'onset': eventsdat['onset'],
                                    'duration': eventsdat['duration']})

    frame_times = np.arange(numvols) * boldtr
    design_matrix_mid = make_first_level_design_matrix(
            frame_times= boldtr / 2,
            events=design_events,
            hrf_model='spm + derivative',
            drift_model=None,
            add_regs=conf_df.filter(regex="^(cosine|trans|rot)")
            )

    plot_design_matrix(design_matrix)
    plt.savefig(f'{scratch_out}/{subj}_ses-{ses}_task-{task}_run-{run}_design-mat.png')

    print('\t\t 2/3 Mask Image, Fit GLM model ar1 autocorrelation')
    # using ar1 autocorrelation (FSL prewhitening), drift model
    fmri_glm = FirstLevelModel(subject_label=subj, mask_img=brainmask,
                                t_r=boldtr, smoothing_fwhm=fwhm,
                                standardize=False, noise_model='ar1', drift_model=None, high_pass=None
                                )
    # Run GLM model using set paths and calculate design matrix
    run_fmri_glm = fmri_glm.fit(nii_path, design_matrices=design_matrix)


    for con_name, con in con_labs.items():
        try:
            beta_name = f'{firstlvl_out}/{subj}_ses-{ses}_task-{task}_run-{run}_contrast-{con_name}_stat-beta.nii.gz'
            beta_est = run_fmri_glm.compute_contrast(con, output_type='effect_size')
            beta_est.to_filename(beta_name)
            # Calc: variance
            var_name = f'{firstlvl_out}/{subj}_ses-{ses}_task-{task}_run-{run}_contrast-{con_name}_stat-var.nii.gz'
            var_est = run_fmri_glm.compute_contrast(con, output_type='effect_variance')
            var_est.to_filename(var_name)
        except Exception as e:
            print(f'Error processing beta: {e} for {subj} and {con_name}')


print("Running Fixed effect model -- precision weight of runs for each contrast")

fixed_effect(subject=subj, session=ses, task_type=task,
            contrast_list=contrasts, firstlvl_indir=firstlvl_out, fixedeffect_outdir=firstlvl_out,
            save_beta=True, save_var=True, save_tstat=False)


print("Running group model")
list_maps = sorted(glob(f'{scratch_out}/**/**/*_ses-{ses}_task-{task}_*'
                        f'contrast-{contrast}_stat-effect.nii.gz'))
print("number of group maps:", len(list_maps))

grp_out=f'{scratch_out}/group_out'
for contrast in contrasts:
    group_onesample(fixedeffect_paths=list_maps, session=ses, task_type=task,
                    contrast_type=contrast, group_outdir=grp_out,
                    mask=brainmask, rt_array=None)

