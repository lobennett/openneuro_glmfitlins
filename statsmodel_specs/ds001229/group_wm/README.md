# ds001229: wm Task Analysis Report

The size of the Fitlins Derivatives for ds001229 wm is 4.8G with 3206 files.

## Statistical Analysis Boilerplate

### First-level Analysis
FitLins was employed to estimate task-related BOLD activity in the wm task for 27 subjects. In this instance, FitLins used the Nilearn estimator in its statistical modeling of the BOLD data. For each participant, 7 regressors of interest (out of total 8 regressors; see list below) were convolved with a spm hemodynamic response function in Nilearn. The design matrix incorporated both regressors of interest and 32 additional components, including a drift cosine basis set and nuisance regressors to account for sources of noise in the BOLD signal. Following Nilearn's *FirstLevelModel* default procedure, each voxel's timeseries was mean-scaled by each voxel's mean of the timeseries. Data were smoothed at each run using a 5mm full-width at half maximum smoothing kernal (default: isotropic additive smoothing). From the resulting model, 7 distinct contrast estimates were computed (see list below).

### Model Outputs
For each participant's run, outputs include but are not limited to:
- A complete design matrix visualization
- Model fit statistics (R-squared and log-likelihood maps)
- For each contrast: effect size maps (beta values), t-statistic maps, z-statistic maps and variance maps

An example design matrix and contrast weight specifications are provided below.

### Group-level Analysis
Within-subject runs were combined using Nilearn's *compute_fixed_effects* function (without precision weighting; `precision_weighted=False`). These subject-level average statistical maps were then entered into a group-level analysis using a two-sided one-sample t-test to estimate average univariate activation patterns.

## Additional Analysis Details 
### Regressors of Interest
trial_type.face_catch, trial_type.face_real, trial_type.lexdec_catch, trial_type.lexdec_real, trial_type.scene_catch, trial_type.scene_real, nprobes, intercept
#### Convolved Regressors
trial_type.face_catch, trial_type.face_real, trial_type.lexdec_catch, trial_type.lexdec_real, trial_type.scene_catch, trial_type.scene_real, nprobes
### Nuisance Regressors
trans_x, trans_x_derivative1, trans_x_derivative1_power2, trans_x_power2, trans_y, trans_y_derivative1, trans_y_derivative1_power2, trans_y_power2, trans_z, trans_z_derivative1, trans_z_derivative1_power2, trans_z_power2, rot_x, rot_x_derivative1, rot_x_derivative1_power2, rot_x_power2, rot_y, rot_y_derivative1, rot_y_derivative1_power2, rot_y_power2, rot_z, rot_z_derivative1, rot_z_derivative1_power2, rot_z_power2, cosine00, cosine01, cosine02, cosine03, cosine04, cosine05, cosine06, cosine07
## Model Structure
- Run-level models: Yes
- Subject-level models: Yes

## Contrasts of Interest
- **facescenevlexdec**: 0.5*`trial_type.face_real` + 0.5*`trial_type.scene_real` - 1*`trial_type.lexdec_real`
- **oglexreal**: 1*`trial_type.lexdec_real`
- **pmfacesreal**: 1*`trial_type.face_real`
- **pmscenereal**: 1*`trial_type.scene_real`
- **scenerealvcatch**: 1*`trial_type.scene_real` - 1*`trial_type.scene_catch`
- **facerealvcatch**: 1*`trial_type.face_real` - 1*`trial_type.face_catch`
- **lexrealvcatch**: 1*`trial_type.lexdec_real` - 1*`trial_type.lexdec_catch`

## Figures

### Contrast Weights
![Contrast Weight](./files/ds001229_task-wm_contrast-matrix.svg)

The contrast maps represents the weights used to model brain activity.

### Design Matrix
![Design Matrix](./files/ds001229_task-wm_design-matrix.svg)

The example design matrix illustrates the model used in the statistical analyses for this task (Note: if motion outliers are included, the number of these will vary between subjects). Each column represents a regressor (of interest or not of interest, based on the above), and each row represents a time point in the BOLD timeseries. The colored patterns show how different experimental conditions are modeled across the scan duration (HRF model).

### Variance Inflation Factor (VIF)
![VIF Distribution](./files/ds001229_task-wm_vif-boxplot.png)

The above includes 1) regressor and 2) contrast VIF estimates. The VIF boxplot quantifies multicollinearity between model regressors and how they impact contrasts (for more on contrasts VIFs, see [Dr. Mumford's repo](https://github.com/jmumford/vif_contrasts)). Lower VIF values indicate more statistically independent regressors, which is desirable for reliable parameter estimation. VIFs were estimated using the first-level model design matrices -- nusiance regressors are excluded here for brevity.

### Voxelwise Model Variance Explained (r-squared)
Voxelwise R-squared values represent the proportion of variance explained by the model at each voxel in the brain. The R-squared images shown here are calculated across runs, subjects and/or sessions (dependent on data Fitlins nodes) for the study and task.

#### Voxelwise Average (Mean)
The **mean** R-squared image reflect the average of the R-squared values across all subjects and runs.In other words, the fluctuation in how much variability in the BOLD signal the model explains at a given voxel.
![R Square](./files/ds001229_task-wm_rsquare-mean.png)

#### Voxelwise Variance (Standard Deviation)
The **standard deviation** (or variance) image provides insights into the variability of model performance.In otherwords, across subjects, runs and/or sessions, how much variability there is in the models ability to explain the BOLD at a given voxel.

#### Flagged Subjects
The quality assessment pipeline evaluates volumetric data across multiple dimensions to identify problematic datasets. Subjects are flagged using: 

  - Dice Estimate: Similarity coefficient between subject r-squared maps and Target Space MNI152 mask falls below .80 (captures dropout and excess non-brain voxels) 
  - Voxels Outside of Mask: Percentage of voxels outside of the target brain mask is greater than the .10% (liberal threshold due to liberal brain masks in fMRIPrep BOLD, captures mostly non-brain voxels) 

The subjects flagged for wm are:
sub-05_run-03, sub-11_run-03, sub-15_run-03, sub-17_run-02, sub-17_run-03

The distribution for subjects and runs in wm are below. 

![Dice](./files/ds001229_task-wm_hist-dicesimilarity.png)
![Voxels Out](./files/ds001229_task-wm_hist-voxoutmask.png)

### Statistical Maps

#### facescenevlexdec
![facescenevlexdec Map](./files/ds001229_task-wm_contrast-facescenevlexdec_map.png)

#### oglexreal
![oglexreal Map](./files/ds001229_task-wm_contrast-oglexreal_map.png)

#### pmfacesreal
![pmfacesreal Map](./files/ds001229_task-wm_contrast-pmfacesreal_map.png)

#### pmscenereal
![pmscenereal Map](./files/ds001229_task-wm_contrast-pmscenereal_map.png)

#### scenerealvcatch
![scenerealvcatch Map](./files/ds001229_task-wm_contrast-scenerealvcatch_map.png)

#### facerealvcatch
![facerealvcatch Map](./files/ds001229_task-wm_contrast-facerealvcatch_map.png)

#### lexrealvcatch
![lexrealvcatch Map](./files/ds001229_task-wm_contrast-lexrealvcatch_map.png)
