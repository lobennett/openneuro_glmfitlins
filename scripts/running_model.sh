#!/bin/bash

# Set data / environment paths for data download and BIDS Stats Models
study_id="ds000102"
data="/Users/demidenm/Desktop/Academia/Stanford/9_ResearchSci/OpenNeuro/openneuro_fitlins/datasets"
model_json="/Users/demidenm/Desktop/Academia/Stanford/9_ResearchSci/OpenNeuro/openneuro_fitlins/openneuro_glmfitlins/statsmodel_specs/${study_id}_specs.json"
scratch="/tmp/"
scripts_dir=`pwd`


# Check if data exist, if not, download
python ${scripts_dir}/get_openneuro-data.py ${study_id} ${data}


# binding the bids input bids, fmriprep derivatives and analyses output directory to docker container
docker run --rm -it \
  -v ${data}/input/${study_id}:/bids \
  -v ${data}/fmriprep/${study_id}:/fmriprep_deriv \
  -v ${data}/analyses/${study_id}:/analyses_out \
  -v ${model_json}:/bids/model_spec \
  -v ${scratch}:/workdir \
  poldracklab/fitlins:0.11.0 \
  /bids /analyses_out run \
  -m /bids/model_spec -d /fmriprep_deriv \
  --space MNI152NLin2009cAsym --desc-label preproc \
  --smoothing 5:run:iso --estimator nilearn \
  --n-cpus 2 \
  --mem-gb 24 \
  -w /workdir


#singularity run --cleanenv \
#-B ${data}/raw/dsX:/data/raw/dsX \
#-B ${data}/prep/dsX/fmriprep:/data/prep/dsX/fmriprep \
#-B ${data}/analyzed/dsX:/data/analyzed/dsX \
#-B ${scratch}:/scratch \
#  ${sif_img}/fitlins-0.11.0.simg \
#    /data/raw/dsX /data/analyzed/dsX dataset \
#    -d /data/prep/dsX/fmriprep \
#    -w /scratch
#