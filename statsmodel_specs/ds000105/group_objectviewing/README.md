# ds000105: objectviewing Task Analysis Report
## Analysis Overview
Subject-level models were fit for 6 subjects performing the objectviewing task.
HRF model type: spm. Data were smoothed at each run using a 5mm FWHM (default: isotropic additive smoothing)
### Regressors of Interest
trial_type.bottle, trial_type.cat, trial_type.chair, trial_type.face, trial_type.house, trial_type.scissors, trial_type.scrambledpix, trial_type.shoe, intercept
### Nuisance Regressors
trans_x, trans_x_derivative1, trans_x_derivative1_power2, trans_x_power2, trans_y, trans_y_derivative1, trans_y_derivative1_power2, trans_y_power2, trans_z, trans_z_derivative1, trans_z_derivative1_power2, trans_z_power2, rot_x, rot_x_derivative1, rot_x_derivative1_power2, rot_x_power2, rot_y, rot_y_derivative1, rot_y_derivative1_power2, rot_y_power2, rot_z, rot_z_derivative1, rot_z_derivative1_power2, rot_z_power2, cosine00, cosine01, cosine02
## Model Structure
- Run-level models: Yes
- Subject-level models: Yes

The run-wise contrast estimates for each subject are averaged using a fixed-effects model.
## Contrasts of Interest
- **shoe**: 1*`trial_type.shoe`
- **house**: 1*`trial_type.house`
- **chair**: 1*`trial_type.chair`
- **cat**: 1*`trial_type.cat`
- **face**: 1*`trial_type.face`
- **scrambledpix**: 1*`trial_type.scrambledpix`
- **bottle**: 1*`trial_type.bottle`
- **scissors**: 1*`trial_type.scissors`
- **shoevscrambpix**: 1*`trial_type.shoe` - 1*`trial_type.scrambledpix`
- **housevscrambpix**: 1*`trial_type.house` - 1*`trial_type.scrambledpix`
- **chairvscrambdpix**: 1*`trial_type.chair` - 1*`trial_type.scrambledpix`
- **catvscrambpix**: 1*`trial_type.cat` - 1*`trial_type.scrambledpix`
- **facevscrambpix**: 1*`trial_type.face` - 1*`trial_type.scrambledpix`
- **bottlevscrambpix**: 1*`trial_type.bottle` - 1*`trial_type.scrambledpix`
- **scissorsvscrambpix**: 1*`trial_type.scissors` - 1*`trial_type.scrambledpix`
- **shoevhouse**: 1*`trial_type.shoe` - 1*`trial_type.house`
- **shoevchair**: 1*`trial_type.shoe` - 1*`trial_type.chair`
- **shoevcat**: 1*`trial_type.shoe` - 1*`trial_type.cat`
- **shoevface**: 1*`trial_type.shoe` - 1*`trial_type.face`
- **shoevbottle**: 1*`trial_type.shoe` - 1*`trial_type.bottle`
- **shoevsscissors**: 1*`trial_type.shoe` - 1*`trial_type.scissors`
- **housevchair**: 1*`trial_type.house` - 1*`trial_type.chair`
- **housevcat**: 1*`trial_type.house` - 1*`trial_type.cat`
- **housevface**: 1*`trial_type.house` - 1*`trial_type.face`
- **housevbottle**: 1*`trial_type.house` - 1*`trial_type.bottle`
- **housevsscissors**: 1*`trial_type.house` - 1*`trial_type.scissors`
- **chairvcat**: 1*`trial_type.chair` - 1*`trial_type.cat`
- **chairvface**: 1*`trial_type.chair` - 1*`trial_type.face`
- **chairvbottle**: 1*`trial_type.chair` - 1*`trial_type.bottle`
- **chairvsscissors**: 1*`trial_type.chair` - 1*`trial_type.scissors`
- **catvface**: 1*`trial_type.cat` - 1*`trial_type.face`
- **catvbottle**: 1*`trial_type.cat` - 1*`trial_type.bottle`
- **catvsscissors**: 1*`trial_type.cat` - 1*`trial_type.scissors`
- **facevbottle**: 1*`trial_type.face` - 1*`trial_type.bottle`
- **facevsscissors**: 1*`trial_type.face` - 1*`trial_type.scissors`
- **bottlevsscissors**: 1*`trial_type.bottle` - 1*`trial_type.scissors`

