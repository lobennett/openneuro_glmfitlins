import os 
import json

def generate_studysummary(spec_path, study_id, data, repo_url="https://github.com/demidenm/openneuro_glmfitlins/blob/main"):
    """
    Generates a README.md file summarizing study details and links to MRIQC summary HTML files.

    Parameters:
    - spec_path: Path where the README.md should be saved.
    - study_id: Study identifier.
    - data: Dictionary containing study details (subjects, tasks, trial types).
    - repo_url: Base GitHub repository URL for generating HTML preview links using https://htmlpreview.github.io/
    """

    readme_content = f"# Study Details: {study_id}\n\n"
    readme_content += f"## Number of Subjects\n- BIDS Input: {len(data['Subjects'])}\n\n"

    # Add sessions information if multiple sessions exist
    if data.get('Sessions') and len(data['Sessions']) > 1:
        readme_content += "## Sessions\n"
        readme_content += f"- Sessions: {', '.join(data['Sessions'])}\n\n"

    readme_content += "## Tasks and Trial Types\n"

    for task_name, task_info in data["Tasks"].items():
        readme_content += f"### Task: {task_name}\n"
        readme_content += f"- **Column Names**: {', '.join(task_info['column_names'])}\n"
        readme_content += f"- **Data Types**: {', '.join([f'{col} ({dtype})' for col, dtype in task_info['column_data_types'].items()])}\n"
        if task_info['bold_volumes']:
            readme_content += f"- **BOLD Volumes**: {task_info['bold_volumes']}\n"
        else:
            readme_content += "- **BOLD Volumes**: None\n"
        if task_info['trial_type_values']:
            readme_content += f"- **Unique 'trial_type' Values**: {', '.join(map(str, task_info['trial_type_values']))}\n"
        else:
            readme_content += "- **Unique 'trial_type' Values**: None\n"
        readme_content += "\n"

    # Scan for HTML files in spec_path/mriqc_summary
    mriqc_dir = os.path.join(spec_path, "mriqc_summary")
    if os.path.exists(mriqc_dir):
        html_files = [f for f in os.listdir(mriqc_dir) if f.endswith(".html")]

        if html_files:
            readme_content += "## MRIQC Summary Reports\n"
            for html_file in sorted(html_files):
                file_url = f"https://htmlpreview.github.io/?{repo_url}/statsmodel_specs/{study_id}/mriqc_summary/{html_file}"
                readme_content += f"- [{html_file}]({file_url})\n"

    # Save the README.md file
    readme_path = os.path.join(spec_path, "README.md")
    with open(readme_path, "w") as f:
        f.write(readme_content)

    print(f"README.md file created at {readme_path}")
    print("\tReview output and update calibration and events preproc values, as needed\n")


def generate_groupmodsummary(study_id, task, num_subjects, hrf_model_type, signal_regressors,  
    noise_regressors, has_run, has_subject, contrast_dict, contrast_image, spec_imgs_dir):
    # Add title and description
    readme_content = f"# {study_id}: {task} Task Analysis Report\n"
    readme_content += "## Analysis Overview\n"
    readme_content += f"Subject-level models were fit for {num_subjects} subjects performing the {task} task.\n"
    readme_content += f"HRF model type: {hrf_model_type}\n"
    
    readme_content += "### Regressors of Interest\n"
    readme_content += ", ".join(signal_regressors) if signal_regressors else "None identified"
    
    readme_content += "\n### Nuisance Regressors\n"
    readme_content += ", ".join(noise_regressors) if noise_regressors else "None identified"
    
    readme_content += "\n## Model Structure\n"
    readme_content += f"- Run-level models: {'Yes' if has_run else 'No'}\n"
    readme_content += f"- Subject-level models: {'Yes' if has_subject else 'No'}\n"
    
    if has_run and has_subject:
        readme_content += "\nThe run-wise contrast estimates for each subject are averaged using a fixed-effects model."
    
    readme_content += "\n## Contrasts of Interest\n"
    for name, expr in contrast_dict.items():
        readme_content += f"- **{name}**: {expr}\n"
    
    readme_content += "\n## Figures\n"
    readme_content += f"\n### Contrast Maps\n![Contrast Map]({f"./imgs/{contrast_image}"})\n"
    readme_content += f"\n### Variance Inflation Factor (VIF)\n![VIF Distribution]({f"./imgs/{study_id}_task-{task}_vif-boxplot.png"})\n"
    
    # Add contrast maps
    readme_content += "\n### Statistical Maps\n"
    for con_name in contrast_dict.keys():
        map_path = f"./imgs/{study_id}_task-{task}_contrast-{con_name}_map.png"
        readme_content += f"\n#### {con_name}\n![{con_name} Map]({map_path})\n"
    
    return readme_content


