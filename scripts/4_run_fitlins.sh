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
config_file=$(realpath "${relative_path}/../path_config.json")

# config file exists
if [ ! -f "$config_file" ]; then
  echo "Error: Config file not found at $config_file"
  exit 1
fi

# Extract values using jq
data_dir=$(jq -r '.datasets_folder' "$config_file")
repo_dir=$(jq -r '.openneuro_glmrepo' "$config_file")
scripts_dir="${repo_dir}/scripts"
scratch_out=$(jq -r '.tmp_folder' "$config_file")
model_json="${repo_dir}/statsmodel_specs/${openneuro_id}/${openneuro_id}-${task_label}_specs.json"
smoothing_type="5:run:iso"


# -------------------- Set Up Input, Scratch, Output Directories --------------------
bids_data_dir="${data_dir}/fmriprep/${openneuro_id}"
scratch_data_dir="${scratch_out}/fitlins/task-${task_label}"
output_data_dir="${data_dir}/analyses/${openneuro_id}/task-${task_label}"

if [ -d "${data_dir}/fmriprep/${openneuro_id}/derivatives_alt" ]; then
  fmriprep_data_dir="${data_dir}/fmriprep/${openneuro_id}/derivatives_alt"
else
  fmriprep_data_dir="${data_dir}/fmriprep/${openneuro_id}/derivatives"
fi


# Create model specifications if desired
if [[ -f "$model_json" ]]; then
  # make directories
mkdir -p "${scratch_data_dir}"
mkdir -p "${output_data_dir}"

# -------------------- Run Fitlins --------------------
echo "#### Running Fitlins models to generate statistical maps ####"
echo -e "\tStudy ID: ${openneuro_id}"
echo -e "\tTask Label: ${task_label}"
echo -e "\tInput Events: ${bids_data_dir}"
echo -e "\tScratch Output: ${scratch_data_dir}"
echo -e "\tFMRIPrep Directory: ${fmriprep_data_dir}"
echo -e "\tModel Spec: ${model_json}"
echo -e "\tSmoothing type: ${smoothing_type}"
echo
sleep 2

uv --project "$repo_dir" \
      run fitlins "${bids_data_dir}" "${output_data_dir}" \
      participant \
      -m "${model_json}" \
      -d "${fmriprep_data_dir}" \
      --drop-missing \
      --ignore "sub-.*_physio\.(json|tsv\.gz)" \
      --space MNI152NLin2009cAsym --desc-label preproc \
      --smoothing "${smoothing_type}" --estimator nilearn \
      --n-cpus 6 \
      --mem-gb 32 \
      -w "${scratch_data_dir}"

else
  echo -e "\tModel specification does not exist. Check file and/or create: $model_json"
  echo 
  exit 1
fi
