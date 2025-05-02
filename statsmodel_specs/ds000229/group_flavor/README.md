# ds000229: flavor Task Analysis Report

The size of the Fitlins Derivatives for ds000229 flavor is 9.6G with 5666 files.

## Statistical Analysis Boilerplate

### First-level Analysis
FitLins was employed to estimate task-related BOLD activity in the flavor task for 15 subjects. In this instance, FitLins used the Nilearn estimator in its statistical modeling of the BOLD data. For each participant, 8 regressors of interest (see list below) were convolved with a spm hemodynamic response function in Nilearn. The design matrix incorporated both regressors of interest and 35 additional components, including a drift cosine basis set and nuisance regressors to account for sources of noise in the BOLD signal. Following Nilearn's *FirstLevelModel* default procedure, each voxel's timeseries was mean-scaled by each voxel's mean BOLD signal. Data were smoothed at each run using a 5mm full-width at half maximum smoothing kernal (default: isotropic additive smoothing). From the resulting model, 15 distinct contrast estimates were computed (see list below).

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
trial_type.onefifty, trial_type.onetwelve, trial_type.rinse, trial_type.seventyfive, trial_type.thirtyseven, trial_type.tless, trial_type.zero, intercept
### Nuisance Regressors
trans_x, trans_x_derivative1, trans_x_derivative1_power2, trans_x_power2, trans_y, trans_y_derivative1, trans_y_derivative1_power2, trans_y_power2, trans_z, trans_z_derivative1, trans_z_derivative1_power2, trans_z_power2, rot_x, rot_x_derivative1, rot_x_derivative1_power2, rot_x_power2, rot_y, rot_y_derivative1, rot_y_derivative1_power2, rot_y_power2, rot_z, rot_z_derivative1, rot_z_derivative1_power2, rot_z_power2, cosine00, cosine01, cosine02, cosine03, cosine04, cosine05, cosine06, cosine07, cosine08, cosine09, cosine10
## Model Structure
- Run-level models: Yes
- Subject-level models: Yes

## Contrasts of Interest
- **rinse**: 1*`trial_type.rinse`
- **tasteless**: 1*`trial_type.tless`
- **tastelessvrinse**: 1*`trial_type.tless` - 1*`trial_type.rinse`
- **cs150**: 1*`trial_type.onefifty`
- **cs112**: 1*`trial_type.onetwelve`
- **cs75**: 1*`trial_type.seventyfive`
- **csabovevbelow100**: 0.5*`trial_type.onefifty` + 0.5*`trial_type.onetwelve` - 0.333*`trial_type.seventyfive` - 0.333*`trial_type.thirtyseven` - 0.333*`trial_type.zero`
- **csthirtyseven**: 1*`trial_type.thirtyseven`
- **cszero**: 1*`trial_type.zero`
- **csbelow100v0**: 0.5*`trial_type.seventyfive` + 0.5*`trial_type.thirtyseven` - 1*`trial_type.zero`
- **csabove100v0**: 0.5*`trial_type.onefifty` + 0.5*`trial_type.onetwelve` - 1*`trial_type.zero`
- **allcsvrinse**: 0.25*`trial_type.onefifty` + 0.25*`trial_type.onetwelve` + 0.25*`trial_type.seventyfive` + 0.25*`trial_type.thirtyseven` - 1*`trial_type.rinse`
- **allcsvtasteless**: 0.25*`trial_type.onefifty` + 0.25*`trial_type.onetwelve` + 0.25*`trial_type.seventyfive` + 0.25*`trial_type.thirtyseven` - 1*`trial_type.tless`
- **paperfig3a**: 0.5*`trial_type.seventyfive` + 0.5*`trial_type.onetwelve` - 0.5*`trial_type.onefifty` - 0.5*`trial_type.thirtyseven`
- **paperfig3b**: 1*`trial_type.seventyfive` - 0.25*`trial_type.zero` - 0.25*`trial_type.onetwelve` - 0.25*`trial_type.onefifty` - 0.25*`trial_type.thirtyseven`

## Figures

### Contrast Weights
![Contrast Weight](./imgs/ds000229_task-flavor_contrast-matrix.svg)

The contrast maps represents the weights used to model brain activity.

### Design Matrix
![Design Matrix](./imgs/ds000229_task-flavor_design-matrix.svg)

