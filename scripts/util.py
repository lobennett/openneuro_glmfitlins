import os 

def process_dataset(data_id, output_fold):
    """
    Process a single dataset: download files and save them locally.

    Args:
        data_id (str): The ID of the dataset to process.
        output_fold (str): The directory where dataset files will be saved.
    """
    print("Downloading File data for dataset: {}".format(data_id))
    dataset_id = data_id
    dataset_out = os.path.join(output_fold, dataset_id)

    snapshots = access_functions.get_snapshots(dataset_id)
    if not snapshots:
        print(f"No snapshots found for dataset {dataset_id}.")
        return

    latest_snapshot = snapshots[-1].split(":")[1]
    print(latest_snapshot)

    response = access_functions.get_participants_tsv(dataset_id, tag=latest_snapshot)
    if not os.path.exists(dataset_out):
        os.mkdir(dataset_out)

    if response:
        files_urls = access_functions.extract_filenames_and_urls(response)
        for info in files_urls:
            if info["filename"] in ["participants.json", "participants.tsv", "dataset_description.json"] or fnmatch.fnmatch(info["filename"], '*_events.json'):
                for url in info["urls"]:
                    access_functions.download_file(url, f"{dataset_out}/{info['filename']}")
    else:
        print(f"Failed to retrieve participant TSV for dataset {dataset_id}.")