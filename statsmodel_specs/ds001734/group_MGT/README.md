# ds001734: MGT Task Analysis Report
## Analysis Overview
Subject-level models were fit for 108 subjects performing the MGT task.
HRF model type: spm. Data were smoothed at each run using a 5mm FWHM (default: isotropic additive smoothing)
### Regressors of Interest
trial_type.decision, trial_type.missed, gain_demean, loss_demean, rt_reg.rt, intercept
### Nuisance Regressors
trans_x, trans_x_derivative1, trans_x_derivative1_power2, trans_x_power2, trans_y, trans_y_derivative1, trans_y_derivative1_power2, trans_y_power2, trans_z, trans_z_derivative1, trans_z_derivative1_power2, trans_z_power2, rot_x, rot_x_derivative1, rot_x_derivative1_power2, rot_x_power2, rot_y, rot_y_derivative1, rot_y_derivative1_power2, rot_y_power2, rot_z, rot_z_derivative1, rot_z_derivative1_power2, rot_z_power2, cosine00, cosine01, cosine02, cosine03, cosine04, cosine05
## Model Structure
- Run-level models: Yes
- Subject-level models: Yes

The run-wise contrast estimates for each subject are averaged using a fixed-effects model.
## Contrasts of Interest
- **alltrials**: ['1 * `trial_type.decision`']
- **gain**: ['1 * `gain_demean`']
- **loss**: ['1 * `loss_demean`']
- **gainvloss**: ['1 * `gain_demean` - 1 * `loss_demean`']
- **rt**: ['1 * `rt_reg.rt`']

## Figures

### Contrast Weights
![Contrast Weight](./imgs/ds001734_task-MGT_contrast-matrix.svg)

The contrast maps represents the weights used to model brain activity.

### Design Matrix
![Design Matrix](./imgs/ds001734_task-MGT_design-matrix.svg)

The example design matrix illustrates the model used in the statistical analyses for this task (Note: if motion outliers are included, the number of these will vary between subjects). Each column represents a regressor (of interest or not of interest, based on the above), and each row represents a time point in the BOLD timeseries. The colored patterns show how different experimental conditions are modeled across the scan duration (HRF model).

### Variance Inflation Factor (VIF)
![VIF Distribution](./imgs/ds001734_task-MGT_vif-boxplot.png)

The Variance Inflation Factor (VIF) boxplot quantifies multicollinearity between model regressors. Lower VIF values indicate more statistically independent regressors, which is desirable for reliable parameter estimation. VIFs were estimated using the first-level model design matrices -- nusiance regressors are excluded here for brevity.

### Voxelwise Model Variance Explained (r-squared)
Voxelwise R-squared values represent the proportion of variance explained by the model at each voxel in the brain. The R-squared images shown here are calculated across runs, subjects and/or sessions (dependent on data Fitlins nodes) for the study and task.

#### Voxelwise Average (Mean)
The **mean** R-squared image reflect the average of the R-squared values across all subjects and runs.In other words, the fluctuation in how much variability in the BOLD signal the model explains at a given voxel.
![R Square](./imgs/ds001734_task-MGT_rsquare-mean.png)

#### Voxelwise Variance (Standard Deviation)
The **standard deviation** (or variance) image provides insights into the variability of model performance.In otherwords, across subjects, runs and/or sessions, how much variability there is in the models ability to explain the BOLD at a given voxel.
/n#### Flagged Subjects
The quality assessment pipeline evaluates volumetric data across multiple dimensions to identify problematic datasets. Subjects are flagged using a 10 percentile threshold.

  - Dice similarity coefficient between subject r-squared maps and Target Space MNI152 mask falls below the 10th percentile 
  - The percentage of voxels outside of the target brain mask is greater than the 10th percentile

The subjects flagged for MGT are:
sub001_run1, sub001_run2, sub001_run4, sub002_run4, sub003_run4, sub006_run1, sub006_run2, sub006_run3, sub006_run4, sub009_run1, sub009_run2, sub010_run2, sub010_run3, sub011_run4, sub014_run4, sub015_run1, sub015_run2, sub015_run3, sub015_run4, sub017_run4, sub019_run4, sub020_run2, sub022_run4, sub025_run1, sub025_run2, sub025_run4, sub032_run3, sub035_run3, sub037_run1, sub037_run2, sub037_run4, sub039_run4, sub045_run1, sub045_run4, sub046_run3, sub052_run3, sub054_run4, sub056_run1, sub056_run3, sub056_run4, sub057_run1, sub059_run2, sub059_run4, sub060_run1, sub060_run2, sub060_run3, sub060_run4, sub062_run1, sub062_run2, sub066_run3, sub071_run1, sub071_run2, sub075_run2, sub075_run3, sub080_run1, sub082_run2, sub092_run2, sub093_run1, sub093_run3, sub093_run4, sub095_run2, sub100_run1, sub100_run2, sub100_run3, sub100_run4, sub105_run4, sub107_run1, sub107_run2, sub107_run3, sub107_run4, sub110_run2, sub110_run3, sub110_run4, sub113_run3, sub113_run4, sub114_run1, sub114_run3, sub117_run1, sub117_run2, sub117_run3, sub117_run4, sub119_run2, sub119_run4, sub124_run1, sub124_run2, sub124_run3, sub124_run4

The distribution for subjects and runs in MGT are below. 

![Dice](./imgs/ds001734_task-MGT_hist-dicesimilarity.png)
![Voxels Out](./imgs/ds001734_task-MGT_hist-voxoutmask.png)

### Statistical Maps

#### alltrials
![alltrials Map](./imgs/ds001734_task-MGT_contrast-alltrials_map.png)

#### gain
![gain Map](./imgs/ds001734_task-MGT_contrast-gain_map.png)

#### loss
![loss Map](./imgs/ds001734_task-MGT_contrast-loss_map.png)

#### gainvloss
![gainvloss Map](./imgs/ds001734_task-MGT_contrast-gainvloss_map.png)

#### rt
![rt Map](./imgs/ds001734_task-MGT_contrast-rt_map.png)
