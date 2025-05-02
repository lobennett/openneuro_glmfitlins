# ds001715: dts Task Analysis Report

The size of the Fitlins Derivatives for ds001715 dts is 33G with 21056 files.

## Statistical Analysis Boilerplate

### First-level Analysis
FitLins was employed to estimate task-related BOLD activity in the dts task for 34 subjects. In this instance, FitLins used the Nilearn estimator in its statistical modeling of the BOLD data. For each participant, 5 regressors of interest (see list below) were convolved with a spm hemodynamic response function in Nilearn. The design matrix incorporated both regressors of interest and 30 additional components, including a drift cosine basis set and nuisance regressors to account for sources of noise in the BOLD signal. Following Nilearn's *FirstLevelModel* default procedure, each voxel's timeseries was mean-scaled by each voxel's mean BOLD signal. Data were smoothed at each run using a 5mm full-width at half maximum smoothing kernal (default: isotropic additive smoothing). From the resulting model, 7 distinct contrast estimates were computed (see list below).

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
signedcolor_cohright, missed_trial, signedcolor_abs, rt_reg.1, intercept
### Nuisance Regressors
signedmotion_cohright, signedmotion_abs, trans_x, trans_x_derivative1, trans_x_derivative1_power2, trans_x_power2, trans_y, trans_y_derivative1, trans_y_derivative1_power2, trans_y_power2, trans_z, trans_z_derivative1, trans_z_derivative1_power2, trans_z_power2, rot_x, rot_x_derivative1, rot_x_derivative1_power2, rot_x_power2, rot_y, rot_y_derivative1, rot_y_derivative1_power2, rot_y_power2, rot_z, rot_z_derivative1, rot_z_derivative1_power2, rot_z_power2, cosine00, cosine01, cosine02, cosine03
## Model Structure
- Run-level models: Yes
- Subject-level models: Yes

## Contrasts of Interest
- **motionaligneffect**: 1*`signedmotion_cohright`
- **coloraligneffect**: 1*`signedcolor_cohright`
- **alignmotionvcolor**: 1*`signedmotion_cohright` - 1*`signedcolor_cohright`
- **absmotioneffect**: 1*`signedcolor_abs`
- **abscolorneffect**: 1*`signedcolor_abs`
- **absmotionvcolor**: 1*`signedcolor_abs` - 1*`signedcolor_abs`
- **rt**: 1*`rt_reg.1`

## Figures

### Contrast Weights
![Contrast Weight](./imgs/ds001715_task-dts_contrast-matrix.svg)

The contrast maps represents the weights used to model brain activity.

### Design Matrix
![Design Matrix](./imgs/ds001715_task-dts_design-matrix.svg)

The example design matrix illustrates the model used in the statistical analyses for this task (Note: if motion outliers are included, the number of these will vary between subjects). Each column represents a regressor (of interest or not of interest, based on the above), and each row represents a time point in the BOLD timeseries. The colored patterns show how different experimental conditions are modeled across the scan duration (HRF model).

### Variance Inflation Factor (VIF)
![VIF Distribution](./imgs/ds001715_task-dts_vif-boxplot.png)

The above includes 1) regressor and 2) contrast VIF estimates. The VIF boxplot quantifies multicollinearity between model regressors and how they impact contrasts (for more on contrasts VIFs, see [Dr. Mumford's repo](https://github.com/jmumford/vif_contrasts)). Lower VIF values indicate more statistically independent regressors, which is desirable for reliable parameter estimation. VIFs were estimated using the first-level model design matrices -- nusiance regressors are excluded here for brevity.

### Voxelwise Model Variance Explained (r-squared)
Voxelwise R-squared values represent the proportion of variance explained by the model at each voxel in the brain. The R-squared images shown here are calculated across runs, subjects and/or sessions (dependent on data Fitlins nodes) for the study and task.

#### Voxelwise Average (Mean)
The **mean** R-squared image reflect the average of the R-squared values across all subjects and runs.In other words, the fluctuation in how much variability in the BOLD signal the model explains at a given voxel.
![R Square](./imgs/ds001715_task-dts_rsquare-mean.png)

#### Voxelwise Variance (Standard Deviation)
The **standard deviation** (or variance) image provides insights into the variability of model performance.In otherwords, across subjects, runs and/or sessions, how much variability there is in the models ability to explain the BOLD at a given voxel.

#### Flagged Subjects
The quality assessment pipeline evaluates volumetric data across multiple dimensions to identify problematic datasets. Subjects are flagged using: 

  - Dice Estimate: Similarity coefficient between subject r-squared maps and Target Space MNI152 mask falls below .85 
  - Voxels Outside of Mask: Percentage of voxels outside of the target brain mask is greater than the .10% (liberal threshold due to liberal brain masks in fMRIPrep BOLD) 

The subjects flagged for dts are:
sub-01_run-01, sub-01_run-02, sub-01_run-03, sub-01_run-04, sub-01_run-05, sub-01_run-06, sub-01_run-07, sub-01_run-08, sub-01_run-09, sub-01_run-10, sub-01_run-11, sub-01_run-12, sub-05_run-10, sub-08_run-02, sub-08_run-05, sub-08_run-11, sub-08_run-12, sub-09_run-01, sub-09_run-02, sub-09_run-03, sub-09_run-04, sub-09_run-05, sub-09_run-06, sub-09_run-07, sub-09_run-08, sub-09_run-09, sub-09_run-10, sub-09_run-11, sub-09_run-12, sub-23_run-01, sub-23_run-02, sub-23_run-03, sub-23_run-04, sub-23_run-05, sub-23_run-06, sub-23_run-07, sub-23_run-08, sub-23_run-09, sub-23_run-10, sub-23_run-11, sub-23_run-12, sub-27_run-08, sub-32_run-01, sub-32_run-02, sub-32_run-03, sub-32_run-04, sub-32_run-05, sub-32_run-06, sub-32_run-07, sub-32_run-08, sub-32_run-09, sub-32_run-10, sub-32_run-11, sub-32_run-12

The distribution for subjects and runs in dts are below. 

![Dice](./imgs/ds001715_task-dts_hist-dicesimilarity.png)
![Voxels Out](./imgs/ds001715_task-dts_hist-voxoutmask.png)

### Statistical Maps

#### motionaligneffect
![motionaligneffect Map](./imgs/ds001715_task-dts_contrast-motionaligneffect_map.png)

#### coloraligneffect
![coloraligneffect Map](./imgs/ds001715_task-dts_contrast-coloraligneffect_map.png)

#### alignmotionvcolor
![alignmotionvcolor Map](./imgs/ds001715_task-dts_contrast-alignmotionvcolor_map.png)

#### absmotioneffect
![absmotioneffect Map](./imgs/ds001715_task-dts_contrast-absmotioneffect_map.png)

#### abscolorneffect
![abscolorneffect Map](./imgs/ds001715_task-dts_contrast-abscolorneffect_map.png)

#### absmotionvcolor
![absmotionvcolor Map](./imgs/ds001715_task-dts_contrast-absmotionvcolor_map.png)

#### rt
![rt Map](./imgs/ds001715_task-dts_contrast-rt_map.png)
