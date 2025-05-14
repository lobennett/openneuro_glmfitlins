#!/bin/bash
#SBATCH --job-name=copy_dirs
#SBATCH --time=08:00:00
#SBATCH --cpus-per-task=6
#SBATCH --mem-per-cpu=4GB
#SBATCH -p russpold,normal,owners

# Output and notifications
#SBATCH --output=./logs/copy_dirs.%A_%a.out
#SBATCH --error=./logs/copy_dirs.%A_%a.err
#SBATCH --mail-user=logben@stanford.edu
#SBATCH --mail-type=ALL

# Load configuration and set paths
echo -e "\nSetting up paths and configuration..."
relative_path=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
config_file=./../../path_config.json
data_dir=$(jq -r '.datasets_folder' "$config_file")

# Create required directories
echo -e "\nCreating necessary directories..."
for subdir in analyses fmriprep input; do 
    [ ! -d "${data_dir}/${subdir}" ] && echo "  Creating directory: ${data_dir}/${subdir}" && mkdir -p "${data_dir}/${subdir}"
done

# Create source / target paths for copied dataset
# - Source directories
source_input_dir="/oak/stanford/groups/russpold/data/network_grant/discovery_BIDS_20250402"
source_fmriprep_dir="$source_input_dir/derivatives/fmriprep_latest_20250402/"
source_derivs_alt_dir="$source_input_dir/derivatives/glm_data"
# - Target directories 
target_input_dir="$data_dir/input/discovery_BIDS_20250402"
target_fmriprep_dir="$data_dir/fmriprep/discovery_BIDS_20250402"
target_derivs_alt_dir="$target_fmriprep_dir/derivatives_alt"

# Function to sync directories with better logging
sync_directories() {
    local src="$1"
    local dst="$2"
    local exclude_pattern="$3"
    local desc="$4"
    
    echo -e "\n======================================================"
    echo "Copying $desc from:"
    echo "  Source: $src"
    echo "  Target: $dst"
    echo "======================================================"
    
    # Construct rsync command based on whether an exclude pattern is provided
    if [ -n "$exclude_pattern" ]; then
        rsync -av --progress --exclude="$exclude_pattern" "${src}/" "${dst}/"
    else
        rsync -av --progress "${src}/" "${dst}/"
    fi
    
    echo "======================================================"
    echo "Completed copying $desc"
    echo "======================================================\n"
}

# Execute sync operations
sync_directories "$source_input_dir" "$target_input_dir" "derivatives/" "BIDS input data"
sync_directories "$source_fmriprep_dir" "$target_fmriprep_dir" "" "fMRIPrep derivatives"
sync_directories "$source_derivs_alt_dir" "$target_derivs_alt_dir" "" "GLM data"