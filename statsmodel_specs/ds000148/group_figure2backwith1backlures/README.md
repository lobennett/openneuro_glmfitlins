# ds000148: figure2backwith1backlures Task Analysis Report
## Analysis Overview
Subject-level models were fit for 49 subjects performing the figure2backwith1backlures task.
HRF model type: spm. Data were smoothed at each run using a 5mm FWHM (default: isotropic additive smoothing)
### Regressors of Interest
trial_type.distractorcorrectrejection, trial_type.distractorfalsealarm, trial_type.lurecorrectrejection, trial_type.targethit, trial_type.targetmiss, intercept
### Nuisance Regressors
drift_1, drift_2, drift_3, drift_4, drift_5, drift_6, drift_7, drift_8, drift_9
## Model Structure
- Run-level models: Yes
- Subject-level models: Yes

The run-wise contrast estimates for each subject are averaged using a fixed-effects model.
## Contrasts of Interest
- **distractcorr**: 1*`trial_type.distractorcorrectrejection`
- **lurecorr**: 1*`trial_type.lurecorrectrejection`
- **targethit**: 1*`trial_type.targethit`
- **hittargetvlure**: 1*`trial_type.targethit` - 1*`trial_type.lurecorrectrejection`

## Figures

### Contrast Weights
![Contrast Weight](./imgs/ds000148_task-figure2backwith1backlures_contrast-matrix.svg)

The contrast maps represents the weights used to model brain activity.

### Design Matrix
![Design Matrix](./imgs/ds000148_task-figure2backwith1backlures_design-matrix.svg)

The example design matrix illustrates the model used in the statistical analyses for this task (Note: if motion outliers are included, the number of these will vary between subjects). Each column represents a regressor (of interest or not of interest, based on the above), and each row represents a time point in the BOLD timeseries. The colored patterns show how different experimental conditions are modeled across the scan duration (HRF model).

### Variance Inflation Factor (VIF)
![VIF Distribution](./imgs/ds000148_task-figure2backwith1backlures_vif-boxplot.png)

The above includes 1) regressor and 2) contrast VIF estimates. The VIF boxplot quantifies multicollinearity between model regressors and how they impact contrasts (for more on contrasts VIFs, see [Dr. Mumford's repo](https://github.com/jmumford/vif_contrasts)). Lower VIF values indicate more statistically independent regressors, which is desirable for reliable parameter estimation. VIFs were estimated using the first-level model design matrices -- nusiance regressors are excluded here for brevity.

### Voxelwise Model Variance Explained (r-squared)
Voxelwise R-squared values represent the proportion of variance explained by the model at each voxel in the brain. The R-squared images shown here are calculated across runs, subjects and/or sessions (dependent on data Fitlins nodes) for the study and task.

#### Voxelwise Average (Mean)
The **mean** R-squared image reflect the average of the R-squared values across all subjects and runs.In other words, the fluctuation in how much variability in the BOLD signal the model explains at a given voxel.
![R Square](./imgs/ds000148_task-figure2backwith1backlures_rsquare-mean.png)

#### Voxelwise Variance (Standard Deviation)
The **standard deviation** (or variance) image provides insights into the variability of model performance.In otherwords, across subjects, runs and/or sessions, how much variability there is in the models ability to explain the BOLD at a given voxel.

#### Flagged Subjects
The quality assessment pipeline evaluates volumetric data across multiple dimensions to identify problematic datasets. Subjects are flagged using: 

  - Dice Estimate: Similarity coefficient between subject r-squared maps and Target Space MNI152 mask falls below .85 
  - Voxels Outside of Mask: Percentage of voxels outside of the target brain mask is greater than the .10% (liberal threshold due to liberal brain masks in fMRIPrep BOLD) 

The subjects flagged for figure2backwith1backlures are:
sub01_run01, sub01_run02, sub04_run02, sub05_run01, sub05_run02, sub06_run02, sub10_run01, sub13_run01, sub14_run02, sub14_run03, sub15_run02, sub16_run01, sub16_run02, sub16_run03, sub17_run01, sub17_run02, sub18_run01, sub18_run02, sub18_run03, sub19_run01, sub21_run01, sub21_run02, sub21_run03, sub22_run01, sub22_run02, sub23_run01, sub24_run02, sub25_run01, sub25_run02, sub25_run03, sub29_run03, sub31_run01, sub31_run03, sub32_run01, sub32_run03, sub33_run01, sub33_run02, sub33_run03, sub34_run01, sub34_run02, sub34_run03, sub35_run03, sub36_run02, sub38_run02, sub39_run01, sub39_run02, sub39_run03, sub41_run01, sub41_run02, sub41_run03, sub42_run03, sub43_run01, sub43_run02, sub44_run02, sub45_run01, sub45_run02, sub46_run02, sub46_run03, sub47_run01, sub47_run03, sub48_run01

The distribution for subjects and runs in figure2backwith1backlures are below. 

![Dice](./imgs/ds000148_task-figure2backwith1backlures_hist-dicesimilarity.png)
![Voxels Out](./imgs/ds000148_task-figure2backwith1backlures_hist-voxoutmask.png)

### Statistical Maps

#### distractcorr
![distractcorr Map](./imgs/ds000148_task-figure2backwith1backlures_contrast-distractcorr_map.png)

#### lurecorr
![lurecorr Map](./imgs/ds000148_task-figure2backwith1backlures_contrast-lurecorr_map.png)

#### targethit
![targethit Map](./imgs/ds000148_task-figure2backwith1backlures_contrast-targethit_map.png)

#### hittargetvlure
![hittargetvlure Map](./imgs/ds000148_task-figure2backwith1backlures_contrast-hittargetvlure_map.png)
