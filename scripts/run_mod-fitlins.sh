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
    uv --project ${repo_dir} run python ${scripts_dir}/create_mod-specs.py \
      --openneuro_study ${openneuro_id} \
      --task ${task_label} \
      --script_dir ${scripts_dir}
else
    echo -e "\tSkipping creation of model specs."
fi

# Create model specifications if desired
read -p "Trim BOLD and Prepare Events? (yes/no): " prep_bold
if [[ "$prep_bold" =~ ^[Yy]([Ee][Ss])?$ ]]; then
    uv --project ${repo_dir} run python ${scripts_dir}/prep_boldevents.py \
      --openneuro_study ${openneuro_id} \
      --task ${task_label} \
      --deriv_dir ${data}/fmriprep/${openneuro_id}/derivatives \
      --specs_dir ${repo_dir}/statsmodel_specs/${openneuro_id}
else
    echo -e "\tSkipping BOLD and events prep."
fi

# Run Fitlins if desired
read -p "Run Fitlins container? (yes/no): " start_fitlins
if [[ ! "$start_fitlins" =~ ^[Yy]([Ee][Ss])?$ ]]; then
    echo "Execution skipped."
    exit 0
fi

echo
echo "Running Fitlins with the paths:"
echo "BIDS input: ${data}/input/${openneuro_id}"
echo "fmriprep derivatives: ${data}/fmriprep/${openneuro_id}/derivatives"
echo "Analyses output: ${data}/analyses/${openneuro_id}"
echo "Model specs: ${model_json}"
echo "Working directory: ${scratch}"
echo 

uv --project ${repo_dir} \
      run fitlins ${data}/input/${openneuro_id} ${data}/analyses/${openneuro_id} \
      participant \
      -m ${model_json} \
      -d ${data}/fmriprep/${openneuro_id}/derivatives \
      --ignore "sub-.*_physio\.(json|tsv\.gz)" \
      --space MNI152NLin2009cAsym --desc-label preproc \
      --smoothing 5:run:iso --estimator nilearn \
      -w ${scratch}