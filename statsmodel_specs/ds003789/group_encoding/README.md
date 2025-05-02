# ds003789: encoding Task Analysis Report

The size of the Fitlins Derivatives for ds003789 encoding is 18G with 11360 files.

## Statistical Analysis Boilerplate

### First-level Analysis
FitLins was employed to estimate task-related BOLD activity in the encoding task for 32 subjects. In this instance, FitLins used the Nilearn estimator in its statistical modeling of the BOLD data. For each participant, 6 regressors of interest (see list below) were convolved with a spm hemodynamic response function in Nilearn. The design matrix incorporated both regressors of interest and 27 additional components, including a drift cosine basis set and nuisance regressors to account for sources of noise in the BOLD signal. Following Nilearn's *FirstLevelModel* default procedure, each voxel's timeseries was mean-scaled by each voxel's mean BOLD signal. Data were smoothed at each run using a 5mm full-width at half maximum smoothing kernal (default: isotropic additive smoothing). From the resulting model, 5 distinct contrast estimates were computed (see list below).

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
trial_type.fixation, trial_type.word_list1, trial_type.word_list2, trial_type.word_list3, rt_reg.rt, intercept
### Nuisance Regressors
trans_x, trans_x_derivative1, trans_x_derivative1_power2, trans_x_power2, trans_y, trans_y_derivative1, trans_y_derivative1_power2, trans_y_power2, trans_z, trans_z_derivative1, trans_z_derivative1_power2, trans_z_power2, rot_x, rot_x_derivative1, rot_x_derivative1_power2, rot_x_power2, rot_y, rot_y_derivative1, rot_y_derivative1_power2, rot_y_power2, rot_z, rot_z_derivative1, rot_z_derivative1_power2, rot_z_power2, cosine00, cosine01, cosine02
## Model Structure
- Run-level models: Yes
- Subject-level models: Yes

## Contrasts of Interest
- **FirstvLast**: 1*`trial_type.word_list1` - 1*`trial_type.word_list2`
- **WordList1**: 1*`trial_type.word_list1`
- **WordList2**: 1*`trial_type.word_list2`
- **WordList3**: 1*`trial_type.word_list3`
- **rt**: 1*`rt_reg.rt`

## Figures

### Contrast Weights
![Contrast Weight](./imgs/ds003789_task-encoding_contrast-matrix.svg)

The contrast maps represents the weights used to model brain activity.

### Design Matrix
![Design Matrix](./imgs/ds003789_task-encoding_design-matrix.svg)

The example design matrix illustrates the model used in the statistical analyses for this task (Note: if motion outliers are included, the number of these will vary between subjects). Each column represents a regressor (of interest or not of interest, based on the above), and each row represents a time point in the BOLD timeseries. The colored patterns show how different experimental conditions are modeled across the scan duration (HRF model).

### Variance Inflation Factor (VIF)
![VIF Distribution](./imgs/ds003789_task-encoding_vif-boxplot.png)

The above includes 1) regressor and 2) contrast VIF estimates. The VIF boxplot quantifies multicollinearity between model regressors and how they impact contrasts (for more on contrasts VIFs, see [Dr. Mumford's repo](https://github.com/jmumford/vif_contrasts)). Lower VIF values indicate more statistically independent regressors, which is desirable for reliable parameter estimation. VIFs were estimated using the first-level model design matrices -- nusiance regressors are excluded here for brevity.

### Voxelwise Model Variance Explained (r-squared)
Voxelwise R-squared values represent the proportion of variance explained by the model at each voxel in the brain. The R-squared images shown here are calculated across runs, subjects and/or sessions (dependent on data Fitlins nodes) for the study and task.

#### Voxelwise Average (Mean)
The **mean** R-squared image reflect the average of the R-squared values across all subjects and runs.In other words, the fluctuation in how much variability in the BOLD signal the model explains at a given voxel.
![R Square](./imgs/ds003789_task-encoding_rsquare-mean.png)

#### Voxelwise Variance (Standard Deviation)
The **standard deviation** (or variance) image provides insights into the variability of model performance.In otherwords, across subjects, runs and/or sessions, how much variability there is in the models ability to explain the BOLD at a given voxel.

#### Flagged Subjects
The quality assessment pipeline evaluates volumetric data across multiple dimensions to identify problematic datasets. Subjects are flagged using: 

  - Dice Estimate: Similarity coefficient between subject r-squared maps and Target Space MNI152 mask falls below .85 
  - Voxels Outside of Mask: Percentage of voxels outside of the target brain mask is greater than the .10% (liberal threshold due to liberal brain masks in fMRIPrep BOLD) 

The subjects flagged for encoding are:
sub-5407_run-01, sub-5408_run-03, sub-5411_run-01, sub-5411_run-02, sub-5411_run-03, sub-5411_run-04, sub-5411_run-05, sub-5411_run-06, sub-5411_run-07, sub-5411_run-08, sub-5411_run-09, sub-5415_run-01, sub-5415_run-02, sub-5415_run-03, sub-5415_run-04, sub-5415_run-05, sub-5415_run-06, sub-5415_run-07, sub-5415_run-08, sub-5415_run-09, sub-5418_run-02, sub-5418_run-03, sub-5418_run-05, sub-5425_run-01, sub-5425_run-02, sub-5425_run-03, sub-5425_run-04, sub-5425_run-06, sub-5425_run-07, sub-5425_run-09, sub-5426_run-02, sub-5426_run-05, sub-5426_run-07, sub-5433_run-09, sub-5437_run-01, sub-5437_run-02, sub-5437_run-03, sub-5437_run-04, sub-5437_run-05, sub-5437_run-06, sub-5437_run-08, sub-5437_run-09, sub-5439_run-06, sub-5439_run-07, sub-5439_run-08

The distribution for subjects and runs in encoding are below. 

![Dice](./imgs/ds003789_task-encoding_hist-dicesimilarity.png)
![Voxels Out](./imgs/ds003789_task-encoding_hist-voxoutmask.png)

### Statistical Maps

#### FirstvLast
![FirstvLast Map](./imgs/ds003789_task-encoding_contrast-FirstvLast_map.png)

#### WordList1
![WordList1 Map](./imgs/ds003789_task-encoding_contrast-WordList1_map.png)

#### WordList2
![WordList2 Map](./imgs/ds003789_task-encoding_contrast-WordList2_map.png)

#### WordList3
![WordList3 Map](./imgs/ds003789_task-encoding_contrast-WordList3_map.png)

#### rt
![rt Map](./imgs/ds003789_task-encoding_contrast-rt_map.png)
