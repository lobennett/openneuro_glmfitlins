#!/bin/bash
#
#SBATCH --job-name=fitlins
#SBATCH --array=1 # 
#SBATCH --time=01:00:00
#SBATCH --cpus-per-task=4
#SBATCH --mem-per-cpu=12GB
#SBATCH -p russpold,normal,owners
# Outputs ----------------------------------
#SBATCH --output=./cluster_jobs/logs/fitlins.%A_%a.out
#SBATCH --error=./cluster_jobs/logs/fitlins.%A_%a.err
#SBATCH --mail-user=demidenm@stanford.edu
#SBATCH --mail-type=ALL
# ------------------------------------------

# open neuro ID & task
if [ -z "$1" ]; then
  echo "Error: OpenNeuro study ID (e.g. ds003425) is required."
  echo "sbatch recreate_fmrip.sh ds003425 learning"
  echo
  exit 1
fi

if [ -z "$2" ]; then
  echo "Error: OpenNeuro task (e.g. learning) is required."
  echo "sbatch recreate_fmrip.sh ds003425 learning"
  echo
  exit 1
fi

study_id=${1}
task_label=${2}

# config paths
singularity=$(which singularity || { echo "Singularity not found. Exiting."; exit 1; })
config_file=./../path_config.json
data_dir=$(jq -r '.datasets_folder' "$config_file")
repo_dir=$(jq -r '.openneuro_glmrepo' "$config_file")
model_json="${repo_dir}/statsmodel_specs/${study_id}/${study_id}-${task_label}_specs.json"
scratch_out=$(jq -r '.tmp_folder' "$config_file")
env_source=$(jq -r '.env_source' "$config_file")
env_name=$(jq -r '.env_name' "$config_file")
singularity_img=$(jq -r '.fitlins_simg' "$config_file")


# set conda env
source ${env_source}
mamba activate ${env_name}

# Run fitlins model
# create derivative and scratch dirs
[ ! -d ${scratch_out}/mod ] && mkdir -p ${scratch_out}/mod && echo "scratch directory created for fitlins mod"
[ ! -d ${data_dir}/analyses/${study_id} ] && mkdir -p ${data_dir}/analyses/${study_id} && echo "Created analyses/${study_id}  folder"


echo "#### Running Fitlins models to generate statistical maps ####"
echo "Study ID ${study_id} and Task Label ${task_label}"
echo "data_in: ${data_dir}/input/${study_id}"
echo "scratch_out: ${scratch_out}/mod"
echo "fmriprep_dir: ${data_dir}/fmriprep/${study_id}/derivatives"
echo "model spec: ${model_json}"

singularity run --cleanenv \
      -B ${data_dir}/input/${study_id}:/bids \
      -B ${data_dir}/fmriprep/${study_id}/derivatives:/fmriprep_deriv \
      -B ${data_dir}/analyses/${study_id}:/analyses_out \
      -B ${model_json}:/bids/model_spec \
      -B ${scratch_out}/mod:/workdir \
      ${singularity_img} \
      /bids /analyses_out participant \
      -m /bids/model_spec -d /fmriprep_deriv \
      --ignore "sub-.*_physio\.(json|tsv\.gz)" \
      --space MNI152NLin2009cAsym --desc-label preproc \
      --smoothing 5:run:iso --estimator nilearn \
      --n-cpus 4 \
      --mem-gb 48 \
      -w /workdir
