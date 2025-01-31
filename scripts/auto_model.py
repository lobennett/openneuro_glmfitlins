import json
from pathlib import Path
from bids.modeling import auto_model
from bids.layout import BIDSLayout
from bids.modeling import BIDSStatsModelsGraph
from nilearn.plotting import plot_design_matrix

db_path = "/Users/demidenm/Desktop/Academia/Stanford/9_ResearchSci/OpenNeuro/openneuro_fitlins/datasets/input/ds000102"
root = "/Users/demidenm/Desktop/Academia/Stanford/9_ResearchSci/OpenNeuro/openneuro_fitlins/datasets/fmriprep/ds000102"
out_spec = "/Users/demidenm/Desktop/Academia/Stanford/9_ResearchSci/OpenNeuro/openneuro_fitlins/openneuro_glmfitlins/statsmodel_specs"
layout = BIDSLayout(db_path)

print(layout.get(suffix="events", extension=".tsv"))
