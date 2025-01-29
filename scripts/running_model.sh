#!/bin/bash

# Set data / environment paths for data download and BIDS Stats Models
openneuro_id="ds000102"
task_label="flanker"
data="/Users/demidenm/Desktop/Academia/Stanford/9_ResearchSci/OpenNeuro/openneuro_fitlins/datasets"
model_json="/Users/demidenm/Desktop/Academia/Stanford/9_ResearchSci/OpenNeuro/openneuro_fitlins/openneuro_glmfitlins/statsmodel_specs/${openneuro_id}_specs.json"
scratch="/tmp/"
scripts_dir=`pwd`


# Check if data exist, if not, download
python ${scripts_dir}/get_openneuro-data.py ${openneuro_id} ${data}


read -p "Do the files './statsmodel-specs/${openneuro_id}_*' exist and are set up? (yes/no): " user_input
  
if [[ "$user_input" == "yes" ]]; then
  # create model specs if files are setup
  if [ ! -f ${model_json} ]; then
    python ${scripts_dir}/create_mod-specs.py --openneuro_study ${openneuro_id} --task ${task_label} --script_dir ${scripts_dir}
  fi
 
  # binding the bids input bids, fmriprep derivatives and analyses output directory to docker container
  echo
  echio "Running docker with the paths:"
  echo "BIDS input: ${data}/input/${openneuro_id}"
  echo "fmriprep derivatives: ${data}/fmriprep/${openneuro_id}"
  echo "Analyses output: ${data}/analyses/${openneuro_id}"
  echo "Model specs: ${model_json}"
  echo 

  docker run --rm -it \
    -v ${data}/input/${openneuro_id}:/bids \
    -v ${data}/fmriprep/${openneuro_id}:/fmriprep_deriv \
    -v ${data}/analyses/${openneuro_id}:/analyses_out \
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

else
    # If files are not set up, ask the user to update
    echo "Please update './statsmodel-specs/${study_id}_*' files before proceeding and review the resulting spec file."

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