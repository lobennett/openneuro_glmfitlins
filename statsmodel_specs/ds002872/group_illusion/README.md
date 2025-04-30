# ds002872: illusion Task Analysis Report
## Analysis Overview
Subject-level models were fit for 39 subjects performing the illusion task.
HRF model type: spm. Data were smoothed at each run using a 5mm FWHM (default: isotropic additive smoothing)
### Regressors of Interest
trial_type.t_low, trial_type.t_hi, trial_type.p_low, trial_type.p_hi, intercept
### Nuisance Regressors
trans_x, trans_x_derivative1, trans_x_derivative1_power2, trans_x_power2, trans_y, trans_y_derivative1, trans_y_derivative1_power2, trans_y_power2, trans_z, trans_z_derivative1, trans_z_derivative1_power2, trans_z_power2, rot_x, rot_x_derivative1, rot_x_derivative1_power2, rot_x_power2, rot_y, rot_y_derivative1, rot_y_derivative1_power2, rot_y_power2, rot_z, rot_z_derivative1, rot_z_derivative1_power2, rot_z_power2, cosine00, cosine01, cosine02, cosine03
## Model Structure
- Run-level models: Yes
- Subject-level models: Yes

The run-wise contrast estimates for each subject are averaged using a fixed-effects model.
## Contrasts of Interest
- **vibration**: 0.5*`trial_type.p_hi` + 0.5*`trial_type.p_low`
- **texture**: 0.5*`trial_type.t_hi` + 0.5*`trial_type.t_low`
- **highvlow**: 0.5*`trial_type.t_hi` + 0.5*`trial_type.p_hi` - 0.5*`trial_type.p_low` - 0.5*`trial_type.t_low`
- **texturevpnevib**: 0.5*`trial_type.t_hi` + 0.5*`trial_type.t_low` - 0.5*`trial_type.p_hi` - 0.5*`trial_type.p_low`
- **vibrationhighvlow**: 1*`trial_type.p_hi` - 1*`trial_type.p_low`
- **texturehighvlow**: 1*`trial_type.t_hi` - 1*`trial_type.t_low`

## Figures

### Contrast Weights
![Contrast Weight](./imgs/ds002872_task-illusion_contrast-matrix.svg)

The contrast maps represents the weights used to model brain activity.

### Design Matrix
![Design Matrix](./imgs/ds002872_task-illusion_design-matrix.svg)

The example design matrix illustrates the model used in the statistical analyses for this task (Note: if motion outliers are included, the number of these will vary between subjects). Each column represents a regressor (of interest or not of interest, based on the above), and each row represents a time point in the BOLD timeseries. The colored patterns show how different experimental conditions are modeled across the scan duration (HRF model).

### Variance Inflation Factor (VIF)
![VIF Distribution](./imgs/ds002872_task-illusion_vif-boxplot.png)

