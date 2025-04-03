import json
import os
import shutil
import argparse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from bids.layout import BIDSLayout
from create_readme import generate_groupmodsummary
from utils import get_numvolumes, extract_model_info, gen_vifdf, calc_niftis_meanstd
from nilearn.plotting import plot_stat_map
from nilearn.image import load_img, concat_imgs, mean_img

# Turn off back end display to create plots
plt.switch_backend('Agg')

# Set up argument parsing
parser = argparse.ArgumentParser(description="Provide OpenNeuro study variables")
parser.add_argument("--openneuro_study", type=str, help="OpenNeuro study ID", required=True)
parser.add_argument("--taskname", type=str, help="Task name using in analyses", required=True)
parser.add_argument("--spec_dir", type=str, help="Directory where model specs are", required=True)
parser.add_argument("--analysis_dir", type=str, help="Root directory for fitlins output", required=True)
args = parser.parse_args()

# Set variables
study_id = args.openneuro_study
analysis_dir = args.analysis_dir
spec_path = args.spec_dir
task = args.taskname

# Get plotting coordinates
study_details = f"{spec_path}/{study_id}/{study_id}_basic-details.json"
with open(study_details, 'r') as file:
    study_info = json.load(file)
    plt_coords = tuple(study_info.get("Tasks", {}).get(task, {}).get("plot_coords"))

# Create images directory
spec_imgs_dir = Path(f"{spec_path}/{study_id}/group_{task}/imgs")
spec_imgs_dir.mkdir(parents=True, exist_ok=True)

# Define nuisance regressor patterns
noise_reg = [
    "motion_", "c_comp_", "a_comp_", "w_comp_", "t_comp_",
    "global_signal", "csf", "white_matter",
    "rot_", "trans_", "cosine"
]

# Load model specifications & study details
try:
    spec_file = f"{spec_path}/{study_id}/{study_id}-{task}_specs.json"
    with open(spec_file, 'r') as file:
        spec_data = json.load(file)
    
    spec_results = extract_model_info(model_spec=spec_data)

except Exception as e:
    print(f"Failed to load or process spec file: {e}")
    exit(1)

# Check whether run and subject nodes exist to determine if subject-level and fixed effect models are computed
has_run = False
has_subject = False
for node in spec_results['nodes']:
    if node['level'] == 'Run':
        has_run = True
    elif node['level'] == 'Subject':
        has_subject = True

# Extract study information
num_subjects = len(spec_results['subjects'])
hrf_model_type = spec_results['nodes'][0]['convolve_model']
derivative_added = spec_results['nodes'][0]['if_derivative_hrf']

if derivative_added:
    hrf_model = f"{hrf_model_type} w/ derivatives"
else:
    hrf_model = hrf_model_type
    
run_node_regressors = spec_results['nodes'][0]['regressors']

# Find and copy example contrast image & design matrix
contrast_images = list(Path(analysis_dir).rglob(f"*_task-{task}_*contrasts.svg"))
if contrast_images:
    print(f"Found example contrasts image: {contrast_images[0].name}")
    con_matrix_copy = Path(spec_imgs_dir) / f"{study_id}_task-{task}_contrast-matrix.svg"
    shutil.copy(contrast_images[0], con_matrix_copy)

design_images = list(Path(analysis_dir).rglob(f"*_task-{task}_*design.svg"))
if design_images:
    print(f"Found example design mat image: {design_images[0].name}")
    design_matrix_copy = Path(spec_imgs_dir) / f"{study_id}_task-{task}_design-matrix.svg"
    shutil.copy(design_images[0], design_matrix_copy)

# Find design matrices
design_matrices = list(Path(analysis_dir).rglob(f"*_task-{task}_*design.tsv"))

# Extract contrast specifications
contrast_dict = {}
for node in spec_results['nodes']:
    if 'contrasts' in node:
        for contrast in node['contrasts']:
            name = contrast['name']
            conditions = contrast['conditions']
            weights = contrast['weights']
            
            # Combine weights and conditions as a mathematical expression
            weighted_conditions = [f"{weight} * `{condition}`" for weight, condition in zip(weights, conditions)]
            contrast_expr = " + ".join(weighted_conditions).replace(" + -", " - ")
            
            contrast_dict[name] = [contrast_expr]

# Calculate VIF for each design matrix
all_vif_dfs = []
signal_regressors = []
noise_regressors = []

