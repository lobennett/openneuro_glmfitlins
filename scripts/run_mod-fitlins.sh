#!/bin/bash
set -euo pipefail

# Check for required arguments
if [ $# -lt 2 ]; then
  echo "Usage: $0 <openneuro_id> <task_label>"
  echo "Example: $0 ds000102 flanker"
  exit 1
fi

# Get command line arguments
openneuro_id=$1 # OpenNeuro ID, e.g. ds000102
task_label=$2 # Task label, e.g. 'flanker'

# Set paths from config file
relative_path=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
config_file=$(realpath ${relative_path}/../path_config.json)

# config file exists
if [ ! -f "$config_file" ]; then
  echo "Error: Config file not found at $config_file"
  exit 1
fi

# Extract values using jq
data=$(jq -r '.datasets_folder' "$config_file")
repo_dir=$(jq -r '.openneuro_glmrepo' "$config_file")
scripts_dir="${repo_dir}/scripts"
scratch=$(jq -r '.tmp_folder' "$config_file")
model_json="${repo_dir}/statsmodel_specs/${openneuro_id}/${openneuro_id}-${task_label}_specs.json"

# Create model specifications if desired
read -p "Create model specifications? (yes/no): " run_create_specs
if [[ "$run_create_specs" =~ ^[Yy]([Ee][Ss])?$ ]]; then
    uv run python ${scripts_dir}/create_mod-specs.py \
      --openneuro_study ${openneuro_id} \
      --task ${task_label} \
      --script_dir ${scripts_dir}
else
    echo "Skipping creation of model specs."
fi

# Run Fitlins if desired
read -p "Run Fitlins container? (yes/no): " start_fitlins
if [[ ! "$start_fitlins" =~ ^[Yy]([Ee][Ss])?$ ]]; then
    echo "Execution skipped."
    exit 0
fi

# Determine whether to use Docker or Singularity
read -p "Run using docker or singularity? (dock/sing): " run_type
if [[ "$run_type" == "dock" ]]; then
    echo
    echo "Running docker with the paths:"
    echo "BIDS input: ${data}/input/${openneuro_id}"
    echo "fmriprep derivatives: ${data}/fmriprep/${openneuro_id}/derivatives"
    echo "Analyses output: ${data}/analyses/${openneuro_id}"
    echo "Model specs: ${model_json}"
    echo "Working directory: ${scratch}"
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
elif [[ "$run_type" == "sing" ]]; then
    echo
    echo "Running singularity: sbatch sing_fitlins.sh"
    echo 
    sbatch cluster_jobs/sing_fitlins.sh ${openneuro_id} ${task_label}
else
    echo "Invalid option: ${run_type}. Must be 'dock' or 'sing'. Exiting."
    exit 1
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
