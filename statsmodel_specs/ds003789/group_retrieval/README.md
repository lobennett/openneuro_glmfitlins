# ds003789: retrieval Task Analysis Report
## Analysis Overview
Subject-level models were fit for 32 subjects performing the retrieval task.
HRF model type: spm. Data were smoothed at each run using a 5mm FWHM (default: isotropic additive smoothing)
### Regressors of Interest
trial_type.foil_new, trial_type.lure_new, trial_type.lure_old, trial_type.target_old, rt_reg.rt, intercept
### Nuisance Regressors
trans_x, trans_x_derivative1, trans_x_derivative1_power2, trans_x_power2, trans_y, trans_y_derivative1, trans_y_derivative1_power2, trans_y_power2, trans_z, trans_z_derivative1, trans_z_derivative1_power2, trans_z_power2, rot_x, rot_x_derivative1, rot_x_derivative1_power2, rot_x_power2, rot_y, rot_y_derivative1, rot_y_derivative1_power2, rot_y_power2, rot_z, rot_z_derivative1, rot_z_derivative1_power2, rot_z_power2, cosine00, cosine01, cosine02, cosine03, cosine04
## Model Structure
- Run-level models: Yes
- Subject-level models: Yes

The run-wise contrast estimates for each subject are averaged using a fixed-effects model.
## Contrasts of Interest
- **targetoldvfoilnew**: 1*`trial_type.target_old` - 1*`trial_type.foil_new`
- **targetoldvlureold**: 1*`trial_type.target_old` - 1*`trial_type.lure_old`
- **foilnewvlurenew**: 1*`trial_type.foil_new` - 1*`trial_type.lure_new`
- **lureoldvslurenew**: 1*`trial_type.lure_old` - 1*`trial_type.lure_new`
- **oldvsnew**: 0.5*`trial_type.target_old` + 0.5*`trial_type.lure_old` - 0.5*`trial_type.foil_new` - 0.5*`trial_type.lure_new`
- **targetold**: 1*`trial_type.target_old`
- **lureold**: 1*`trial_type.lure_old`
- **foilnew**: 1*`trial_type.foil_new`
- **lurenew**: 1*`trial_type.lure_new`
- **alllure**: 0.5*`trial_type.lure_old` + 0.5*`trial_type.lure_new`
- **rt**: 1*`rt_reg.rt`

## Figures

### Contrast Weights
![Contrast Weight](./imgs/ds003789_task-retrieval_contrast-matrix.svg)

The contrast maps represents the weights used to model brain activity.

### Design Matrix
![Design Matrix](./imgs/ds003789_task-retrieval_design-matrix.svg)

The example design matrix illustrates the model used in the statistical analyses for this task (Note: if motion outliers are included, the number of these will vary between subjects). Each column represents a regressor (of interest or not of interest, based on the above), and each row represents a time point in the BOLD timeseries. The colored patterns show how different experimental conditions are modeled across the scan duration (HRF model).

### Variance Inflation Factor (VIF)
![VIF Distribution](./imgs/ds003789_task-retrieval_vif-boxplot.png)

The above includes 1) regressor and 2) contrast VIF estimates. The VIF boxplot quantifies multicollinearity between model regressors and how they impact contrasts (for more on contrasts VIFs, see [Dr. Mumford's repo](https://github.com/jmumford/vif_contrasts)). Lower VIF values indicate more statistically independent regressors, which is desirable for reliable parameter estimation. VIFs were estimated using the first-level model design matrices -- nusiance regressors are excluded here for brevity.

### Voxelwise Model Variance Explained (r-squared)
Voxelwise R-squared values represent the proportion of variance explained by the model at each voxel in the brain. The R-squared images shown here are calculated across runs, subjects and/or sessions (dependent on data Fitlins nodes) for the study and task.

#### Voxelwise Average (Mean)
The **mean** R-squared image reflect the average of the R-squared values across all subjects and runs.In other words, the fluctuation in how much variability in the BOLD signal the model explains at a given voxel.
![R Square](./imgs/ds003789_task-retrieval_rsquare-mean.png)

#### Voxelwise Variance (Standard Deviation)
The **standard deviation** (or variance) image provides insights into the variability of model performance.In otherwords, across subjects, runs and/or sessions, how much variability there is in the models ability to explain the BOLD at a given voxel.

#### Flagged Subjects
The quality assessment pipeline evaluates volumetric data across multiple dimensions to identify problematic datasets. Subjects are flagged using: 

  - Dice Estimate: Similarity coefficient between subject r-squared maps and Target Space MNI152 mask falls below .85 
  - Voxels Outside of Mask: Percentage of voxels outside of the target brain mask is greater than the .10% (liberal threshold due to liberal brain masks in fMRIPrep BOLD) 

The subjects flagged for retrieval are:
sub5411_run02, sub5411_run03, sub5415_run01, sub5415_run02, sub5415_run03, sub5426_run01, sub5426_run02, sub5426_run03, sub5437_run01, sub5437_run02, sub5437_run03

The distribution for subjects and runs in retrieval are below. 

![Dice](./imgs/ds003789_task-retrieval_hist-dicesimilarity.png)
![Voxels Out](./imgs/ds003789_task-retrieval_hist-voxoutmask.png)

### Statistical Maps

#### targetoldvfoilnew
![targetoldvfoilnew Map](./imgs/ds003789_task-retrieval_contrast-targetoldvfoilnew_map.png)

#### targetoldvlureold
![targetoldvlureold Map](./imgs/ds003789_task-retrieval_contrast-targetoldvlureold_map.png)

#### foilnewvlurenew
![foilnewvlurenew Map](./imgs/ds003789_task-retrieval_contrast-foilnewvlurenew_map.png)

#### lureoldvslurenew
![lureoldvslurenew Map](./imgs/ds003789_task-retrieval_contrast-lureoldvslurenew_map.png)

#### oldvsnew
![oldvsnew Map](./imgs/ds003789_task-retrieval_contrast-oldvsnew_map.png)

#### targetold
![targetold Map](./imgs/ds003789_task-retrieval_contrast-targetold_map.png)

#### lureold
![lureold Map](./imgs/ds003789_task-retrieval_contrast-lureold_map.png)

#### foilnew
![foilnew Map](./imgs/ds003789_task-retrieval_contrast-foilnew_map.png)

#### lurenew
![lurenew Map](./imgs/ds003789_task-retrieval_contrast-lurenew_map.png)

#### alllure
![alllure Map](./imgs/ds003789_task-retrieval_contrast-alllure_map.png)

#### rt
![rt Map](./imgs/ds003789_task-retrieval_contrast-rt_map.png)
