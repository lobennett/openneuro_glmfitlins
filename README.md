# openneuro_glmfitlins

**Maintainer**: Michael Demidenko  
**Contact**: [email](mailto:demidenko.michael@gmail.com)

*This repository is a work in-progress. It was last updated: 2025-02-27*

## Overview

`openneuro_glmfitlins` is a tool designed to process OpenNeuro datasets using [FitLins](https://github.com/poldracklab/fitlins) via [BIDS Stats Models](https://bids-standard.github.io/stats-models/), facilitating efficient and reproducible neuroimaging data analysis.

## Features of this Repo

- **Automated Data Retrieval**: Uses DataLad and AWS CLI to clone BIDS input data and download fMRIPrep (preprocessed) MRI/fMRI data.
- **Flexible Analysis Specifications**: Provides summaries of relevant subject, run, and task fMRI data, allowing for easier curation of statistical models via JSON files.
- **Reproducible Environments**: Uses Docker for consistent computational reproducibility ([FitLins Installation Guide](https://fitlins.readthedocs.io/en/latest/installation.html#singularity-container)).

In my case, I installed Docker Desktop for Mac with Apple Silicon via the [Docker website](https://docs.docker.com/desktop/setup/install/mac-install/). This was about a 1.8GB application. After installing Docker Desktop and completing setup via the prompts, I ran the following to set up FitLins v0.11.0:

```bash
docker pull poldracklab/fitlins:0.11.0
```
This process took ~45-60 seconds to complete, ending with the prompt: `Status: Downloaded newer image for poldracklab/fitlins:0.11.0`. Alternatively, if you are wanting to run via singularity, you can download the container using:

```bash
singularity build fitlins-0.11.0.simg docker://poldracklab/fitlins:0.11.0
```

## Repository Structure

- `scripts/`: Contains scripts for data download, JSON file creation, and FitLins model analysis. 
- `statsmodel_specs/`: JSON files specifying statistical models for FitLins for *each* OpenNeuro study. Each directory also contains an `mriqc_summary`, which includes `.tsv` and `.html` files. Inside `statsmodel_specs/STUDY_ID`, there is a README file summarizing basic information and providing preview links to the `.html` file (e.g., Git renders files).
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

Ensure you have `git` version >= 2.2 by checking via:
```bash
git --version
```

Install Python dependencies using:
```bash
pip install numpy pandas pybids datalad
```

## Usage

1. **Clone the repository** - Start by cloning the repository using Git:
```bash
git clone git@github.com:demidenm/openneuro_glmfitlins.git
```

2. **Setup paths** - Before downloading the data, update paths in `path_config.json`. The primary paths to set up are:
    - `datasets_folder`: Location for BIDS input files, fMRIPrep derivatives, and analysis results.
    - `openneuro_glmrepo`: Path to the repository cloned in step 1.
    - `tmp_folder`: Temporary/scratch folder for FitLins intermediate files.

3. **Download OpenNeuro data** - Once you have cloned the repository, installed dependencies, and set up paths, navigate to `openneuro_glmfitlins/scripts/` and run:
```bash
bash download_data.sh ds000001
```
Or, if the script is executable (e.g., `chmod +x download_data.sh`), you can run:
```bash
./download_data.sh ds000001
```

For each dataset, specify the OpenNeuro dataset number (e.g., [ds000001](https://openneuro.org/datasets/ds000001)). The script will prompt you with the size of the fMRIPrep directory on AWS and the number of files in that [repository](https://github.com/OpenNeuroDerivatives/ds000001-fmriprep), along with the question: *"Do you want to proceed with the download? (yes/no)"*.

You can reduce the download size by specifying exclusions in [`file_exclusions.json`](./scripts/file_exclusions.json). For example, to save space, you can exclude FreeSurfer files (`./sourcedata/freesurfer`) and CIFTI outputs (`fsaverage*.gii`, `*dtseries.nii`). If satisfied with the file size, type "yes" and press Enter.

*First, the BIDS input data will be cloned (excluding binary files such as BOLD images). If you do not have the appropriate Git or DataLad installation, this step may return an error.*

4. **Running the model** - The FitLins model specs include run, subject, and dataset-level models. The example JSON dynamically modified is [`example_mod-specs.json`](./scripts/example_mod-specs.json). Run by specifying the STUDYID and the TASKNAME
```bash
bash run_mod-fitlins.sh ds000001 balloonanalogrisktask
```
Or, if the script is executable (e.g., `chmod +x run_mod-fitlins.sh`), you can run:
```bash
././run_mod-fitlins.sh ds000001 balloonanalogrisktask
```

Once `statsmodel_specs/ds000001/` contains the required subject and contrast JSON files, respond "yes" to the first prompt to generate `ds000001_specs.json`. 


Then, answer "no" to the next question to run the FitLins Docker container. First, inspect [`ds000001_specs.json`](./statsmodel_specs/ds000001/ds000001_specs.json) to ensure the model is correct. Make modifications as needed (e.g., removing run or dataset-level models). Use the [BIDS Model Validator](https://bids-standard.github.io/stats-models/validator.html) to check for JSON errors.

## License
This project is licensed under the MIT License. See the LICENSE file for details.