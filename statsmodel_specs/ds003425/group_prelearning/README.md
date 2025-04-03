# ds003425: prelearning Task Analysis Report
## Analysis Overview
Subject-level models were fit for 11 subjects performing the prelearning task.
HRF model type: spm w/ derivatives
### Regressors of Interest
trial_type.2, trial_type.2_derivative, trial_type.3, trial_type.3_derivative, trial_type.4, trial_type.4_derivative, trial_type.5, trial_type.5_derivative, trial_type.6, trial_type.6_derivative, intercept
### Nuisance Regressors
trans_x, trans_x_derivative1, trans_x_derivative1_power2, trans_x_power2, trans_y, trans_y_derivative1, trans_y_derivative1_power2, trans_y_power2, trans_z, trans_z_derivative1, trans_z_derivative1_power2, trans_z_power2, rot_x, rot_x_derivative1, rot_x_derivative1_power2, rot_x_power2, rot_y, rot_y_derivative1, rot_y_derivative1_power2, rot_y_power2, rot_z, rot_z_derivative1, rot_z_derivative1_power2, rot_z_power2, cosine00
## Model Structure
- Run-level models: Yes
- Subject-level models: Yes

The run-wise contrast estimates for each subject are averaged using a fixed-effects model.
## Contrasts of Interest
- **VCSPvVCSN**: ['1 * `trial_type.2` - 1 * `trial_type.4`']
- **ICSPvICSN**: ['1 * `trial_type.3` - 1 * `trial_type.5`']

## Figures

### Contrast Weights
![Contrast Weight](./imgs/ds003425_task-prelearning_contrast-matrix.svg)
The contrast maps represents the weights used to model brain activity.

### Design Matrixs
![Design Matrix](./imgs/ds003425_task-prelearning_design-matrix.svg)
The example design matrix illustrate the model used in the statistical analyses for this task (Note: if motion outliers are included, the number of these will vary between subjects). Each column represents a regressor (of interest or not of interested, based on the above), and each row represents a time point in the BOLD timeseries. The colored patterns show how different experimental conditions are modeled across the scan duration (HRF model).

### Variance Inflation Factor (VIF)
![VIF Distribution](./imgs/ds003425_task-prelearning_vif-boxplot.png)
The Variance Inflation Factor (VIF) boxplot quantifies multicollinearity between model regressors. Lower VIF values indicate more statistically independent regressors, which is desirable for reliable parameter estimation. VIFs were estimated using the design matrices -- nusiance regressors are excluded here for brevity.

### Voxelwise Model Variance Explained (r-squared)
Voxelwise R-squared values represent the proportion of variance explained by the model at each voxel in the brain. The R-squared images shown here are calculated across runs, subjects and/or sessions (dependent on data Fitlins nodes) for the study and task.

#### Voxelwise Average (Mean)
The **mean** R-squared image reflect the average of the R-squared values across all subjects and runs.In other words, the fluctuation in how much variability in the BOLD signal the model explains at a given voxel.
![R Square](./imgs/ds003425_task-prelearning_rsquare-mean.png)

#### Voxelwise Variance (Standard Deviation)
The **standard deviation** (or variance) image provides insights into the variability of model performance.In otherwords, across subjects, runs and/or sessions, how much variability there is in the models ability to explain the BOLD at a given voxel.
![R Square](./imgs/ds003425_task-prelearning_rsquare-std.png)

### Statistical Maps

#### VCSPvVCSN
![VCSPvVCSN Map](./imgs/ds003425_task-prelearning_contrast-VCSPvVCSN_map.png)

#### ICSPvICSN
![ICSPvICSN Map](./imgs/ds003425_task-prelearning_contrast-ICSPvICSN_map.png)
