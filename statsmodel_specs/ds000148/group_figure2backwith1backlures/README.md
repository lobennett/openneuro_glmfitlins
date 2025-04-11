# ds000148: figure2backwith1backlures Task Analysis Report
## Analysis Overview
Subject-level models were fit for 49 subjects performing the figure2backwith1backlures task.
HRF model type: spm. Data were smoothed at each run using a 5mm FWHM (default: isotropic additive smoothing)

*Note*: Due to an error/issue with confounds timerseries files, fmriprep computed nuisance regressors were not used and a default fitlins drift model was estimate. This will be investigated and rerun at a later date.

### Regressors of Interest
trial_type.distractorcorrectrejection, trial_type.distractorfalsealarm, trial_type.lurecorrectrejection, trial_type.targethit, trial_type.targetmiss, intercept
### Nuisance Regressors
drift_1, drift_2, drift_3, drift_4, drift_5, drift_6, drift_7, drift_8, drift_9
## Model Structure
- Run-level models: Yes
- Subject-level models: Yes

The run-wise contrast estimates for each subject are averaged using a fixed-effects model.
## Contrasts of Interest
- **distractcorr**: ['1 * `trial_type.distractorcorrectrejection`']
- **lurecorr**: ['1 * `trial_type.lurecorrectrejection`']
- **targethit**: ['1 * `trial_type.targethit`']
- **hittargetvlure**: ['1 * `trial_type.targethit` - 1 * `trial_type.lurecorrectrejection`']

## Figures

### Contrast Weights
![Contrast Weight](./imgs/ds000148_task-figure2backwith1backlures_contrast-matrix.svg)

The contrast maps represents the weights used to model brain activity.

### Design Matrixs
![Design Matrix](./imgs/ds000148_task-figure2backwith1backlures_design-matrix.svg)

The example design matrix illustrate the model used in the statistical analyses for this task (Note: if motion outliers are included, the number of these will vary between subjects). Each column represents a regressor (of interest or not of interested, based on the above), and each row represents a time point in the BOLD timeseries. The colored patterns show how different experimental conditions are modeled across the scan duration (HRF model).

### Variance Inflation Factor (VIF)
![VIF Distribution](./imgs/ds000148_task-figure2backwith1backlures_vif-boxplot.png)

The Variance Inflation Factor (VIF) boxplot quantifies multicollinearity between model regressors. Lower VIF values indicate more statistically independent regressors, which is desirable for reliable parameter estimation. VIFs were estimated using the design matrices -- nusiance regressors are excluded here for brevity.

### Voxelwise Model Variance Explained (r-squared)
Voxelwise R-squared values represent the proportion of variance explained by the model at each voxel in the brain. The R-squared images shown here are calculated across runs, subjects and/or sessions (dependent on data Fitlins nodes) for the study and task.

#### Voxelwise Average (Mean)
The **mean** R-squared image reflect the average of the R-squared values across all subjects and runs.In other words, the fluctuation in how much variability in the BOLD signal the model explains at a given voxel.
![R Square](./imgs/ds000148_task-figure2backwith1backlures_rsquare-mean.png)

#### Voxelwise Variance (Standard Deviation)
The **standard deviation** (or variance) image provides insights into the variability of model performance.In otherwords, across subjects, runs and/or sessions, how much variability there is in the models ability to explain the BOLD at a given voxel.
![R Square](./imgs/ds000148_task-figure2backwith1backlures_rsquare-std.png)

### Statistical Maps

#### distractcorr
![distractcorr Map](./imgs/ds000148_task-figure2backwith1backlures_contrast-distractcorr_map.png)

#### lurecorr
![lurecorr Map](./imgs/ds000148_task-figure2backwith1backlures_contrast-lurecorr_map.png)

#### targethit
![targethit Map](./imgs/ds000148_task-figure2backwith1backlures_contrast-targethit_map.png)

#### hittargetvlure
![hittargetvlure Map](./imgs/ds000148_task-figure2backwith1backlures_contrast-hittargetvlure_map.png)
