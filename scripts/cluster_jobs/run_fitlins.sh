#!/bin/bash
#SBATCH --job-name=fitlins
#SBATCH --time=01:00:00
#SBATCH --cpus-per-task=4
#SBATCH --mem-per-cpu=12GB
#SBATCH -p russpold,normal,owners

# Output and notifications
#SBATCH --output=./logs/fitlins.%A_%a.out
#SBATCH --error=./logs/fitlins.%A_%a.err
#SBATCH --mail-user=demidenm@stanford.edu
#SBATCH --mail-type=ALL

# -------------------- Parameter Checking --------------------
if [ -z "$1" ] || [ -z "$2" ]; then
  echo "Usage: sbatch $0 <OpenNeuro Study ID> <Task Label>"
  echo "Example: sbatch $0 ds003425 learning"
  exit 1
fi

study_id=$1
task_label=$2

# -------------------- Load Configuration --------------------
config_file="../../path_config.json"

if [ ! -f "$config_file" ]; then
  echo "Error: Configuration file $config_file not found."
  exit 1
fi

data_dir=$(jq -r '.datasets_folder' "$config_file")
repo_dir=$(jq -r '.openneuro_glmrepo' "$config_file")
model_json="${repo_dir}/statsmodel_specs/${study_id}/${study_id}-${task_label}_specs.json"
scratch_out=$(jq -r '.tmp_folder' "$config_file")
env_source=$(jq -r '.env_source' "$config_file")
env_name=$(jq -r '.env_name' "$config_file")
singularity_img=$(jq -r '.fitlins_simg' "$config_file")

# -------------------- Set Up Environment --------------------
echo "Setting up Python environment with uv..."
cd "$repo_dir" || { echo "Error: Failed to change directory to $repo_dir"; exit 1; }
source ".venv/bin/activate"

# -------------------- Set Up Input, Scratch, Output Directories --------------------
input_data_dir="${data_dir}/input/${study_id}"
scratch_data_dir="${scratch_out}/fitlins/task-${task_label}"
output_data_dir="${data_dir}/analyses/${study_id}/task-${task_label}"
fmriprep_data_dir="${data_dir}/fmriprep/${study_id}/derivatives"


# make directories
mkdir -p "${scratch_data_dir}"
mkdir -p "${output_data_dir}"

# -------------------- Run Fitlins --------------------
echo "#### Running Fitlins models to generate statistical maps ####"
echo "Study ID: $study_id"
echo "Task Label: $task_label"
echo "Input Data: ${input_data_dir}"
echo "Scratch Output: ${scratch_data_dir}"
echo "FMRIPrep Directory: ${fmriprep_data_dir}"
echo "Model Spec: ${model_json}"

uv --project "$repo_dir" \
      run fitlins "${input_data_dir}" "${output_data_dir}" \
      participant \
      -m "$model_json" \
      -d "${fmriprep_data_dir}" \
      --ignore "sub-.*_physio\.(json|tsv\.gz)" \
      --space MNI152NLin2009cAsym --desc-label preproc \
      --smoothing 5:run:iso --estimator nilearn \
      --n-cpus 4 \
      --mem-gb 48 \
      -w "${scratch_data_dir}"