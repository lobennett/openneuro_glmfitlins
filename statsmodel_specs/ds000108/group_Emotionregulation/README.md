# ds000108: Emotionregulation Task Analysis Report

The size of the Fitlins Derivatives for ds000108 Emotionregulation is 17G with 12476 files.

## Statistical Analysis Boilerplate

### First-level Analysis
FitLins was employed to estimate task-related BOLD activity in the Emotionregulation task for 30 subjects. In this instance, FitLins used the Nilearn estimator in its statistical modeling of the BOLD data. For each participant, 12 regressors of interest (out of total 13 regressors; see list below) were convolved with a spm hemodynamic response function in Nilearn. The design matrix incorporated both regressors of interest and 28 additional components, including a drift cosine basis set and nuisance regressors to account for sources of noise in the BOLD signal. Following Nilearn's *FirstLevelModel* default procedure, each voxel's timeseries was mean-scaled by each voxel's mean of the timeseries. Data were smoothed at each run using a 5mm full-width at half maximum smoothing kernal (default: isotropic additive smoothing). From the resulting model, 9 distinct contrast estimates were computed (see list below).

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
trial_type.Look_Neg_Ant, trial_type.Look_Neg_Cue, trial_type.Look_Neg_Rating, trial_type.Look_Neg_Stim, trial_type.Look_Neutral_Ant, trial_type.Look_Neutral_Cue, trial_type.Look_Neutral_Rating, trial_type.Look_Neutral_Stim, trial_type.Reapp_Neg_Ant, trial_type.Reapp_Neg_Cue, trial_type.Reapp_Neg_Rating, trial_type.Reapp_Neg_Stim, intercept
#### Convolved Regressors
trial_type.Look_Neg_Ant, trial_type.Look_Neg_Cue, trial_type.Look_Neg_Rating, trial_type.Look_Neg_Stim, trial_type.Look_Neutral_Ant, trial_type.Look_Neutral_Cue, trial_type.Look_Neutral_Rating, trial_type.Look_Neutral_Stim, trial_type.Reapp_Neg_Ant, trial_type.Reapp_Neg_Cue, trial_type.Reapp_Neg_Rating, trial_type.Reapp_Neg_Stim
### Nuisance Regressors
trans_x, trans_x_derivative1, trans_x_derivative1_power2, trans_x_power2, trans_y, trans_y_derivative1, trans_y_derivative1_power2, trans_y_power2, trans_z, trans_z_derivative1, trans_z_derivative1_power2, trans_z_power2, rot_x, rot_x_derivative1, rot_x_derivative1_power2, rot_x_power2, rot_y, rot_y_derivative1, rot_y_derivative1_power2, rot_y_power2, rot_z, rot_z_derivative1, rot_z_derivative1_power2, rot_z_power2, cosine00, cosine01, cosine02, cosine03
## Model Structure
- Run-level models: Yes
- Subject-level models: Yes

## Contrasts of Interest
- **StimReappNegvLookNeg**: 1*`trial_type.Reapp_Neg_Stim` - 1*`trial_type.Look_Neg_Stim`
- **StimLookNegvNeutral**: 1*`trial_type.Look_Neg_Stim` - 1*`trial_type.Look_Neutral_Stim`
- **StimReappvLookNegNeut**: 1*`trial_type.Reapp_Neg_Stim` - 0.5*`trial_type.Look_Neg_Stim` - 0.5*`trial_type.Look_Neutral_Stim`
- **StimReappNeg**: 1*`trial_type.Reapp_Neg_Stim`
- **StimLookNeg**: 1*`trial_type.Look_Neg_Stim`
- **StimLookNeutral**: 1*`trial_type.Look_Neutral_Stim`
- **StimPhase**: 0.33*`trial_type.Look_Neg_Stim` + 0.33*`trial_type.Reapp_Neg_Stim` + 0.33*`trial_type.Look_Neutral_Stim`
- **AntPhase**: 0.33*`trial_type.Look_Neg_Ant` + 0.33*`trial_type.Reapp_Neg_Ant` + 0.33*`trial_type.Look_Neutral_Ant`
- **RatePhase**: 0.33*`trial_type.Look_Neg_Rating` + 0.33*`trial_type.Reapp_Neg_Rating` + 0.33*`trial_type.Look_Neutral_Rating`

## Figures

### Contrast Weights
![Contrast Weight](./files/ds000108_task-Emotionregulation_contrast-matrix.svg)

The contrast maps represents the weights used to model brain activity.

### Design Matrix
![Design Matrix](./files/ds000108_task-Emotionregulation_design-matrix.svg)

The example design matrix illustrates the model used in the statistical analyses for this task (Note: if motion outliers are included, the number of these will vary between subjects). Each column represents a regressor (of interest or not of interest, based on the above), and each row represents a time point in the BOLD timeseries. The colored patterns show how different experimental conditions are modeled across the scan duration (HRF model).

### Variance Inflation Factor (VIF)
![VIF Distribution](./files/ds000108_task-Emotionregulation_vif-boxplot.png)

