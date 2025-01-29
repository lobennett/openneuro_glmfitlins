import os
import json
import numpy as np


## Set up argument parsing
parser = argparse.ArgumentParser(description="Setup OpenNeuro study variables")
parser.add_argument("--openneuro_study", type=str, required=True, help="OpenNeuro study ID")
parser.add_argument("--task", type=str, required=True, help="Task label")
parser.add_argument("--script_dir", type=str, required=True, help="Base directory for scripts")
args = parser.parse_args()

# Assign arguments to variables
study_id = args.openneuro_study
task = args.task
scripts = os.path.abspath(args.script_dir)

# Load the model JSON
sample_specs = os.path.join(scripts, "example_mod-specs.json")

if os.path.exists(sample_specs):
    print("working on file", sample_specs)
    with open(sample_specs, "r") as file:
        model_data = json.load(file)
else:
    print("Error: The model JSON file does not exist.", sample_specs)
    exit(1)

# Load the subjects JSON
subjects_json = os.path.join(scripts, "..", "statsmodel_specs", f"{study_id}_subjects.json")
if os.path.exists(subjects_json):
    print("working on file", subjects_json)    
    with open(subjects_json, "r") as file:
        subjects_data = json.load(file)
else:
    print("Error: The subjects JSON file does not exist.", subjects_json)
    exit(1)

# Load the contrasts JSON
contrast_json = os.path.join(scripts, "..", "statsmodel_specs", f"{study_id}_contrasts.json")
if os.path.exists(contrast_json):
    print("working on file", contrast_json)
    with open(contrast_json, "r") as file:
        contrast_data = json.load(file)
else:
    print("Error: The contrasts JSON file does not exist.", contrast_json)
    exit(1)


# Update the Study Name
if "Name" in model_data:
    model_data["Name"] = f"{study_id}"

# Update the Task Values
if "Input" in model_data:
    model_data["Input"]["task"] = [task]

# Update the subjects in the model
if "Input" in model_data:
    model_data["Input"]["subject"] = subjects_data["Subjects"]

# Update the contrasts in the model (for the "Run" level node)
for node in model_data["Nodes"]:
    if node["Level"] == "Run":
        node["Contrasts"] = contrast_data["Contrasts"]
        break  # Exit loop after updating

# Save the updated model JSON
with open(os.path.join(scripts, "..", "statsmodel_specs", f"{study_id}_specs.json"), "w") as file:
    json.dump(model_data, file, indent=2)

print("Model specs created, updated study name, task, subjects and contrasts")