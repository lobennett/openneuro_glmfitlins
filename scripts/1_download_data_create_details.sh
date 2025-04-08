#!/bin/bash

if ! command -v aws &> /dev/null; then
	echo "Error: AWS CLI is not installed. Confirm your environment is activated and AWS is installed."
	exit 1
fi
# Set data / environment paths for data download and BIDS Stats Models
openneuro_id=$1 # OpenNeuro ID, e.g. ds000001
if [ -z "$openneuro_id" ]; then
  echo "Please provide the OpenNeuro ID (e.g. ds000102) as the first argument."
  exit 1
fi

# Sets paths from config file
relative_path=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
config_file=$(realpath "${relative_path}/../path_config.json")

# Extract values using jq
data=$(jq -r '.datasets_folder' "$config_file")
repo_dir=$(jq -r '.openneuro_glmrepo' "$config_file")
spec_dir="${repo_dir}/statsmodel_specs/${openneuro_id}"
scripts_dir="${repo_dir}/scripts"

# Creating directories that don't exist
for subdir in analyses fmriprep input; do 
  [ ! -d "${data}/${subdir}" ] && echo "Creating directory: ${data}/${subdir}" && mkdir -p "${data}/${subdir}"
done

[ ! -d "$spec_dir" ] && echo "Creating directory: $spec_dir" && mkdir -p "$spec_dir"

# First, confirm data / files size of fMRIPrep derivatives on s3
df_info=$(uv run aws s3 ls --no-sign-request s3://openneuro-derivatives/fmriprep/${openneuro_id}-fmriprep/ --recursive --summarize | tail -n 3)

# confirm whether minimal or not baesd on presesence of MNI.nii.gz
# return quietly for check '-q'
if aws s3 ls --recursive --no-sign-request "s3://openneuro-derivatives/fmriprep/${openneuro_id}-fmriprep/" 2>/dev/null | grep -q ".*_space-MNI152.*_desc-preproc_bold.nii.gz"; then
  minimal_derivatives="no"
  echo "Found .*_space-MNI152.*_desc-preproc_bold.nii.gz on s3, not minimal derivatives"
  echo

else
  minimal_derivatives="yes"
  echo "Did NOT find .*_space-MNI152.*_desc-preproc_bold.nii.gz on s3, contents are minimal derivatives. "
  echo -e "\t\e[31mAfter downloading the data, run recreate_fmriprep.sh script\e[0m"
  echo
  sleep 1
fi


# Extract the number of files and total size
n_files=$(echo "$df_info" | grep "Total Objects" | awk -F':' '{print $2}' | tr -d ' ')
total_size_bytes=$(echo "$df_info" | grep "Total Size" | awk -F':' '{print $2}' | tr -d ' ')

# Convert bytes to GB
gb_size=$(echo "scale=6; $total_size_bytes / (1024*1024*1024)" | bc)
gb_rnd=$(printf "%.1f" $gb_size)

echo
echo "fMRIPrep derivatives size for ${openneuro_id} is ${gb_rnd}GB with ${n_files} files."
echo "Downloading data to ${data}/fmriprep/${openneuro_id}/derivatives"
echo -e "\tNote: You can reduce the size by adding file filters into the './scripts/prep_report_py/file_exclusions.json' file."
echo -e "\tIn the event of missing derivatives (here: ${minimal_derivatives}) need to recompute derivatives, do not exclude critical files."
echo

# Check if fMRIPrep are minimal derivatives and whether to download
read -p "Do you want to proceed with the download? (yes/no): " user_input

if [[ "$user_input" == "yes" ]]; then
  if [[ "$minimal_derivatives" == "yes" ]]; then
    echo "Downloading complete BIDS and fMRIPrep'd minimal data..."
    uv run python "${scripts_dir}/prep_report_py/get_openneuro_data.py" "${openneuro_id}" "${data}" "${spec_dir}" "True"
    echo -e "\e[31mMake sure to run recreate_fmriprep.sh script\e[0m"
    echo

  elif [[ "$minimal_derivatives" == "no" ]]; then
    echo "Downloading minimal BIDS and all fMRIPrep'd derivatives..."
    uv run python "${scripts_dir}/prep_report_py/get_openneuro_data.py" "${openneuro_id}" "${data}" "${spec_dir}" "False"
    echo -e "\tCopying dataset_description.json file within the fmriprep root directory"
    cp "${data}/fmriprep/${openneuro_id}/derivatives/dataset_description.json" "${data}/fmriprep/${openneuro_id}/dataset_description.json"
    echo
  fi
 
  echo -e "\tDownload completed."
  echo 
else
  echo -e "\tNot downloading the data for ${openneuro_id}."
  echo
  exit 1
fi


# creating a symbolic link "derivatives" directory if complete fmri data is present.
# if minimal_derivatives is set to "no"
if [[ "$minimal_derivatives" == "no" ]]; then
    # Define source and destination directories
    source_dir="${data}/fmriprep/${openneuro_id}"
    dest_dir="${source_dir}/derivatives"
    
    # Create the derivatives directory if it doesn't exist
    mkdir -p "$dest_dir"
    
    # Find all files and directories in the source directory (fmriprep base). Exclude hidden and events files
    echo -e "\t Creating [hard] symbolic links from fmriprep/${openneuro_id} to fmriprep/${openneuro_id}/derivatives."
    find "$source_dir" -mindepth 1 -not -path "$dest_dir*" -not -path "*/\.*" -not -name "*_events.tsv" | while read item; do
        # Calculate the relative path
        rel_path="${item#$source_dir/}"
        
        # Create parent directories in the destination if needed
        if [[ -d "$item" ]]; then
            mkdir -p "$dest_dir/$rel_path"
        else
            # Create parent directory for the file if needed
            mkdir -p "$(dirname "$dest_dir/$rel_path")"
            
            # [hard] symbolic link for beh files so fitlins recognizes
            ln -f "$item" "$dest_dir/$rel_path"
        fi
    done
    
    echo "Data are not minimally processed, created symbolic link structure from fmriprep/${openneuro_id} in fmriprep/${openneuro_id}/derivatives."
    echo
fi


# create symbolics links of events files, to account for cases where modifications are
inp_dir="${data}/input/${openneuro_id}"
fmriprep_dest="${data}/fmriprep/${openneuro_id}"

find "$inp_dir" -type f -name '*_events.tsv' | while read -r file; do
    rel_path="${file#$inp_dir/}"
    dest_path="${fmriprep_dest}/${rel_path}"

    # if destination eexist, symbolic link eents file
    if [ -d "$(dirname "$dest_path")" ]; then
        #  [hard] symbolic link for beh files so fitlins recognizes
        ln -f "$file" "$dest_path"
    else 
      echo "$(dirname "$dest_path") folder missing"
    fi
done

echo "Starting study summary. For large datasets, BIDSLayout may take a moment to run."
echo
# Run Python script for study details
uv run python "${scripts_dir}/prep_report_py/study_simple_details.py" \
    --openneuro_study "${openneuro_id}" \
    --bids_dir "${data}/input/${openneuro_id}" \
    --fmriprep_dir "${data}/fmriprep/${openneuro_id}" \
    --spec_dir "${spec_dir}"
