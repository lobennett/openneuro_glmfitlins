# ds000108: Emotionregulation Task Analysis Report
## Analysis Overview
Subject-level models were fit for 30 subjects performing the Emotionregulation task.
HRF model type: spm. Data were smoothed at each run using a 5mm FWHM (default: isotropic additive smoothing)
### Regressors of Interest
trial_type.Look_Neg_Ant, trial_type.Look_Neg_Cue, trial_type.Look_Neg_Rating, trial_type.Look_Neg_Stim, trial_type.Look_Neutral_Ant, trial_type.Look_Neutral_Cue, trial_type.Look_Neutral_Rating, trial_type.Look_Neutral_Stim, trial_type.Reapp_Neg_Ant, trial_type.Reapp_Neg_Cue, trial_type.Reapp_Neg_Rating, trial_type.Reapp_Neg_Stim, intercept
### Nuisance Regressors
trans_x, trans_x_derivative1, trans_x_derivative1_power2, trans_x_power2, trans_y, trans_y_derivative1, trans_y_derivative1_power2, trans_y_power2, trans_z, trans_z_derivative1, trans_z_derivative1_power2, trans_z_power2, rot_x, rot_x_derivative1, rot_x_derivative1_power2, rot_x_power2, rot_y, rot_y_derivative1, rot_y_derivative1_power2, rot_y_power2, rot_z, rot_z_derivative1, rot_z_derivative1_power2, rot_z_power2, cosine00, cosine01, cosine02, cosine03
## Model Structure
- Run-level models: Yes
- Subject-level models: Yes

The run-wise contrast estimates for each subject are averaged using a fixed-effects model.
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
![Contrast Weight](./imgs/ds000108_task-Emotionregulation_contrast-matrix.svg)

The contrast maps represents the weights used to model brain activity.

### Design Matrix
![Design Matrix](./imgs/ds000108_task-Emotionregulation_design-matrix.svg)

The example design matrix illustrates the model used in the statistical analyses for this task (Note: if motion outliers are included, the number of these will vary between subjects). Each column represents a regressor (of interest or not of interest, based on the above), and each row represents a time point in the BOLD timeseries. The colored patterns show how different experimental conditions are modeled across the scan duration (HRF model).

### Variance Inflation Factor (VIF)
![VIF Distribution](./imgs/ds000108_task-Emotionregulation_vif-boxplot.png)