## Figures

### Contrast Weights
![Contrast Weight](./imgs/ds000105_task-objectviewing_contrast-matrix.svg)

The contrast maps represents the weights used to model brain activity.

### Design Matrix
![Design Matrix](./imgs/ds000105_task-objectviewing_design-matrix.svg)

The example design matrix illustrates the model used in the statistical analyses for this task (Note: if motion outliers are included, the number of these will vary between subjects). Each column represents a regressor (of interest or not of interest, based on the above), and each row represents a time point in the BOLD timeseries. The colored patterns show how different experimental conditions are modeled across the scan duration (HRF model).

### Variance Inflation Factor (VIF)
![VIF Distribution](./imgs/ds000105_task-objectviewing_vif-boxplot.png)

The above includes 1) regressor and 2) contrast VIF estimates. The VIF boxplot quantifies multicollinearity between model regressors and how they impact contrasts (for more on contrasts VIFs, see [Dr. Mumford's repo](https://github.com/jmumford/vif_contrasts)). Lower VIF values indicate more statistically independent regressors, which is desirable for reliable parameter estimation. VIFs were estimated using the first-level model design matrices -- nusiance regressors are excluded here for brevity.

### Voxelwise Model Variance Explained (r-squared)
Voxelwise R-squared values represent the proportion of variance explained by the model at each voxel in the brain. The R-squared images shown here are calculated across runs, subjects and/or sessions (dependent on data Fitlins nodes) for the study and task.

#### Voxelwise Average (Mean)
The **mean** R-squared image reflect the average of the R-squared values across all subjects and runs.In other words, the fluctuation in how much variability in the BOLD signal the model explains at a given voxel.
![R Square](./imgs/ds000105_task-objectviewing_rsquare-mean.png)

#### Voxelwise Variance (Standard Deviation)
The **standard deviation** (or variance) image provides insights into the variability of model performance.In otherwords, across subjects, runs and/or sessions, how much variability there is in the models ability to explain the BOLD at a given voxel.

#### Flagged Subjects
The quality assessment pipeline evaluates volumetric data across multiple dimensions to identify problematic datasets. Subjects are flagged using: 

  - Dice Estimate: Similarity coefficient between subject r-squared maps and Target Space MNI152 mask falls below .85 
  - Voxels Outside of Mask: Percentage of voxels outside of the target brain mask is greater than the .10% (liberal threshold due to liberal brain masks in fMRIPrep BOLD) 

The subjects flagged for objectviewing are:
sub-2_run-1, sub-2_run-10, sub-2_run-11, sub-2_run-12, sub-2_run-2, sub-2_run-3, sub-2_run-4, sub-2_run-5, sub-2_run-6, sub-2_run-7, sub-2_run-9, sub-3_run-1, sub-3_run-10, sub-3_run-11, sub-3_run-12, sub-3_run-2, sub-3_run-3, sub-3_run-4, sub-3_run-5, sub-3_run-6, sub-3_run-7, sub-3_run-8, sub-3_run-9, sub-4_run-1, sub-4_run-10, sub-4_run-11, sub-4_run-12, sub-4_run-2, sub-4_run-3, sub-4_run-4, sub-4_run-5, sub-4_run-6, sub-4_run-7, sub-4_run-8, sub-4_run-9, sub-5_run-1, sub-5_run-10, sub-5_run-11, sub-5_run-2, sub-5_run-3, sub-5_run-4, sub-5_run-5, sub-5_run-6, sub-5_run-7, sub-5_run-8, sub-5_run-9, sub-6_run-1, sub-6_run-10, sub-6_run-11, sub-6_run-12, sub-6_run-2, sub-6_run-3, sub-6_run-4, sub-6_run-5, sub-6_run-6, sub-6_run-7, sub-6_run-8, sub-6_run-9

The distribution for subjects and runs in objectviewing are below. 

![Dice](./imgs/ds000105_task-objectviewing_hist-dicesimilarity.png)
![Voxels Out](./imgs/ds000105_task-objectviewing_hist-voxoutmask.png)

### Statistical Maps

#### shoe
![shoe Map](./imgs/ds000105_task-objectviewing_contrast-shoe_map.png)

#### house
![house Map](./imgs/ds000105_task-objectviewing_contrast-house_map.png)

#### chair
![chair Map](./imgs/ds000105_task-objectviewing_contrast-chair_map.png)

#### cat
![cat Map](./imgs/ds000105_task-objectviewing_contrast-cat_map.png)

#### face
![face Map](./imgs/ds000105_task-objectviewing_contrast-face_map.png)

#### scrambledpix
![scrambledpix Map](./imgs/ds000105_task-objectviewing_contrast-scrambledpix_map.png)

#### bottle
![bottle Map](./imgs/ds000105_task-objectviewing_contrast-bottle_map.png)

#### scissors
![scissors Map](./imgs/ds000105_task-objectviewing_contrast-scissors_map.png)

#### shoevscrambpix
![shoevscrambpix Map](./imgs/ds000105_task-objectviewing_contrast-shoevscrambpix_map.png)

#### housevscrambpix
![housevscrambpix Map](./imgs/ds000105_task-objectviewing_contrast-housevscrambpix_map.png)

#### chairvscrambdpix
![chairvscrambdpix Map](./imgs/ds000105_task-objectviewing_contrast-chairvscrambdpix_map.png)

#### catvscrambpix
![catvscrambpix Map](./imgs/ds000105_task-objectviewing_contrast-catvscrambpix_map.png)

#### facevscrambpix
![facevscrambpix Map](./imgs/ds000105_task-objectviewing_contrast-facevscrambpix_map.png)

#### bottlevscrambpix
![bottlevscrambpix Map](./imgs/ds000105_task-objectviewing_contrast-bottlevscrambpix_map.png)

#### scissorsvscrambpix
![scissorsvscrambpix Map](./imgs/ds000105_task-objectviewing_contrast-scissorsvscrambpix_map.png)

#### shoevhouse
![shoevhouse Map](./imgs/ds000105_task-objectviewing_contrast-shoevhouse_map.png)

#### shoevchair
![shoevchair Map](./imgs/ds000105_task-objectviewing_contrast-shoevchair_map.png)

#### shoevcat
![shoevcat Map](./imgs/ds000105_task-objectviewing_contrast-shoevcat_map.png)

#### shoevface
![shoevface Map](./imgs/ds000105_task-objectviewing_contrast-shoevface_map.png)

#### shoevbottle
![shoevbottle Map](./imgs/ds000105_task-objectviewing_contrast-shoevbottle_map.png)

#### shoevsscissors
![shoevsscissors Map](./imgs/ds000105_task-objectviewing_contrast-shoevsscissors_map.png)

#### housevchair
![housevchair Map](./imgs/ds000105_task-objectviewing_contrast-housevchair_map.png)

#### housevcat
![housevcat Map](./imgs/ds000105_task-objectviewing_contrast-housevcat_map.png)

#### housevface
![housevface Map](./imgs/ds000105_task-objectviewing_contrast-housevface_map.png)

#### housevbottle
![housevbottle Map](./imgs/ds000105_task-objectviewing_contrast-housevbottle_map.png)

#### housevsscissors
![housevsscissors Map](./imgs/ds000105_task-objectviewing_contrast-housevsscissors_map.png)

#### chairvcat
![chairvcat Map](./imgs/ds000105_task-objectviewing_contrast-chairvcat_map.png)

#### chairvface
![chairvface Map](./imgs/ds000105_task-objectviewing_contrast-chairvface_map.png)

#### chairvbottle
![chairvbottle Map](./imgs/ds000105_task-objectviewing_contrast-chairvbottle_map.png)

#### chairvsscissors
![chairvsscissors Map](./imgs/ds000105_task-objectviewing_contrast-chairvsscissors_map.png)

#### catvface
![catvface Map](./imgs/ds000105_task-objectviewing_contrast-catvface_map.png)

#### catvbottle
![catvbottle Map](./imgs/ds000105_task-objectviewing_contrast-catvbottle_map.png)

#### catvsscissors
![catvsscissors Map](./imgs/ds000105_task-objectviewing_contrast-catvsscissors_map.png)

#### facevbottle
![facevbottle Map](./imgs/ds000105_task-objectviewing_contrast-facevbottle_map.png)

#### facevsscissors
![facevsscissors Map](./imgs/ds000105_task-objectviewing_contrast-facevsscissors_map.png)

#### bottlevsscissors
![bottlevsscissors Map](./imgs/ds000105_task-objectviewing_contrast-bottlevsscissors_map.png)
