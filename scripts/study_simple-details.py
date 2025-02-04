import json
import os
import argparse
import pandas as pd
import numpy as np
from bids.layout import BIDSLayout
from create_readme import generate_readme

# Set up argument parsing
parser = argparse.ArgumentParser(description="Setup OpenNeuro study variables")
parser.add_argument("--openneuro_study", type=str, help="OpenNeuro study ID", required=True)   
parser.add_argument("--bids_dir", type=str, help="Base BIDS Directory", required=True)
parser.add_argument("--fmriprep_dir", type=str, help="Base fMRIPrep derivatives directory if different from bids_dir", required=False)
parser.add_argument("--spec_dir", type=str, help="Directory where model specs are", required=True)

args = parser.parse_args()

# set variables
study_id = args.openneuro_study
bids_path = args.bids_dir
fmriprep_path = args.fmriprep_dir
spec_path = args.spec_dir


# get layouts
bids_layout = BIDSLayout(bids_path)
preproc_layout = BIDSLayout(fmriprep_path, derivatives=True)

# did input basics
bids_sub_n = bids_layout.get_subjects()
bids_run_n = bids_layout.get_runs()
bids_tasks = bids_layout.get_tasks()
bids_runs_array = [run or run for run in bids_run_n]

# fmriprep basics
preproc_sub_n = preproc_layout.get_subjects()
preproc_run_n = preproc_layout.get_runs()
preproc_tasks = preproc_layout.get_tasks()
preproc_runs_array = [run or run for run in preproc_run_n]

Subjects = preproc_sub_n
Tasks = preproc_tasks

# print to terminal subject details
print()
print(f"{study_id} Details for BIDS Input versus fMRIPrep")
print("============ Subjects ============")
print(f"Number of Subjects in BIDS Input: {len(bids_sub_n)}")
print(f"Number of Subjects in fMRIPrep: {len(preproc_sub_n)}")
print()
print("============ Tasks ============")
print(f"Tasks in BIDS Input: {bids_tasks}")
print(f"Tasks in fMRIPrep: {preproc_tasks}")
print()

# create dictionary to store study and task details
data = {
    "Subjects": Subjects,
    "Tasks": {}
}

# get column names, data types, and trial_type values for each task
for task_name in Tasks:
    # pull event files that match & load into single long df
    event_files = bids_layout.get(task=task_name, suffix="events", extension=".tsv")
    group_df = pd.concat([pd.read_csv(file, sep='\t') for file in event_files], ignore_index=True)

    # obtain col names and data types, get unique values for trial_type
    column_names = list(group_df.columns)
    column_data_types = {col: str(dtype) for col, dtype in zip(group_df.columns, group_df.dtypes)}
    if 'trial_type' in group_df.columns:
        trial_type_values = group_df['trial_type'].unique().tolist()
    else:
        trial_type_values = []

    # task-specific data task dict, col names, dtypes and values within 'trial_type'
    data["Tasks"][task_name] = {
        "column_names": column_names,
        "column_data_types": column_data_types,
        "trial_type_values": trial_type_values
    }

    print(f"Task: {task_name}")
    print(f"Number of event files: {len(event_files)}")
    print(f"Column names: {column_names}")
    print(f"Column data types: {column_data_types}")
    print(f"Unique 'trial_type' values: {trial_type_values}")
    print()


# save study and task details to json
with open(os.path.join(spec_path, f'{study_id}_basic-details.json'), 'w') as f:
    json.dump(data, f, indent=4)

# generate README.md file
generate_readme(spec_path, study_id, data)
