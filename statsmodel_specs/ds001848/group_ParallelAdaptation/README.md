# ds001848: ParallelAdaptation Task Analysis Report

The size of the Fitlins Derivatives for ds001848 ParallelAdaptation is 23G with 13478 files.

## Statistical Analysis Boilerplate

### First-level Analysis
FitLins was employed to estimate task-related BOLD activity in the ParallelAdaptation task for 52 subjects. In this instance, FitLins used the Nilearn estimator in its statistical modeling of the BOLD data. For each participant, 15 regressors of interest (see list below) were convolved with a spm hemodynamic response function in Nilearn. The design matrix incorporated both regressors of interest and 35 additional components, including a drift cosine basis set and nuisance regressors to account for sources of noise in the BOLD signal. Following Nilearn's *FirstLevelModel* default procedure, each voxel's timeseries was mean-scaled by each voxel's mean BOLD signal. Data were smoothed at each run using a 5mm full-width at half maximum smoothing kernal (default: isotropic additive smoothing). From the resulting model, 10 distinct contrast estimates were computed (see list below).

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
trial_type.catch_null0, trial_type.catch_physical_size1, trial_type.catch_physical_size4, trial_type.catch_quantity1, trial_type.catch_quantity4, trial_type.catch_symbolic1, trial_type.catch_symbolic4, trial_type.deviant_nonsymbolic1, trial_type.deviant_nonsymbolic4, trial_type.deviant_physical_size1, trial_type.deviant_physical_size4, trial_type.deviant_symbolic1, trial_type.deviant_symbolic4, trial_type.null_null0, intercept
### Nuisance Regressors
trans_x, trans_x_derivative1, trans_x_derivative1_power2, trans_x_power2, trans_y, trans_y_derivative1, trans_y_derivative1_power2, trans_y_power2, trans_z, trans_z_derivative1, trans_z_derivative1_power2, trans_z_power2, rot_x, rot_x_derivative1, rot_x_derivative1_power2, rot_x_power2, rot_y, rot_y_derivative1, rot_y_derivative1_power2, rot_y_power2, rot_z, rot_z_derivative1, rot_z_derivative1_power2, rot_z_power2, cosine00, cosine01, cosine02, cosine03, cosine04, cosine05, cosine06, cosine07, cosine08, cosine09, cosine10
## Model Structure
- Run-level models: Yes
- Subject-level models: Yes

## Contrasts of Interest
- **devnonsym**: 0.5*`trial_type.deviant_nonsymbolic4` + 0.5*`trial_type.deviant_nonsymbolic1`
- **devsym**: 0.5*`trial_type.deviant_symbolic4` + 0.5*`trial_type.deviant_symbolic1`
- **devphys**: 0.5*`trial_type.deviant_physical_size4` + 0.5*`trial_type.deviant_physical_size1`
- **devsym4vdevsym1**: 1*`trial_type.deviant_symbolic4` - 1*`trial_type.deviant_symbolic1`
- **devnonsym4vnondevsym1**: 1*`trial_type.deviant_nonsymbolic4` - 1*`trial_type.deviant_nonsymbolic1`
- **devphys4vdevphys1**: 1*`trial_type.deviant_physical_size4` - 1*`trial_type.deviant_physical_size1`
- **catchsym4vcatchsym1**: 1*`trial_type.catch_symbolic4` - 1*`trial_type.catch_symbolic1`
- **symnonsym4vphys4**: 0.5*`trial_type.deviant_symbolic4` + 0.5*`trial_type.deviant_nonsymbolic4` - 1*`trial_type.deviant_physical_size4`
- **symnonsym4vcatch4**: 0.5*`trial_type.deviant_symbolic4` + 0.5*`trial_type.deviant_nonsymbolic4` - 1*`trial_type.catch_symbolic4`
- **dist4v1**: 0.33*`trial_type.deviant_symbolic4` + 0.33*`trial_type.deviant_nonsymbolic4` + 0.33*`trial_type.deviant_physical_size4` - 0.33*`trial_type.deviant_symbolic1` - 0.33*`trial_type.deviant_nonsymbolic1` - 0.33*`trial_type.deviant_physical_size1`