The above includes 1) regressor and 2) contrast VIF estimates. The VIF boxplot quantifies multicollinearity between model regressors and how they impact contrasts (for more on contrasts VIFs, see [Dr. Mumford's repo](https://github.com/jmumford/vif_contrasts)). Lower VIF values indicate more statistically independent regressors, which is desirable for reliable parameter estimation. VIFs were estimated using the first-level model design matrices -- nusiance regressors are excluded here for brevity.

### Voxelwise Model Variance Explained (r-squared)
Voxelwise R-squared values represent the proportion of variance explained by the model at each voxel in the brain. The R-squared images shown here are calculated across runs, subjects and/or sessions (dependent on data Fitlins nodes) for the study and task.

#### Voxelwise Average (Mean)
The **mean** R-squared image reflect the average of the R-squared values across all subjects and runs.In other words, the fluctuation in how much variability in the BOLD signal the model explains at a given voxel.
![R Square](./imgs/ds000108_task-Emotionregulation_rsquare-mean.png)

#### Voxelwise Variance (Standard Deviation)
The **standard deviation** (or variance) image provides insights into the variability of model performance.In otherwords, across subjects, runs and/or sessions, how much variability there is in the models ability to explain the BOLD at a given voxel.

#### Flagged Subjects
The quality assessment pipeline evaluates volumetric data across multiple dimensions to identify problematic datasets. Subjects are flagged using: 

  - Dice Estimate: Similarity coefficient between subject r-squared maps and Target Space MNI152 mask falls below .85 
  - Voxels Outside of Mask: Percentage of voxels outside of the target brain mask is greater than the .10% (liberal threshold due to liberal brain masks in fMRIPrep BOLD) 

The subjects flagged for Emotionregulation are:
sub01_run1, sub01_run2, sub01_run3, sub01_run4, sub01_run5, sub01_run6, sub02_run1, sub02_run2, sub02_run3, sub02_run4, sub02_run5, sub02_run6, sub03_run1, sub03_run2, sub03_run3, sub03_run4, sub03_run5, sub03_run6, sub04_run1, sub04_run3, sub04_run5, sub04_run6, sub05_run1, sub05_run2, sub05_run3, sub05_run4, sub05_run5, sub05_run6, sub06_run1, sub06_run2, sub06_run3, sub06_run4, sub06_run5, sub06_run6, sub07_run1, sub07_run2, sub07_run3, sub07_run4, sub07_run5, sub07_run6, sub08_run1, sub08_run2, sub08_run3, sub08_run4, sub08_run5, sub08_run6, sub09_run1, sub09_run2, sub09_run3, sub09_run4, sub09_run5, sub09_run6, sub10_run1, sub10_run2, sub10_run3, sub10_run4, sub10_run5, sub10_run6, sub11_run1, sub11_run2, sub11_run3, sub11_run4, sub11_run5, sub11_run6, sub12_run1, sub12_run2, sub12_run3, sub12_run4, sub12_run5, sub12_run6, sub13_run1, sub13_run2, sub13_run3, sub13_run4, sub13_run5, sub13_run6, sub14_run1, sub14_run2, sub14_run3, sub14_run4, sub14_run5, sub14_run6, sub15_run1, sub15_run2, sub15_run3, sub15_run4, sub15_run5, sub15_run6, sub16_run1, sub16_run2, sub16_run3, sub16_run4, sub16_run5, sub16_run6, sub17_run1, sub17_run2, sub17_run3, sub17_run4, sub17_run5, sub17_run6, sub18_run1, sub18_run2, sub18_run3, sub18_run4, sub18_run5, sub18_run6, sub19_run1, sub19_run2, sub19_run3, sub19_run4, sub19_run5, sub19_run6, sub20_run1, sub20_run2, sub20_run3, sub20_run4, sub20_run5, sub20_run6, sub21_run1, sub21_run4, sub21_run5, sub21_run6, sub22_run1, sub22_run2, sub22_run3, sub22_run4, sub22_run5, sub22_run6, sub23_run1, sub23_run2, sub23_run3, sub23_run5, sub23_run6, sub25_run1, sub25_run2, sub25_run3, sub25_run4, sub25_run5, sub25_run6, sub26_run1, sub26_run2, sub26_run3, sub26_run4, sub26_run5, sub27_run1, sub27_run2, sub27_run3, sub27_run4, sub27_run5, sub27_run6, sub30_run1, sub30_run2, sub30_run3, sub30_run4, sub30_run5, sub30_run6, sub31_run1, sub31_run2, sub31_run3, sub31_run4, sub31_run5, sub31_run6, sub32_run1, sub32_run2, sub32_run3, sub32_run4, sub32_run5, sub32_run6, sub33_run1, sub33_run2, sub33_run3, sub33_run4, sub33_run5, sub33_run6

The distribution for subjects and runs in Emotionregulation are below. 

![Dice](./imgs/ds000108_task-Emotionregulation_hist-dicesimilarity.png)
![Voxels Out](./imgs/ds000108_task-Emotionregulation_hist-voxoutmask.png)

### Statistical Maps

#### StimReappNegvLookNeg
![StimReappNegvLookNeg Map](./imgs/ds000108_task-Emotionregulation_contrast-StimReappNegvLookNeg_map.png)

#### StimLookNegvNeutral
![StimLookNegvNeutral Map](./imgs/ds000108_task-Emotionregulation_contrast-StimLookNegvNeutral_map.png)

#### StimReappvLookNegNeut
![StimReappvLookNegNeut Map](./imgs/ds000108_task-Emotionregulation_contrast-StimReappvLookNegNeut_map.png)

#### StimReappNeg
![StimReappNeg Map](./imgs/ds000108_task-Emotionregulation_contrast-StimReappNeg_map.png)

#### StimLookNeg
![StimLookNeg Map](./imgs/ds000108_task-Emotionregulation_contrast-StimLookNeg_map.png)

#### StimLookNeutral
![StimLookNeutral Map](./imgs/ds000108_task-Emotionregulation_contrast-StimLookNeutral_map.png)

#### StimPhase
![StimPhase Map](./imgs/ds000108_task-Emotionregulation_contrast-StimPhase_map.png)

#### AntPhase
![AntPhase Map](./imgs/ds000108_task-Emotionregulation_contrast-AntPhase_map.png)

#### RatePhase
![RatePhase Map](./imgs/ds000108_task-Emotionregulation_contrast-RatePhase_map.png)
