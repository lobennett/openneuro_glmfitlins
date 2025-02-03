#!/bin/bash

# Set data / environment paths for data download and BIDS Stats Models
openneuro_id=$1 # OpenNeuro ID, e.g. ds000102
if [ -z "$openneuro_id" ]; then
  echo "Please provide the OpenNeuro ID (e.g. ds000001) as the first argument."
  exit 1
fi

task_label=${2} # Task label, e.g. 'flanker'
if [ -z "$task_label" ]; then
  echo "Please provide the task label (e.g. 'balloonanalogrisktask') as the second argument."
  exit 1
fi

# sets paths from config file
config_file="../path_config.json"

# Extract values using jq
data=$(jq -r '.datasets_folder' "$config_file")
repo_dir=$(jq -r '.openneuro_glmrepo' "$config_file")
model_json="${repo_dir}/statsmodel_specs/${openneuro_id}/${openneuro_id}_specs.json"
scripts_dir="${repo_dir}/scripts"
scratch=$(jq -r '.tmp_folder' "$config_file")


read -p "Do the files ${model_json} exist and are set up? (yes/no): " user_input
  
if [[ "$user_input" == "yes" ]]; then
  # create model specs if files are setup
  if [ ! -f ${model_json} ]; then
    python ${scripts_dir}/create_mod-specs.py --openneuro_study ${openneuro_id} --task ${task_label} --script_dir ${scripts_dir}
  fi
 
  # binding the bids input bids, fmriprep derivatives and analyses output directory to docker container
  echo
  echo "Running docker with the paths:"
  echo "BIDS input: ${data}/input/${openneuro_id}"
  echo "fmriprep derivatives: ${data}/fmriprep/${openneuro_id}/derivatives"
  echo "Analyses output: ${data}/analyses/${openneuro_id}"
  echo "Model specs: ${model_json}"
  echo 

  docker run --rm -it \
    -v ${data}/input/${openneuro_id}:/bids \
    -v ${data}/fmriprep/${openneuro_id}/derivatives:/fmriprep_deriv \
    -v ${data}/analyses/${openneuro_id}:/analyses_out \
    -v ${model_json}:/bids/model_spec \
    -v ${scratch}:/workdir \
    poldracklab/fitlins:0.11.0 \
    /bids /analyses_out run \
    -m /bids/model_spec -d /fmriprep_deriv \
    --space MNI152NLin2009cAsym --desc-label preproc \
    --smoothing 5:run:iso --estimator nilearn \
    --n-cpus 1 \
    --mem-gb 24 \
    -w /workdir

else
    # If files are not set up, ask the user to update
    echo "Please update ${model_json} files before proceeding and review the resulting spec file."

fi
 


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