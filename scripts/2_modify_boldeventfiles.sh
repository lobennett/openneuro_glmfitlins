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

# -------------------- Set Up Input, Scratch, Output Directories --------------------
spec_data_dir="${repo_dir}/statsmodel_specs/${openneuro_id}"
bids_dir_data_dir="${data}/input/${openneuro_id}"
scratch_data_dir="${scratch}/fitlins/task-${task_label}"
output_data_dir="${data}/analyses/${openneuro_id}/task-${task_label}"
fmriprep_data_dir="${data}/fmriprep/${openneuro_id}/derivatives"
fmriprep_data_dir_alt="${data}/fmriprep/${openneuro_id}/derivatives_alt"

# -------------------- Run Fitlins --------------------
echo "#### Running Fitlins models to generate statistical maps ####"
echo -e "\tStudy ID: ${openneuro_id}"
echo -e "\tTask Label: ${task_label}"
echo -e "\tInput Data: ${bids_dir_data_dir}"
echo -e "\tScratch Output: ${scratch_data_dir}"
echo -e "\tfMRIPrep Derivatives Directory: ${fmriprep_data_dir}"
echo
sleep 2

uv --project ${repo_dir} run python ${scripts_dir}/prep_report_py/prep_boldevents.py \
   --openneuro_study ${openneuro_id} \
   --task ${task_label} \
   --deriv_dir ${fmriprep_data_dir} \
   --bids_dir ${bids_dir_data_dir} \
   --specs_dir ${spec_data_dir}


if [ -d "${fmriprep_data_dir_alt}" ]; then
  cp "${fmriprep_data_dir}/dataset_description.json" "${fmriprep_data_dir_alt}"
fi
