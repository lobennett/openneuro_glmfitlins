# openneuro_glmfitlins

**Maintainer**: Michael Demidenko  
**Contact**: [demidenko.michael@gmail.com](mailto:demidenko.michael@gmail.com)

*This repository is a work in-progress. Last updated: 2025-03-03*

## Overview

`openneuro_glmfitlins` provides scripts to analyze OpenNeuro datasets using [FitLins](https://github.com/poldracklab/fitlins) via [BIDS Stats Models](https://bids-standard.github.io/stats-models/). The goal is to facilitate efficient and reproducible neuroimaging data analysis with minimal barriers to entry.

## Features

- **Automatic Setup**: Uses [./setup_uv.sh](setup_uv.sh) to install [uv](https://docs.astral.sh/uv/guides/install-python/) Python manager, verify GitHub, DataLad and git-annex versions, and create an environment with required Python packages
- **Automated Data Retrieval**: Uses DataLad and AWS CLI to clone BIDS input data and download fMRIPrep preprocessed MRI/fMRI data
- **Flexible Analysis Specifications**: Provides summaries of relevant subject, run, and task fMRI data for easier curation of statistical models
- **Reproducible Environments**: Uses Docker/Singularity for computational reproducibility
- **High Performance Computing**: Facilitates recomputation of minimally preprocessed MRI data and FitLins modeling

## Repository Structure

- `scripts/`: Scripts for data download, JSON file creation, and FitLins model analysis, including cluster jobs
- `statsmodel_specs/`: JSON files specifying statistical models for each OpenNeuro study, with MRIQC summaries and README files
- `LICENSE`: MIT License governing the use of this repository
- `path_config.json`: Configuration file for directory paths

## Prerequisites

- **System Dependencies**:
  - [Docker](https://docs.docker.com/get-docker/) or [Singularity](https://sylabs.io/singularity/)
  - [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)
  - [DataLad](https://www.datalad.org/)
  - Git version ≥ 2.2 (check with `git --version`)

- **Python Dependencies**:
  - Python 3.12 or higher
  - numpy, pandas, pybids, datalad

## Installation

### Local System Setup

For Docker (Mac example):
```bash
# Install Docker Desktop from https://docs.docker.com/desktop/setup/install/mac-install/
docker pull poldracklab/fitlins:0.11.0
```

For Singularity:
```bash
singularity build fitlins-0.11.0.simg docker://poldracklab/fitlins:0.11.0
```

## Usage

1. **Clone the repository**:
   ```bash
   git clone git@github.com:demidenm/openneuro_glmfitlins.git
   ```

2. **Run setup and sync environment**:
   ```bash
   bash setup_uv.sh
   uv sync  # Run this each time you restart terminal
   ```

3. **Configure paths** in `path_config.json`:
   - `datasets_folder`: Location for BIDS files, fMRIPrep derivatives, and results
   - `openneuro_glmrepo`: Path to the cloned repository
   - `tmp_folder`: Temporary/scratch folder for FitLins intermediate files

4. **Download OpenNeuro data**:
   ```bash
   cd openneuro_glmfitlins/scripts/
   bash download_data.sh ds000001
   ```
   
   The script will show the size of the fMRIPrep directory and ask for confirmation. You can reduce download size by specifying exclusions in `file_exclusions.json`.

5. **Run the model**:
   ```bash
   bash run_mod-fitlins.sh ds000001 balloonanalogrisktask
   ```
   
   When prompted, respond "yes" to generate the specs file, then examine `statsmodel_specs/ds000001/ds000001_specs.json` before running FitLins. Use the [BIDS Model Validator](https://bids-standard.github.io/stats-models/validator.html) to check for JSON errors.

## License

This project is licensed under the MIT License. See the LICENSE file for details.