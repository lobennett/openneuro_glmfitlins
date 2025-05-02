# ds002033: ChangeDetection Task Analysis Report

The size of the Fitlins Derivatives for ds002033 ChangeDetection is 9.1G with 5786 files.

## Statistical Analysis Boilerplate

### First-level Analysis
FitLins was employed to estimate task-related BOLD activity in the ChangeDetection task for 40 subjects. In this instance, FitLins used the Nilearn estimator in its statistical modeling of the BOLD data. For each participant, 8 regressors of interest (see list below) were convolved with a spm hemodynamic response function in Nilearn. The design matrix incorporated both regressors of interest and 28 additional components, including a drift cosine basis set and nuisance regressors to account for sources of noise in the BOLD signal. Following Nilearn's *FirstLevelModel* default procedure, each voxel's timeseries was mean-scaled by each voxel's mean BOLD signal. Data were smoothed at each run using a 5mm full-width at half maximum smoothing kernal (default: isotropic additive smoothing). From the resulting model, 4 distinct contrast estimates were computed (see list below).

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
trial_type.digits, trial_type.hash__red, trial_type.letters, trial_type.mirrored_digits, trial_type.mirrored_letters, trial_type.scrambled_digits, trial_type.scrambled_letters, intercept
### Nuisance Regressors
trans_x, trans_x_derivative1, trans_x_derivative1_power2, trans_x_power2, trans_y, trans_y_derivative1, trans_y_derivative1_power2, trans_y_power2, trans_z, trans_z_derivative1, trans_z_derivative1_power2, trans_z_power2, rot_x, rot_x_derivative1, rot_x_derivative1_power2, rot_x_power2, rot_y, rot_y_derivative1, rot_y_derivative1_power2, rot_y_power2, rot_z, rot_z_derivative1, rot_z_derivative1_power2, rot_z_power2, cosine00, cosine01, cosine02, cosine03
## Model Structure
- Run-level models: Yes
- Subject-level models: Yes

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
sub-01_run-01, sub-01_run-02, sub-01_run-03, sub-01_run-04, sub-02_run-01, sub-02_run-02, sub-02_run-04, sub-03_run-01, sub-03_run-02, sub-03_run-03, sub-03_run-04, sub-04_run-01, sub-04_run-02, sub-04_run-03, sub-04_run-04, sub-07_run-01, sub-07_run-02, sub-07_run-03, sub-07_run-04, sub-08_run-01, sub-08_run-02, sub-08_run-03, sub-08_run-04, sub-09_run-01, sub-09_run-02, sub-09_run-03, sub-09_run-04, sub-10_run-01, sub-10_run-02, sub-10_run-03, sub-10_run-04, sub-11_run-01, sub-11_run-02, sub-11_run-03, sub-11_run-04, sub-13_run-01, sub-13_run-02, sub-13_run-03, sub-13_run-04, sub-14_run-01, sub-14_run-02, sub-14_run-03, sub-14_run-04, sub-15_run-01, sub-15_run-02, sub-15_run-03, sub-15_run-04, sub-16_run-01, sub-16_run-02, sub-16_run-03, sub-16_run-04, sub-17_run-01, sub-17_run-02, sub-17_run-03, sub-17_run-04, sub-20_run-01, sub-20_run-02, sub-20_run-03, sub-20_run-04, sub-22_run-01, sub-22_run-02, sub-22_run-03, sub-22_run-04, sub-23_run-01, sub-23_run-02, sub-23_run-03, sub-23_run-04, sub-24_run-01, sub-24_run-02, sub-24_run-03, sub-24_run-04, sub-26_run-01, sub-26_run-02, sub-26_run-03, sub-26_run-04, sub-27_run-01, sub-27_run-02, sub-27_run-03, sub-27_run-04, sub-28_run-01, sub-28_run-02, sub-28_run-03, sub-28_run-04, sub-29_run-01, sub-29_run-02, sub-29_run-03, sub-29_run-04, sub-32_run-01, sub-32_run-02, sub-32_run-03, sub-32_run-04, sub-33_run-01, sub-33_run-02, sub-33_run-03, sub-33_run-04, sub-34_run-01, sub-34_run-02, sub-34_run-03, sub-34_run-04, sub-35_run-01, sub-35_run-02, sub-35_run-03, sub-35_run-04, sub-36_run-01, sub-36_run-02, sub-36_run-03, sub-36_run-04, sub-38_run-01, sub-38_run-02, sub-38_run-03, sub-38_run-04, sub-39_run-01, sub-39_run-02, sub-40_run-01, sub-40_run-02, sub-40_run-03, sub-40_run-04, sub-42_run-01, sub-42_run-02, sub-42_run-03, sub-42_run-04

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
