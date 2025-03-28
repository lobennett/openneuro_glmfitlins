import argparse
import os
import json
import numpy as np
from utils import get_numvolumes, trim_derivatives
from bids.layout import BIDSLayout


## Set up argument parsing
parser = argparse.ArgumentParser(description="Setup OpenNeuro study variables")
parser.add_argument("--openneuro_study", type=str, required=True, help="OpenNeuro study ID")
parser.add_argument("--task", type=str, required=True, help="Task label")
parser.add_argument("--deriv_dir", type=str, required=True, help="fMRIprep Derivatives Folder")
parser.add_argument("--specs_dir", type=str, required=True, help="stat model specs containing study details")
args = parser.parse_args()

study_id = args.openneuro_study
taskname = args.task
fmriprep_path = args.deriv_dir
spec_dir = args.specs_dir

# grab task specific specs
with open(f'{spec_dir}/{study_id}_basic-details.json', 'r') as file:
    specdata = json.load(file)

taskspecs = specdata.get('Tasks').get(taskname)
boldvolumes = int(taskspecs.get('bold_volumes'))
dummyvolumes = taskspecs.get('dummy_volumes')
dummyvolumes = int(dummyvolumes) if dummyvolumes is not None else 0  # Default to 0 if None
final_vols = (boldvolumes - dummyvolumes)

preproc_events = taskspecs.get('preproc_events')

print(f"\tGenerating Layout of Derivatives {fmriprep_path}/../")
preproc_layout = BIDSLayout(f"{fmriprep_path}/..", derivatives=True)
task_bold_files = preproc_layout.get(task=taskname, suffix="bold", extension=".nii.gz")
task_conf_files = preproc_layout.get(task=taskname, suffix="timeseries", extension=".tsv")

if not task_bold_files or not task_conf_files:
    ValueError(f"No files found for task: {taskname}")

# check and trim bold files if needed
for bold_file in task_bold_files:
    bold_volcheck = get_numvolumes(bold_file.path)
    
    if bold_volcheck != final_vols:
        print(f"BOLD volumes in {bold_file.filename} do not match expected target")
        print(f"\tBOLD volumes: {bold_volcheck} | Target volumes: {final_vols} | Adjusting by: {dummyvolumes}.")
        
        try:
            trimmed_nifti = trim_calibration_volumes(
                bold_path=bold_file.path, 
                num_voltotrim=dummyvolumes
            )
            trimmed_nifti.to_filename(bold_file.path)
            print(f"Trimmed BOLD file overwritten for {bold_file.filename}")
        except Exception as e:
            print(f"Error processing BOLD file {bold_file.filename}: {e}")
    else:
        print(f"BOLD data for {bold_file.filename} appears to be preprocessed")

# check and trim bold files if needed
for conf_file in task_conf_files:
    conf_df = pd.read_csv(conf_file.path, sep='\t')
    conf_volcheck = len(conf_df)
    
    if conf_volcheck != final_vols:
        print(f"Confounds rows in {conf_file.filename} do not match expected target")
        print(f"\tConfounds rows: {conf_volcheck} | Target volumes: {final_vols} | Adjusting by: {dummyvolumes}.")
        
        try:
            trimmed_confounds = trim_confounds(
                confounds_path=conf_file.path, 
                num_rowstotrim=dummyvolumes
            )
            trimmed_confounds.to_csv(conf_file.path, sep='\t', index=False)
            print(f"Trimmed confounds file overwritten for {conf_file.filename}")
        except Exception as e:
            print(f"Error processing confounds file {conf_file.filename}: {e}")
    else:
        print(f"Confounds data for {conf_file.filename} appears to be preprocessed")


