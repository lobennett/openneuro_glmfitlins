#!/bin/bash
study_id="ds000102"
data="/Users/demidenm/Desktop/Academia/Stanford/9_ResearchSci/OpenNeuro/openneuro_fitlins/datasets"
model_json="/Users/demidenm/Desktop/Academia/Stanford/9_ResearchSci/OpenNeuro/openneuro_fitlins/openneuro_glmfitlins/scripts/example_fitlins.json"
scratch="/tmp/"

# binding the bids input and fmriprep directory as read-only (e.g. :ro) and the output directory as read-write (e.g. :rw)
docker run --rm -it \
  -v ${data}/input/${study_id}:/bids \
  -v ${data}/fmriprep/${study_id}:/fmriprep_deriv \
  -v ${data}/analyses/${study_id}:/analyses_out \
  -v ${model_json}:/bids/model_spec \
  -v ${scratch}:/workdir \
  poldracklab/fitlins:0.11.0 \
  /bids /analyses_out run \
  -m /bids/model_spec -d /fmriprep_deriv \
  --space MNI152NLin2009cAsym \
  --desc-label preproc \ 
  -s 5:run:iso \
  --estimator nilearn \
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