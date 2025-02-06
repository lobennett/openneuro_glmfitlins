import os 
import json

def generate_readme(spec_path, study_id, data, repo_url="https://github.com/demidenm/openneuro_glmfitlins/blob/main"):
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
    readme_content += "## Tasks and Trial Types\n"

    for task_name, task_info in data["Tasks"].items():
        readme_content += f"### Task: {task_name}\n"
        readme_content += f"- **Column Names**: {', '.join(task_info['column_names'])}\n"
        readme_content += f"- **Data Types**: {', '.join([f'{col} ({dtype})' for col, dtype in task_info['column_data_types'].items()])}\n"
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