## Figures

### Contrast Weights
![Contrast Weight](./imgs/ds001848_task-ParallelAdaptation_contrast-matrix.svg)

The contrast maps represents the weights used to model brain activity.

### Design Matrix
![Design Matrix](./imgs/ds001848_task-ParallelAdaptation_design-matrix.svg)

The example design matrix illustrates the model used in the statistical analyses for this task (Note: if motion outliers are included, the number of these will vary between subjects). Each column represents a regressor (of interest or not of interest, based on the above), and each row represents a time point in the BOLD timeseries. The colored patterns show how different experimental conditions are modeled across the scan duration (HRF model).

### Variance Inflation Factor (VIF)
![VIF Distribution](./imgs/ds001848_task-ParallelAdaptation_vif-boxplot.png)

The above includes 1) regressor and 2) contrast VIF estimates. The VIF boxplot quantifies multicollinearity between model regressors and how they impact contrasts (for more on contrasts VIFs, see [Dr. Mumford's repo](https://github.com/jmumford/vif_contrasts)). Lower VIF values indicate more statistically independent regressors, which is desirable for reliable parameter estimation. VIFs were estimated using the first-level model design matrices -- nusiance regressors are excluded here for brevity.

### Voxelwise Model Variance Explained (r-squared)
Voxelwise R-squared values represent the proportion of variance explained by the model at each voxel in the brain. The R-squared images shown here are calculated across runs, subjects and/or sessions (dependent on data Fitlins nodes) for the study and task.

#### Voxelwise Average (Mean)
The **mean** R-squared image reflect the average of the R-squared values across all subjects and runs.In other words, the fluctuation in how much variability in the BOLD signal the model explains at a given voxel.
![R Square](./imgs/ds001848_task-ParallelAdaptation_rsquare-mean.png)

#### Voxelwise Variance (Standard Deviation)
The **standard deviation** (or variance) image provides insights into the variability of model performance.In otherwords, across subjects, runs and/or sessions, how much variability there is in the models ability to explain the BOLD at a given voxel.

#### Flagged Subjects
The quality assessment pipeline evaluates volumetric data across multiple dimensions to identify problematic datasets. Subjects are flagged using: 

  - Dice Estimate: Similarity coefficient between subject r-squared maps and Target Space MNI152 mask falls below .85 
  - Voxels Outside of Mask: Percentage of voxels outside of the target brain mask is greater than the .10% (liberal threshold due to liberal brain masks in fMRIPrep BOLD) 

The subjects flagged for ParallelAdaptation are:
sub-01_run-01, sub-01_run-02, sub-01_run-03, sub-02_run-01, sub-02_run-02, sub-02_run-03, sub-03_run-01, sub-04_run-01, sub-04_run-02, sub-04_run-03, sub-05_run-01, sub-05_run-02, sub-05_run-03, sub-06_run-01, sub-06_run-02, sub-06_run-03, sub-07_run-01, sub-07_run-02, sub-07_run-03, sub-08_run-01, sub-08_run-02, sub-08_run-03, sub-09_run-01, sub-09_run-02, sub-09_run-03, sub-10_run-01, sub-10_run-02, sub-10_run-03, sub-11_run-01, sub-11_run-02, sub-11_run-03, sub-12_run-01, sub-12_run-02, sub-12_run-03, sub-13_run-01, sub-13_run-02, sub-13_run-03, sub-14_run-01, sub-14_run-02, sub-14_run-03, sub-15_run-01, sub-15_run-02, sub-15_run-03, sub-17_run-01, sub-17_run-02, sub-17_run-03, sub-18_run-01, sub-18_run-02, sub-18_run-03, sub-19_run-01, sub-19_run-02, sub-19_run-03, sub-20_run-01, sub-20_run-02, sub-20_run-03, sub-21_run-02, sub-21_run-03, sub-22_run-01, sub-22_run-02, sub-22_run-03, sub-23_run-01, sub-23_run-02, sub-23_run-03, sub-24_run-01, sub-24_run-02, sub-24_run-03, sub-25_run-01, sub-25_run-02, sub-25_run-03, sub-26_run-01, sub-26_run-02, sub-26_run-03, sub-27_run-02, sub-27_run-03, sub-28_run-01, sub-28_run-02, sub-28_run-03, sub-29_run-01, sub-29_run-02, sub-29_run-03, sub-30_run-01, sub-30_run-02, sub-30_run-03, sub-31_run-01, sub-31_run-02, sub-31_run-03, sub-32_run-01, sub-32_run-02, sub-32_run-03, sub-33_run-01, sub-33_run-02, sub-33_run-03, sub-34_run-01, sub-34_run-02, sub-34_run-03, sub-36_run-01, sub-36_run-02, sub-36_run-03, sub-37_run-01, sub-37_run-02, sub-37_run-03, sub-38_run-01, sub-38_run-02, sub-38_run-03, sub-39_run-02, sub-39_run-03, sub-40_run-01, sub-40_run-02, sub-40_run-03, sub-41_run-01, sub-41_run-02, sub-41_run-03, sub-42_run-01, sub-42_run-02, sub-42_run-03, sub-43_run-01, sub-43_run-02, sub-43_run-03, sub-45_run-01, sub-45_run-02, sub-45_run-03, sub-46_run-01, sub-46_run-02, sub-46_run-03, sub-47_run-01, sub-47_run-02, sub-47_run-03, sub-48_run-01, sub-48_run-02, sub-48_run-03, sub-50_run-01, sub-50_run-02, sub-50_run-03, sub-51_run-01, sub-51_run-02, sub-51_run-03

The distribution for subjects and runs in ParallelAdaptation are below. 

![Dice](./imgs/ds001848_task-ParallelAdaptation_hist-dicesimilarity.png)
![Voxels Out](./imgs/ds001848_task-ParallelAdaptation_hist-voxoutmask.png)

### Statistical Maps

#### devnonsym
![devnonsym Map](./imgs/ds001848_task-ParallelAdaptation_contrast-devnonsym_map.png)

#### devsym
![devsym Map](./imgs/ds001848_task-ParallelAdaptation_contrast-devsym_map.png)

#### devphys
![devphys Map](./imgs/ds001848_task-ParallelAdaptation_contrast-devphys_map.png)

#### devsym4vdevsym1
![devsym4vdevsym1 Map](./imgs/ds001848_task-ParallelAdaptation_contrast-devsym4vdevsym1_map.png)

#### devnonsym4vnondevsym1
![devnonsym4vnondevsym1 Map](./imgs/ds001848_task-ParallelAdaptation_contrast-devnonsym4vnondevsym1_map.png)

#### devphys4vdevphys1
![devphys4vdevphys1 Map](./imgs/ds001848_task-ParallelAdaptation_contrast-devphys4vdevphys1_map.png)

#### catchsym4vcatchsym1
![catchsym4vcatchsym1 Map](./imgs/ds001848_task-ParallelAdaptation_contrast-catchsym4vcatchsym1_map.png)

#### symnonsym4vphys4
![symnonsym4vphys4 Map](./imgs/ds001848_task-ParallelAdaptation_contrast-symnonsym4vphys4_map.png)

#### symnonsym4vcatch4
![symnonsym4vcatch4 Map](./imgs/ds001848_task-ParallelAdaptation_contrast-symnonsym4vcatch4_map.png)

#### dist4v1
![dist4v1 Map](./imgs/ds001848_task-ParallelAdaptation_contrast-dist4v1_map.png)
