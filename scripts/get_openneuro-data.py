import os
import sys
import subprocess
import json

openneuro_study = "ds000102"
data_dir = "/Users/demidenm/Desktop/Academia/Stanford/9_ResearchSci/OpenNeuro/openneuro_fitlins/datasets"
bids_data = f"{data_dir}/input"
fmriprep_dir = f"{data_dir}/fmriprep"
git_repo_url = f"https://github.com/OpenNeuroDatasets/{openneuro_study}.git"

if os.path.exists(os.path.join(data_dir,openneuro_study)):
    print(f"{openneuro_study} already exists. Skipping BIDS data clone.")
else:
    try:
        # Run the datalad clone command
        subprocess.run(['datalad', 'clone', git_repo_url, os.path.join(data_dir,openneuro_study)], check=True)
        print(f"{openneuro_study}. Dataset cloned successfully.")

    except subprocess.CalledProcessError as e:
        # Check if the error is related to an outdated Git version
        if 'error: unknown option `show-origin`' in str(e):
            print("Error: Your Git version may be outdated. Please confirm and update Git.")
            print("Use 'git --version' to check your version.")

        else:
            print(f"An error occurred while cloning the dataset: {e}")


# Build the AWS CLI command
download_fmriprep = [
    "aws", "s3", "sync", "--no-sign-request",
    f"s3://openneuro-derivatives/fmriprep/{openneuro_study}-fmriprep",
    os.path.join(fmriprep_dir, openneuro_study),
    "--exclude", "*freesurfer*",
    "--exclude", "*fsaverage*",
    "--exclude", "*dtseries*"
]


if os.path.exists(os.path.join(fmriprep_dir, openneuro_study)):
    print(f"Already exists. Skipping fMRIprep data download for {openneuro_study}")
else:
    ## Add the exclusions to the command
    ## Load exclusions from a JSON file
    #with open("exclusions.json", "r") as file:
    #    data = json.load(file)
    #    exclusions = data.get("exclusions", [])
    #for pattern in exclusions:
    #    download_fmriprep.extend(["--exclude", pattern])
    #

    try:
        subprocess.run(download_fmriprep, check=True)
        print("S3 sync completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