for design_mat_path in design_matrices:
    try:
        design_matrix = pd.read_csv(design_mat_path, sep='\t')
        noise_regressors = [col for col in design_matrix.columns if any(noise in col for noise in noise_reg)]
        signal_regressors = [col for col in design_matrix.columns if not any(noise in col for noise in noise_reg)]
        
        _, vif_df = gen_vifdf(
            designmat=design_matrix,
            contrastdict=contrast_dict,  
            nuisance_regressors=noise_regressors,
        )

        # Add source identifier
        vif_df["design_matrix"] = design_mat_path.name
        all_vif_dfs.append(vif_df)
    except Exception as e:
        print(f"Error processing {design_mat_path.name}: {e}")

# Create visualization if data is available
if all_vif_dfs:
    combined_vif_df = pd.concat(all_vif_dfs, ignore_index=True)
    plt.figure(figsize=(10, 6))
    sns.boxplot(x="name", y="value", data=combined_vif_df)
    plt.title("VIF Across Regressors")
    plt.xlabel("Regressor")
    plt.ylabel("Variance Inflation Factor (VIF)")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    
    # Save the figure
    plt.savefig(f"{spec_imgs_dir}/{study_id}_task-{task}_vif-boxplot.png", dpi=300)
    plt.close()
else:
    print("No VIF data available for visualization")

# Estimate average and variance of r-square maps
rquare_statmaps = list(Path(analysis_dir).rglob(f"*_task-{task}*_stat-rSquare_statmap.nii.gz"))
r2mean, r2std = calc_niftis_meanstd(path_imgs=rquare_statmaps)

        
# Find and create the group map plot
if r2mean:
    r2mean_path = f"{spec_imgs_dir}/{study_id}_task-{task}_rsquare-mean.png"
    plot_stat_map(
        stat_map_img=r2mean,
        cut_coords=plt_coords, 
        cmap="Reds",
        vmin=0,
        vmax=1,
        display_mode='ortho', 
        colorbar=True,  
        output_file=r2mean_path,
        title=f"{task}: R-squared mean across {len(rquare_statmaps)} Subject/Run Images"
    )
if r2std:
    r2std_path = f"{spec_imgs_dir}/{study_id}_task-{task}_rsquare-std.png"
    plot_stat_map(
        stat_map_img=r2std,
        cut_coords=plt_coords, 
        cmap="Reds",
        vmin=0,
        vmax=1,
        display_mode='ortho', 
        colorbar=True, 
        output_file=r2std_path,
        title=f"{task}: R-squared stdev across {len(rquare_statmaps)} Subject/Run Images"
    )

# Plot group maps if they exist
grp_map_path = f"{analysis_dir}/node-dataLevel"
if os.path.exists(grp_map_path):

    # Create group maps and save them for each contrast
    for con_name in contrast_dict.keys():
        output_img_path = f"{spec_imgs_dir}/{study_id}_task-{task}_contrast-{con_name}_map.png"
        
        # Find and create the group map plot
        grp_zstat_paths = list(Path(grp_map_path).rglob(f"*contrast-{con_name}_stat-z_statmap.nii.gz"))
        if grp_zstat_paths:
            plot_stat_map(
                stat_map_img=grp_zstat_paths[0],
                cut_coords=plt_coords, 
                display_mode='ortho', 
                colorbar=True, 
                threshold=1.5, 
                output_file=output_img_path,
                title=f"{task} {con_name}: z-stat map"
            )
else:
    print("Group map path not found.")

# Generate and save README
contrast_image = contrast_images[0] if contrast_images else None
grp_readme = generate_groupmodsummary(
    study_id=study_id, 
    task=task, 
    num_subjects=num_subjects, 
    hrf_model_type=hrf_model, 
    signal_regressors=signal_regressors, 
    noise_regressors=noise_regressors, 
    has_run=has_run, 
    has_subject=has_subject, 
    contrast_dict=contrast_dict, 
    contrast_image=Path(con_matrix_copy).name if contrast_image else None, 
    design_image=Path(design_matrix_copy).name if design_images else None, 
    spec_imgs_dir=spec_imgs_dir
)

# Save the README.md file
readme_path = os.path.join(f"{spec_path}/{study_id}/group_{task}", "README.md")
with open(readme_path, "w") as f:
    f.write(grp_readme)