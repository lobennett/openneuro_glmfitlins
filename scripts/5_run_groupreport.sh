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
data=$(jq -r '.datasets_folder' "$config_file")
repo_dir=$(jq -r '.openneuro_glmrepo' "$config_file")
scratch_out=$(jq -r '.tmp_folder' "$config_file")
specs_dir="${repo_dir}/statsmodel_specs"
scripts_dir="${repo_dir}/scripts"
analysis_dir="${data}/analyses/${openneuro_id}/task-${task_label}"
scratch_data_dir="${scratch_out}/fitlins/task-${task_label}"


uv --project ${repo_dir} \
    run ${scripts_dir}/prep_report_py/groupmap_report.py \
    --openneuro_study ${openneuro_id} \
    --taskname ${task_label} \
    --analysis_dir ${analysis_dir} \
    --spec_dir ${specs_dir} \
    --scratch_dir ${scratch_data_dir} 

