# openneuro_glmfitlins

**Maintainer**: Michael Demidenko  
**Contact**: [email](mailto:demidenko.michael@gmail.com)

## Overview

`openneuro_glmfitlins` is a tool designed to process OpenNeuro datasets using [FitLins](https://github.com/poldracklab/fitlins) via [BIDS Stats Models](https://bids-standard.github.io/stats-models/), facilitating efficient and reproducible neuroimaging data analysis.

## Featres of this repo

- **Automated Data Retrieval**: Use DataLad and AWS CLI to clone BIDS input data and download fMRIPrep (preprocessed) MRI/fMRI data.
- **Flexible Analysis Specifications**: Download provide summarizes of relevate subject, runs, task fMRI data. Allows for easier curation of statistical models via JSON files. 
- **Reproducible Environments**: Uses docker for consistent computational reproducibile (environments)[https://fitlins.readthedocs.io/en/latest/installation.html#singularity-container].

In my case, I installed docker desktop for Mac with Apple Silicon via the (docker website)[https://docs.docker.com/desktop/setup/install/mac-install/]. This was about a 1.8GB application. After installing docker desktop and completing setup via the prompts, I ran the following to setup fitlins v0.11.0

```bash
docker pull poldracklab/fitlins:0.11.0
```
This process took ~45-60 seconds to complete, ending with the prompt "Status: Downloaded newer image for poldracklab/fitlins:0.11.0

## Repository Structure

- `scripts/`: Contains scripts for data download, json file creation and fitlins model analysis. 
- `statsmodel_specs/`: JSON files specifying statistical models for FitLins for *each* open-neuro study. Within each directory, there is also an `mriqc_summary` which is the .tsv and .html file. Within each `statsmodel_spec/STUDY_ID` there is a README file to summaries some basic information and have preview links to the .html file (i.e., git renders files)
- `LICENSE`: MIT License governing the use of this repository.
- `path_config.json`: Configuration file for directory paths. Use this to specify where the input/output data should be downloaded/saved.

## Prerequisites

Ensure the following are installed:

- **System Dependencies**:
  - [Docker](https://docs.docker.com/get-docker/)
  - [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)
  - [DataLad](https://www.datalad.org/)

- **Python Dependencies**:
  - Python 3.12 or higher
  - `numpy`
  - `pandas`
  - `pybids`
  - `datalad`

Note, you will also need at least `git` version => 2.2. Check via `git --version`

Install Python dependencies using:

```bash
pip install numpy pandas pybids datalad
```

## Usage

1. Clone repository to your machine - Start by cloning the respository using git clone:
```bash
git clone git@github.com:demidenm/openneuro_glmfitlins.git
```
2. Setup paths - Before downloading the data, make sure to update paths in the `path_config.json`. There are three primary paths you'll want to setup:
    - datasets_folder: This is where the 1) BIDS input clones files/folders, 2) fmriprep derivatives and 3) the resulting analyses data.
    - openneuro_glmrepo: this is the path to the repository you clone in step 1.
    - tmp_folder: this is your temporary/scratch folder, where intermediate files will be created for the fitlins model.
3. Download the openneuro data - Once you have 1) cloned the repository [and dependencies are installed] and 2) setup your paths, you can download your open neuro data by navigating the the `openneuro_glmfitlins/scripts/` folder and running. This will create some preliminary files such as README e.g (ds000001 example)[./statsmdeol_specs/ds000001/README.md], mriqc_summary e.g. (ds000001 BOLD example)[https://htmlpreview.github.io/?https://github.com/demidenm/openneuro_glmfitlins/blob/main/statsmodel_specs/ds000001/mriqc_summary/group_bold.html]), and *_basic-details.json in the (./statsmodels_specs/STUDY_ID directory)[./statsmodels_specs]. At the end of the script, you will also get some results dumped into the terminal. You will use the task labels, subjects and trial_type / column name information to specify your _contrasts.json and _subjects.json file that will be used in the subject step
```bash
bash download_data.sh ds000001
```
Or, if your file is executable (e.g. chmod +x download_data.sh), you can run:
```bash
./download_data.sh ds000001
```
Note, for each you will specify the open-neuro dataset number such as (ds000001)[https://openneuro.org/datasets/ds000001]. The script will prompt you with the size of the fmriprep directory that is on aws and the number of files that are in that [repository](https://github.com/OpenNeuroDerivatives/ds000001-fmriprep) and the question "Do you wnt to proceed with the download? (yes/no)". 
You can reduce the download size and file quantity by specifying exclusions in [file_exclusions.json file](./scripts/file_exclusions.json). For example, if you are only going to be interested in task fMRI analyses on the volumetric MNI data, you can save space by exclude freesurfer (e.g., ./sourcedata/freesurfer) and CIFTI outputs (e.g., fsaverage*.gii, *dtseries.nii). If you are satisfied with the file size/quantity, type "yes" and hit return.
*First, the BIDS input data will be cloned (only the non-binary files, such as .json and .tsv, as BOLD are not used). This will download quickly. **If you do not have the appropriate git or datalad install this part may return an error**.*

4. Running model - Currently, the Fitlins model specs performs a run, subject and dataset level model. The example json that is dynamically modified is [./scripts/example_mod-specs.json](./scripts/example_mod-specs.json). Once the subject and contrast json files are specified within `statsmodel_specs/ds000001`, you can response 'yes' to the first prompt to generate the `statsmodels_specs/ds000001/ds000001_specs.json` file. It will add the necessary subjects, contrasts, study and task name information from the example model spec. Answer 'no' to the next question, to run the fitlins docker. First inspect the (ds000001_specs.json)[./statsmodels_specs/ds000001/ds000001_specs.json] to ensure that your model is what you'd like to run. Make any minor modifications you need, such as removing run or dataset level models. When doing so, use the (BIDS Model Validator)[https://bids-standard.github.io/stats-models/validator.html] to catch json errors.


## License
This project is licensed under the MIT License. See the LICENSE file for details.
