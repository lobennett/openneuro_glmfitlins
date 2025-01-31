import argparse
import os
import sys
import subprocess
import json


# Set up argument parsing
parser = argparse.ArgumentParser(description="Setup OpenNeuro study variables")
parser.add_argument("openneuro_study", type=str, help="OpenNeuro study ID")
parser.add_argument("data_dir", type=str, help="Base directory for dataset storage")
args = parser.parse_args()

# Assign arguments to variables
openneuro_study = args.openneuro_study
data_dir = os.path.abspath(args.data_dir)

# Define paths
file_exclude_list = os.path.join('.', "file_exclusions.json")
bids_data = os.path.join(data_dir, "input")
fmriprep_dir = os.path.join(data_dir, "fmriprep")
git_repo_url = f"https://github.com/OpenNeuroDatasets/{openneuro_study}.git"

print("Checking whether the BIDS data and fMRIprep directories exist for values: ")
print(f"    OpenNeuro Study: {openneuro_study}")
print(f"    Data Directory: {data_dir}")
print(f"    BIDS Data Path: {bids_data}")
print(f"    fMRIPrep Directory: {fmriprep_dir}")
print(f"    Git Repo URL: {git_repo_url}")
print()

bids_input_dir = os.path.join(bids_data, openneuro_study)
if os.path.exists(bids_input_dir):
    print(f"        {openneuro_study} already exists. Skipping BIDS data clone.")
else:
    try:
        # Run the datalad clone command
        subprocess.run(['datalad', 'clone', git_repo_url, bids_input_dir], check=True)
        print(f"    {openneuro_study}. Dataset cloned successfully.")

    except subprocess.CalledProcessError as e:
        # Check if the error is related to an outdated Git version
        if 'error: unknown option `show-origin`' in str(e):
            print("     Error: Your Git version may be outdated. Please confirm and update Git.")
            print("     Use 'git --version' to check your version.")

        else:
            print(f"        An error occurred while cloning the dataset: {e}")


# Build the AWS CLI command
fmriprep_out_dir = os.path.join(fmriprep_dir, openneuro_study, "derivatives")
download_fmriprep = [
    "aws", "s3", "sync", "--no-sign-request",
    f"s3://openneuro-derivatives/fmriprep/{openneuro_study}-fmriprep",
    fmriprep_out_dir
]

move_file_command = [
    "cp", 
    os.path.join(fmriprep_out_dir, "dataset_description.json"), 
    os.path.join(fmriprep_out_dir, "..", "dataset_description.json")
]


if os.path.exists(fmriprep_out_dir):
    print(f"        fMRIprep Directory already exists. Skipping fMRIprep data download for {openneuro_study}")
else:
    # Load and Add Exclusions to file
    with open(file_exclude_list, "r") as file:
        data = json.load(file)
        exclusions = data.get("exclusions", [])
    for pattern in exclusions:
        download_fmriprep.extend(["--exclude", pattern])
    
    try:
        subprocess.run(download_fmriprep, check=True)
        subprocess.run(move_file_command, check=True)

        print("     S3 sync completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"        An error occurred: {e}")
