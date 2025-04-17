# ds002033: ChangeDetection Task Analysis Report
## Analysis Overview
Subject-level models were fit for 40 subjects performing the ChangeDetection task.
HRF model type: spm. Data were smoothed at each run using a 5mm FWHM (default: isotropic additive smoothing)
### Regressors of Interest
trial_type.digits, trial_type.hash__red, trial_type.letters, trial_type.mirrored_digits, trial_type.mirrored_letters, trial_type.scrambled_digits, trial_type.scrambled_letters, intercept
### Nuisance Regressors
trans_x, trans_x_derivative1, trans_x_derivative1_power2, trans_x_power2, trans_y, trans_y_derivative1, trans_y_derivative1_power2, trans_y_power2, trans_z, trans_z_derivative1, trans_z_derivative1_power2, trans_z_power2, rot_x, rot_x_derivative1, rot_x_derivative1_power2, rot_x_power2, rot_y, rot_y_derivative1, rot_y_derivative1_power2, rot_y_power2, rot_z, rot_z_derivative1, rot_z_derivative1_power2, rot_z_power2, cosine00, cosine01, cosine02, cosine03
## Model Structure
- Run-level models: Yes
- Subject-level models: Yes

The run-wise contrast estimates for each subject are averaged using a fixed-effects model.
## Contrasts of Interest
- **digitsvletter**: 1*`trial_type.digits` - 1*`trial_type.letters`
- **srmdigitsvsrmletters**: 1*`trial_type.scrambled_digits` - 1*`trial_type.scrambled_letters`
- **digits**: 1*`trial_type.digits`
- **letters**: 1*`trial_type.letters`

## Figures

### Contrast Weights
![Contrast Weight](./imgs/ds002033_task-ChangeDetection_contrast-matrix.svg)

The contrast maps represents the weights used to model brain activity.

### Design Matrix
![Design Matrix](./imgs/ds002033_task-ChangeDetection_design-matrix.svg)

The example design matrix illustrates the model used in the statistical analyses for this task (Note: if motion outliers are included, the number of these will vary between subjects). Each column represents a regressor (of interest or not of interest, based on the above), and each row represents a time point in the BOLD timeseries. The colored patterns show how different experimental conditions are modeled across the scan duration (HRF model).

### Variance Inflation Factor (VIF)
![VIF Distribution](./imgs/ds002033_task-ChangeDetection_vif-boxplot.png)

The above includes 1) regressor and 2) contrast VIF estimates. The VIF boxplot quantifies multicollinearity between model regressors and how they impact contrasts (for more on contrasts VIFs, see [Dr. Mumford's repo](https://github.com/jmumford/vif_contrasts)). Lower VIF values indicate more statistically independent regressors, which is desirable for reliable parameter estimation. VIFs were estimated using the first-level model design matrices -- nusiance regressors are excluded here for brevity.

### Voxelwise Model Variance Explained (r-squared)
Voxelwise R-squared values represent the proportion of variance explained by the model at each voxel in the brain. The R-squared images shown here are calculated across runs, subjects and/or sessions (dependent on data Fitlins nodes) for the study and task.

#### Voxelwise Average (Mean)
The **mean** R-squared image reflect the average of the R-squared values across all subjects and runs.In other words, the fluctuation in how much variability in the BOLD signal the model explains at a given voxel.
![R Square](./imgs/ds002033_task-ChangeDetection_rsquare-mean.png)

#### Voxelwise Variance (Standard Deviation)
The **standard deviation** (or variance) image provides insights into the variability of model performance.In otherwords, across subjects, runs and/or sessions, how much variability there is in the models ability to explain the BOLD at a given voxel.

#### Flagged Subjects
The quality assessment pipeline evaluates volumetric data across multiple dimensions to identify problematic datasets. Subjects are flagged using: 

  - Dice Estimate: Similarity coefficient between subject r-squared maps and Target Space MNI152 mask falls below .85 
  - Voxels Outside of Mask: Percentage of voxels outside of the target brain mask is greater than the .10% (liberal threshold due to liberal brain masks in fMRIPrep BOLD) 

The subjects flagged for ChangeDetection are:
sub01_run01, sub01_run02, sub01_run03, sub01_run04, sub02_run01, sub02_run02, sub02_run04, sub03_run01, sub03_run02, sub03_run03, sub03_run04, sub04_run01, sub04_run02, sub04_run03, sub04_run04, sub07_run01, sub07_run02, sub07_run03, sub07_run04, sub08_run01, sub08_run02, sub08_run03, sub08_run04, sub09_run01, sub09_run02, sub09_run03, sub09_run04, sub10_run01, sub10_run02, sub10_run03, sub10_run04, sub11_run01, sub11_run02, sub11_run03, sub11_run04, sub13_run01, sub13_run02, sub13_run03, sub13_run04, sub14_run01, sub14_run02, sub14_run03, sub14_run04, sub15_run01, sub15_run02, sub15_run03, sub15_run04, sub16_run01, sub16_run02, sub16_run03, sub16_run04, sub17_run01, sub17_run02, sub17_run03, sub17_run04, sub20_run01, sub20_run02, sub20_run03, sub20_run04, sub22_run01, sub22_run02, sub22_run03, sub22_run04, sub23_run01, sub23_run02, sub23_run03, sub23_run04, sub24_run01, sub24_run02, sub24_run03, sub24_run04, sub26_run01, sub26_run02, sub26_run03, sub26_run04, sub27_run01, sub27_run02, sub27_run03, sub27_run04, sub28_run01, sub28_run02, sub28_run03, sub28_run04, sub29_run01, sub29_run02, sub29_run03, sub29_run04, sub32_run01, sub32_run02, sub32_run03, sub32_run04, sub33_run01, sub33_run02, sub33_run03, sub33_run04, sub34_run01, sub34_run02, sub34_run03, sub34_run04, sub35_run01, sub35_run02, sub35_run03, sub35_run04, sub36_run01, sub36_run02, sub36_run03, sub36_run04, sub38_run01, sub38_run02, sub38_run03, sub38_run04, sub39_run01, sub39_run02, sub40_run01, sub40_run02, sub40_run03, sub40_run04, sub42_run01, sub42_run02, sub42_run03, sub42_run04

The distribution for subjects and runs in ChangeDetection are below. 

![Dice](./imgs/ds002033_task-ChangeDetection_hist-dicesimilarity.png)
![Voxels Out](./imgs/ds002033_task-ChangeDetection_hist-voxoutmask.png)

### Statistical Maps

#### digitsvletter
![digitsvletter Map](./imgs/ds002033_task-ChangeDetection_contrast-digitsvletter_map.png)

#### srmdigitsvsrmletters
![srmdigitsvsrmletters Map](./imgs/ds002033_task-ChangeDetection_contrast-srmdigitsvsrmletters_map.png)

#### digits
![digits Map](./imgs/ds002033_task-ChangeDetection_contrast-digits_map.png)

#### letters
![letters Map](./imgs/ds002033_task-ChangeDetection_contrast-letters_map.png)
