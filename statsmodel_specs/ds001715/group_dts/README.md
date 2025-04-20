# ds001715: dts Task Analysis Report
## Analysis Overview
Subject-level models were fit for 34 subjects performing the dts task.
HRF model type: spm. Data were smoothed at each run using a 5mm FWHM (default: isotropic additive smoothing)
### Regressors of Interest
signedmotion_cohright, signedmotion_abs, signedcolor_cohright, missed_trial, signedcolor_abs, rt_reg.1, intercept
### Nuisance Regressors
trans_x, trans_x_derivative1, trans_x_derivative1_power2, trans_x_power2, trans_y, trans_y_derivative1, trans_y_derivative1_power2, trans_y_power2, trans_z, trans_z_derivative1, trans_z_derivative1_power2, trans_z_power2, rot_x, rot_x_derivative1, rot_x_derivative1_power2, rot_x_power2, rot_y, rot_y_derivative1, rot_y_derivative1_power2, rot_y_power2, rot_z, rot_z_derivative1, rot_z_derivative1_power2, rot_z_power2, cosine00, cosine01, cosine02, cosine03
## Model Structure
- Run-level models: Yes
- Subject-level models: Yes

The run-wise contrast estimates for each subject are averaged using a fixed-effects model.
## Contrasts of Interest
- **motionaligneffect**: 1*`signedmotion_cohright`
- **coloraligneffect**: 1*`signedcolor_cohright`
- **alignmotionvcolor**: 1*`signedmotion_cohright` - 1*`signedcolor_cohright`
- **absmotioneffect**: 1*`signedcolor_abs`
- **abscolorneffect**: 1*`signedcolor_abs`
- **absmotionvcolor**: 1*`signedcolor_abs` - 1*`signedcolor_abs`
- **rt**: 1*`rt_reg.1`

## Figures

### Contrast Weights
![Contrast Weight](./imgs/ds001715_task-dts_contrast-matrix.svg)

The contrast maps represents the weights used to model brain activity.

### Design Matrix
![Design Matrix](./imgs/ds001715_task-dts_design-matrix.svg)

The example design matrix illustrates the model used in the statistical analyses for this task (Note: if motion outliers are included, the number of these will vary between subjects). Each column represents a regressor (of interest or not of interest, based on the above), and each row represents a time point in the BOLD timeseries. The colored patterns show how different experimental conditions are modeled across the scan duration (HRF model).

### Variance Inflation Factor (VIF)
![VIF Distribution](./imgs/ds001715_task-dts_vif-boxplot.png)

The above includes 1) regressor and 2) contrast VIF estimates. The VIF boxplot quantifies multicollinearity between model regressors and how they impact contrasts (for more on contrasts VIFs, see [Dr. Mumford's repo](https://github.com/jmumford/vif_contrasts)). Lower VIF values indicate more statistically independent regressors, which is desirable for reliable parameter estimation. VIFs were estimated using the first-level model design matrices -- nusiance regressors are excluded here for brevity.

### Voxelwise Model Variance Explained (r-squared)
Voxelwise R-squared values represent the proportion of variance explained by the model at each voxel in the brain. The R-squared images shown here are calculated across runs, subjects and/or sessions (dependent on data Fitlins nodes) for the study and task.

#### Voxelwise Average (Mean)
The **mean** R-squared image reflect the average of the R-squared values across all subjects and runs.In other words, the fluctuation in how much variability in the BOLD signal the model explains at a given voxel.
![R Square](./imgs/ds001715_task-dts_rsquare-mean.png)

#### Voxelwise Variance (Standard Deviation)
The **standard deviation** (or variance) image provides insights into the variability of model performance.In otherwords, across subjects, runs and/or sessions, how much variability there is in the models ability to explain the BOLD at a given voxel.

#### Flagged Subjects
The quality assessment pipeline evaluates volumetric data across multiple dimensions to identify problematic datasets. Subjects are flagged using: 

  - Dice Estimate: Similarity coefficient between subject r-squared maps and Target Space MNI152 mask falls below .85 
  - Voxels Outside of Mask: Percentage of voxels outside of the target brain mask is greater than the .10% (liberal threshold due to liberal brain masks in fMRIPrep BOLD) 

The subjects flagged for dts are:
sub01_run01, sub01_run02, sub01_run03, sub01_run04, sub01_run05, sub01_run06, sub01_run07, sub01_run08, sub01_run09, sub01_run10, sub01_run11, sub01_run12, sub05_run10, sub08_run02, sub08_run05, sub08_run11, sub08_run12, sub09_run01, sub09_run02, sub09_run03, sub09_run04, sub09_run05, sub09_run06, sub09_run07, sub09_run08, sub09_run09, sub09_run10, sub09_run11, sub09_run12, sub23_run01, sub23_run02, sub23_run03, sub23_run04, sub23_run05, sub23_run06, sub23_run07, sub23_run08, sub23_run09, sub23_run10, sub23_run11, sub23_run12, sub27_run08, sub32_run01, sub32_run02, sub32_run03, sub32_run04, sub32_run05, sub32_run06, sub32_run07, sub32_run08, sub32_run09, sub32_run10, sub32_run11, sub32_run12

The distribution for subjects and runs in dts are below. 

![Dice](./imgs/ds001715_task-dts_hist-dicesimilarity.png)
![Voxels Out](./imgs/ds001715_task-dts_hist-voxoutmask.png)

### Statistical Maps

#### motionaligneffect
![motionaligneffect Map](./imgs/ds001715_task-dts_contrast-motionaligneffect_map.png)

#### coloraligneffect
![coloraligneffect Map](./imgs/ds001715_task-dts_contrast-coloraligneffect_map.png)

#### alignmotionvcolor
![alignmotionvcolor Map](./imgs/ds001715_task-dts_contrast-alignmotionvcolor_map.png)

#### absmotioneffect
![absmotioneffect Map](./imgs/ds001715_task-dts_contrast-absmotioneffect_map.png)

#### abscolorneffect
![abscolorneffect Map](./imgs/ds001715_task-dts_contrast-abscolorneffect_map.png)

#### absmotionvcolor
![absmotionvcolor Map](./imgs/ds001715_task-dts_contrast-absmotionvcolor_map.png)

#### rt
![rt Map](./imgs/ds001715_task-dts_contrast-rt_map.png)
