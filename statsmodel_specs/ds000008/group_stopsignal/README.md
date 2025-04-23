# ds000008: stopsignal Task Analysis Report
## Analysis Overview
Subject-level models were fit for 14 subjects performing the stopsignal task.
HRF model type: spm. Data were smoothed at each run using a 5mm FWHM (default: isotropic additive smoothing)
### Regressors of Interest
trial_type.failedstop, trial_type.go, trial_type.junk, trial_type.successfulstop, rt_reg.rt, intercept
### Nuisance Regressors
trans_x, trans_x_derivative1, trans_x_derivative1_power2, trans_x_power2, trans_y, trans_y_derivative1, trans_y_derivative1_power2, trans_y_power2, trans_z, trans_z_derivative1, trans_z_derivative1_power2, trans_z_power2, rot_x, rot_x_derivative1, rot_x_derivative1_power2, rot_x_power2, rot_y, rot_y_derivative1, rot_y_derivative1_power2, rot_y_power2, rot_z, rot_z_derivative1, rot_z_derivative1_power2, rot_z_power2, cosine00, cosine01, cosine02, cosine03
## Model Structure
- Run-level models: Yes
- Subject-level models: Yes

The run-wise contrast estimates for each subject are averaged using a fixed-effects model.
## Contrasts of Interest
- **successstop**: 1*`trial_type.successfulstop`
- **go**: 1*`trial_type.go`
- **successstopvgo**: 1*`trial_type.successfulstop` - 1*`trial_type.go`
- **failstopvgo**: 1*`trial_type.failedstop` - 1*`trial_type.go`
- **successstopvfailstop**: 1*`trial_type.successfulstop` - 1*`trial_type.failedstop`
- **allstopvGo**: 0.5*`trial_type.successfulstop` + 0.5*`trial_type.failedstop` - 1*`trial_type.go`
- **rt**: 1*`rt_reg.rt`

## Figures

### Contrast Weights
![Contrast Weight](./imgs/ds000008_task-stopsignal_contrast-matrix.svg)

The contrast maps represents the weights used to model brain activity.

### Design Matrix
![Design Matrix](./imgs/ds000008_task-stopsignal_design-matrix.svg)

The example design matrix illustrates the model used in the statistical analyses for this task (Note: if motion outliers are included, the number of these will vary between subjects). Each column represents a regressor (of interest or not of interest, based on the above), and each row represents a time point in the BOLD timeseries. The colored patterns show how different experimental conditions are modeled across the scan duration (HRF model).

### Variance Inflation Factor (VIF)
![VIF Distribution](./imgs/ds000008_task-stopsignal_vif-boxplot.png)

The above includes 1) regressor and 2) contrast VIF estimates. The VIF boxplot quantifies multicollinearity between model regressors and how they impact contrasts (for more on contrasts VIFs, see [Dr. Mumford's repo](https://github.com/jmumford/vif_contrasts)). Lower VIF values indicate more statistically independent regressors, which is desirable for reliable parameter estimation. VIFs were estimated using the first-level model design matrices -- nusiance regressors are excluded here for brevity.

### Voxelwise Model Variance Explained (r-squared)
Voxelwise R-squared values represent the proportion of variance explained by the model at each voxel in the brain. The R-squared images shown here are calculated across runs, subjects and/or sessions (dependent on data Fitlins nodes) for the study and task.

#### Voxelwise Average (Mean)
The **mean** R-squared image reflect the average of the R-squared values across all subjects and runs.In other words, the fluctuation in how much variability in the BOLD signal the model explains at a given voxel.
![R Square](./imgs/ds000008_task-stopsignal_rsquare-mean.png)

#### Voxelwise Variance (Standard Deviation)
The **standard deviation** (or variance) image provides insights into the variability of model performance.In otherwords, across subjects, runs and/or sessions, how much variability there is in the models ability to explain the BOLD at a given voxel.

#### Flagged Subjects
The quality assessment pipeline evaluates volumetric data across multiple dimensions to identify problematic datasets. Subjects are flagged using: 

  - Dice Estimate: Similarity coefficient between subject r-squared maps and Target Space MNI152 mask falls below .85 
  - Voxels Outside of Mask: Percentage of voxels outside of the target brain mask is greater than the .10% (liberal threshold due to liberal brain masks in fMRIPrep BOLD) 

The subjects flagged for stopsignal are:
sub04_run01, sub04_run02, sub04_run03, sub04_run1, sub04_run2, sub04_run3, sub06_run01, sub06_run03, sub06_run1, sub06_run3

The distribution for subjects and runs in stopsignal are below. 

![Dice](./imgs/ds000008_task-stopsignal_hist-dicesimilarity.png)
![Voxels Out](./imgs/ds000008_task-stopsignal_hist-voxoutmask.png)

### Statistical Maps

#### successstop
![successstop Map](./imgs/ds000008_task-stopsignal_contrast-successstop_map.png)

#### go
![go Map](./imgs/ds000008_task-stopsignal_contrast-go_map.png)

#### successstopvgo
![successstopvgo Map](./imgs/ds000008_task-stopsignal_contrast-successstopvgo_map.png)

#### failstopvgo
![failstopvgo Map](./imgs/ds000008_task-stopsignal_contrast-failstopvgo_map.png)

#### successstopvfailstop
![successstopvfailstop Map](./imgs/ds000008_task-stopsignal_contrast-successstopvfailstop_map.png)

#### allstopvGo
![allstopvGo Map](./imgs/ds000008_task-stopsignal_contrast-allstopvGo_map.png)

#### rt
![rt Map](./imgs/ds000008_task-stopsignal_contrast-rt_map.png)