The above includes 1) regressor and 2) contrast VIF estimates. The VIF boxplot quantifies multicollinearity between model regressors and how they impact contrasts (for more on contrasts VIFs, see [Dr. Mumford's repo](https://github.com/jmumford/vif_contrasts)). Lower VIF values indicate more statistically independent regressors, which is desirable for reliable parameter estimation. VIFs were estimated using the first-level model design matrices -- nusiance regressors are excluded here for brevity.

### Voxelwise Model Variance Explained (r-squared)
Voxelwise R-squared values represent the proportion of variance explained by the model at each voxel in the brain. The R-squared images shown here are calculated across runs, subjects and/or sessions (dependent on data Fitlins nodes) for the study and task.

#### Voxelwise Average (Mean)
The **mean** R-squared image reflect the average of the R-squared values across all subjects and runs.In other words, the fluctuation in how much variability in the BOLD signal the model explains at a given voxel.
![R Square](./imgs/ds002872_task-illusion_rsquare-mean.png)

#### Voxelwise Variance (Standard Deviation)
The **standard deviation** (or variance) image provides insights into the variability of model performance.In otherwords, across subjects, runs and/or sessions, how much variability there is in the models ability to explain the BOLD at a given voxel.

#### Flagged Subjects
The quality assessment pipeline evaluates volumetric data across multiple dimensions to identify problematic datasets. Subjects are flagged using: 

  - Dice Estimate: Similarity coefficient between subject r-squared maps and Target Space MNI152 mask falls below .85 
  - Voxels Outside of Mask: Percentage of voxels outside of the target brain mask is greater than the .10% (liberal threshold due to liberal brain masks in fMRIPrep BOLD) 

The subjects flagged for illusion are:
sub-01_run-01, sub-01_run-02, sub-01_run-03, sub-01_run-04, sub-02_run-01, sub-02_run-02, sub-02_run-03, sub-02_run-04, sub-04_run-01, sub-04_run-02, sub-04_run-03, sub-04_run-04, sub-05_run-01, sub-05_run-02, sub-05_run-03, sub-05_run-04, sub-06_run-01, sub-06_run-02, sub-06_run-03, sub-06_run-04, sub-08_run-01, sub-08_run-02, sub-08_run-03, sub-08_run-04, sub-09_run-01, sub-09_run-02, sub-09_run-03, sub-09_run-04, sub-10_run-01, sub-10_run-02, sub-10_run-03, sub-10_run-04, sub-11_run-01, sub-11_run-02, sub-11_run-04, sub-12_run-01, sub-12_run-02, sub-12_run-03, sub-12_run-04, sub-14_run-03, sub-14_run-04, sub-15_run-01, sub-15_run-02, sub-15_run-03, sub-15_run-04, sub-16_run-01, sub-16_run-02, sub-16_run-03, sub-16_run-04, sub-17_run-01, sub-17_run-02, sub-17_run-03, sub-17_run-04, sub-18_run-01, sub-18_run-02, sub-18_run-03, sub-18_run-04, sub-19_run-01, sub-19_run-02, sub-19_run-03, sub-19_run-04, sub-20_run-01, sub-20_run-02, sub-20_run-03, sub-20_run-04, sub-21_run-01, sub-21_run-02, sub-21_run-03, sub-21_run-04, sub-22_run-01, sub-22_run-02, sub-22_run-03, sub-22_run-04, sub-23_run-01, sub-23_run-02, sub-23_run-03, sub-23_run-04, sub-24_run-01, sub-24_run-02, sub-24_run-03, sub-24_run-04, sub-25_run-01, sub-25_run-02, sub-25_run-03, sub-25_run-04, sub-26_run-01, sub-26_run-02, sub-26_run-03, sub-26_run-05, sub-27_run-01, sub-28_run-01, sub-28_run-02, sub-28_run-03, sub-28_run-04, sub-30_run-01, sub-30_run-03, sub-30_run-04, sub-31_run-02, sub-31_run-04, sub-32_run-01, sub-32_run-02, sub-32_run-03, sub-32_run-04, sub-33_run-01, sub-33_run-02, sub-33_run-03, sub-33_run-04, sub-35_run-03, sub-36_run-01, sub-36_run-02, sub-36_run-03, sub-36_run-04, sub-37_run-04, sub-39_run-01, sub-39_run-02, sub-39_run-03, sub-39_run-04, sub-41_run-01, sub-41_run-02, sub-41_run-03, sub-41_run-04

The distribution for subjects and runs in illusion are below. 

![Dice](./imgs/ds002872_task-illusion_hist-dicesimilarity.png)
![Voxels Out](./imgs/ds002872_task-illusion_hist-voxoutmask.png)

### Statistical Maps

#### vibration
![vibration Map](./imgs/ds002872_task-illusion_contrast-vibration_map.png)

#### texture
![texture Map](./imgs/ds002872_task-illusion_contrast-texture_map.png)

#### highvlow
![highvlow Map](./imgs/ds002872_task-illusion_contrast-highvlow_map.png)

#### texturevpnevib
![texturevpnevib Map](./imgs/ds002872_task-illusion_contrast-texturevpnevib_map.png)

#### vibrationhighvlow
![vibrationhighvlow Map](./imgs/ds002872_task-illusion_contrast-vibrationhighvlow_map.png)

#### texturehighvlow
![texturehighvlow Map](./imgs/ds002872_task-illusion_contrast-texturehighvlow_map.png)