The example design matrix illustrates the model used in the statistical analyses for this task (Note: if motion outliers are included, the number of these will vary between subjects). Each column represents a regressor (of interest or not of interest, based on the above), and each row represents a time point in the BOLD timeseries. The colored patterns show how different experimental conditions are modeled across the scan duration (HRF model).

### Variance Inflation Factor (VIF)
![VIF Distribution](./imgs/ds000229_task-flavor_vif-boxplot.png)

The above includes 1) regressor and 2) contrast VIF estimates. The VIF boxplot quantifies multicollinearity between model regressors and how they impact contrasts (for more on contrasts VIFs, see [Dr. Mumford's repo](https://github.com/jmumford/vif_contrasts)). Lower VIF values indicate more statistically independent regressors, which is desirable for reliable parameter estimation. VIFs were estimated using the first-level model design matrices -- nusiance regressors are excluded here for brevity.

### Voxelwise Model Variance Explained (r-squared)
Voxelwise R-squared values represent the proportion of variance explained by the model at each voxel in the brain. The R-squared images shown here are calculated across runs, subjects and/or sessions (dependent on data Fitlins nodes) for the study and task.

#### Voxelwise Average (Mean)
The **mean** R-squared image reflect the average of the R-squared values across all subjects and runs.In other words, the fluctuation in how much variability in the BOLD signal the model explains at a given voxel.
![R Square](./imgs/ds000229_task-flavor_rsquare-mean.png)

#### Voxelwise Variance (Standard Deviation)
The **standard deviation** (or variance) image provides insights into the variability of model performance.In otherwords, across subjects, runs and/or sessions, how much variability there is in the models ability to explain the BOLD at a given voxel.

#### Flagged Subjects
The quality assessment pipeline evaluates volumetric data across multiple dimensions to identify problematic datasets. Subjects are flagged using: 

  - Dice Estimate: Similarity coefficient between subject r-squared maps and Target Space MNI152 mask falls below .85 
  - Voxels Outside of Mask: Percentage of voxels outside of the target brain mask is greater than the .10% (liberal threshold due to liberal brain masks in fMRIPrep BOLD) 

The subjects flagged for flavor are:
sub-05_run-02, sub-06_run-01, sub-06_run-02, sub-06_run-03, sub-07_run-01, sub-07_run-02, sub-07_run-03, sub-08_run-01, sub-10_run-01, sub-10_run-03

The distribution for subjects and runs in flavor are below. 

![Dice](./imgs/ds000229_task-flavor_hist-dicesimilarity.png)
![Voxels Out](./imgs/ds000229_task-flavor_hist-voxoutmask.png)

### Statistical Maps

#### rinse
![rinse Map](./imgs/ds000229_task-flavor_contrast-rinse_map.png)

#### tasteless
![tasteless Map](./imgs/ds000229_task-flavor_contrast-tasteless_map.png)

#### tastelessvrinse
![tastelessvrinse Map](./imgs/ds000229_task-flavor_contrast-tastelessvrinse_map.png)

#### cs150
![cs150 Map](./imgs/ds000229_task-flavor_contrast-cs150_map.png)

#### cs112
![cs112 Map](./imgs/ds000229_task-flavor_contrast-cs112_map.png)

#### cs75
![cs75 Map](./imgs/ds000229_task-flavor_contrast-cs75_map.png)

#### csabovevbelow100
![csabovevbelow100 Map](./imgs/ds000229_task-flavor_contrast-csabovevbelow100_map.png)

#### csthirtyseven
![csthirtyseven Map](./imgs/ds000229_task-flavor_contrast-csthirtyseven_map.png)

#### cszero
![cszero Map](./imgs/ds000229_task-flavor_contrast-cszero_map.png)

#### csbelow100v0
![csbelow100v0 Map](./imgs/ds000229_task-flavor_contrast-csbelow100v0_map.png)

#### csabove100v0
![csabove100v0 Map](./imgs/ds000229_task-flavor_contrast-csabove100v0_map.png)

#### allcsvrinse
![allcsvrinse Map](./imgs/ds000229_task-flavor_contrast-allcsvrinse_map.png)

#### allcsvtasteless
![allcsvtasteless Map](./imgs/ds000229_task-flavor_contrast-allcsvtasteless_map.png)

#### paperfig3a
![paperfig3a Map](./imgs/ds000229_task-flavor_contrast-paperfig3a_map.png)

#### paperfig3b
![paperfig3b Map](./imgs/ds000229_task-flavor_contrast-paperfig3b_map.png)