The above includes 1) regressor and 2) contrast VIF estimates. The VIF boxplot quantifies multicollinearity between model regressors and how they impact contrasts (for more on contrasts VIFs, see [Dr. Mumford's repo](https://github.com/jmumford/vif_contrasts)). Lower VIF values indicate more statistically independent regressors, which is desirable for reliable parameter estimation. VIFs were estimated using the first-level model design matrices -- nusiance regressors are excluded here for brevity.

### Voxelwise Model Variance Explained (r-squared)
Voxelwise R-squared values represent the proportion of variance explained by the model at each voxel in the brain. The R-squared images shown here are calculated across runs, subjects and/or sessions (dependent on data Fitlins nodes) for the study and task.

#### Voxelwise Average (Mean)
The **mean** R-squared image reflect the average of the R-squared values across all subjects and runs.In other words, the fluctuation in how much variability in the BOLD signal the model explains at a given voxel.
![R Square](./files/ds000108_task-Emotionregulation_rsquare-mean.png)

#### Voxelwise Variance (Standard Deviation)
The **standard deviation** (or variance) image provides insights into the variability of model performance.In otherwords, across subjects, runs and/or sessions, how much variability there is in the models ability to explain the BOLD at a given voxel.

#### Flagged Subjects
The quality assessment pipeline evaluates volumetric data across multiple dimensions to identify problematic datasets. Subjects are flagged using: 

  - Dice Estimate: Similarity coefficient between subject r-squared maps and Target Space MNI152 mask falls below .80 (captures dropout and excess non-brain voxels) 
  - Voxels Outside of Mask: Percentage of voxels outside of the target brain mask is greater than the .10% (liberal threshold due to liberal brain masks in fMRIPrep BOLD, captures mostly non-brain voxels) 

The subjects flagged for Emotionregulation are:
sub-01_run-1, sub-02_run-2, sub-02_run-4, sub-02_run-5, sub-02_run-6, sub-03_run-1, sub-03_run-2, sub-03_run-3, sub-03_run-4, sub-03_run-6, sub-06_run-4, sub-06_run-5, sub-06_run-6, sub-07_run-5, sub-08_run-1, sub-08_run-2, sub-08_run-3, sub-08_run-4, sub-08_run-5, sub-08_run-6, sub-10_run-6, sub-11_run-1, sub-11_run-2, sub-11_run-5, sub-11_run-6, sub-12_run-1, sub-12_run-2, sub-12_run-3, sub-12_run-4, sub-12_run-5, sub-12_run-6, sub-13_run-1, sub-13_run-4, sub-13_run-5, sub-13_run-6, sub-15_run-2, sub-15_run-3, sub-16_run-1, sub-16_run-2, sub-16_run-3, sub-16_run-4, sub-16_run-5, sub-16_run-6, sub-17_run-2, sub-17_run-3, sub-17_run-4, sub-17_run-5, sub-19_run-1, sub-19_run-4, sub-19_run-5, sub-20_run-1, sub-20_run-2, sub-20_run-3, sub-20_run-4, sub-20_run-5, sub-20_run-6, sub-21_run-5, sub-22_run-1, sub-22_run-2, sub-22_run-3, sub-22_run-4, sub-22_run-5, sub-22_run-6, sub-23_run-1, sub-23_run-2, sub-23_run-3, sub-23_run-5, sub-25_run-3, sub-25_run-4, sub-25_run-5, sub-25_run-6, sub-26_run-2, sub-31_run-1, sub-31_run-2, sub-31_run-3, sub-31_run-4, sub-31_run-5, sub-31_run-6

The distribution for subjects and runs in Emotionregulation are below. 

![Dice](./files/ds000108_task-Emotionregulation_hist-dicesimilarity.png)
![Voxels Out](./files/ds000108_task-Emotionregulation_hist-voxoutmask.png)

### Statistical Maps

#### StimReappNegvLookNeg
![StimReappNegvLookNeg Map](./files/ds000108_task-Emotionregulation_contrast-StimReappNegvLookNeg_map.png)

#### StimLookNegvNeutral
![StimLookNegvNeutral Map](./files/ds000108_task-Emotionregulation_contrast-StimLookNegvNeutral_map.png)

#### StimReappvLookNegNeut
![StimReappvLookNegNeut Map](./files/ds000108_task-Emotionregulation_contrast-StimReappvLookNegNeut_map.png)

#### StimReappNeg
![StimReappNeg Map](./files/ds000108_task-Emotionregulation_contrast-StimReappNeg_map.png)

#### StimLookNeg
![StimLookNeg Map](./files/ds000108_task-Emotionregulation_contrast-StimLookNeg_map.png)

#### StimLookNeutral
![StimLookNeutral Map](./files/ds000108_task-Emotionregulation_contrast-StimLookNeutral_map.png)

#### StimPhase
![StimPhase Map](./files/ds000108_task-Emotionregulation_contrast-StimPhase_map.png)

#### AntPhase
![AntPhase Map](./files/ds000108_task-Emotionregulation_contrast-AntPhase_map.png)

#### RatePhase
![RatePhase Map](./files/ds000108_task-Emotionregulation_contrast-RatePhase_map.png)
