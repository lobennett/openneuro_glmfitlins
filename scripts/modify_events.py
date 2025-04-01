import os
import pandas as pd
import numpy as np
from pathlib import Path

def ds003425(eventspath: str, task: str):
    """
    Process event data for ds003425 by modifying trial types if applicable. 
    Per DOI: 10.1038/s41598-022-05019-y, 'As noted previously we modelled CS+ reinforced (i.e., shock) trials and the first and last CS− trials as two 
    separate regressors that were not used in higher-level analyses (they were modelled similar to the conditions of interest).'
    Shock = 1=csp shock in events files
    CS- trials 4=csm and 5=csmi in events files
    Parameters:
    eventspath (str): path to the events .tsv file
    task (str): task name for dataset (regulate, learning, training, prelearning)
    
    Returns:
    modified events files
    """

    if task in ["learning", "prelearning", "regulate"]:
        eventsdat = pd.read_csv(eventspath, sep='\t')

        # Only modify if trial_type does NOT contain 6
        if 6 not in eventsdat['trial_type'].values:
            # Filter events where trial_type is 4 or 5
            filtered_events = eventsdat[eventsdat['trial_type'].isin([4, 5])]

            if not filtered_events.empty:
                # first and last row from the filtered events
                first_and_last_events = filtered_events.iloc[[0, -1]].copy()
                first_and_last_events['trial_type'] = 6

                # Append modified first and last events back to the original dataset
                eventsdat = pd.concat([eventsdat, first_and_last_events], ignore_index=True)
                eventsdat.to_csv(eventspath, sep='\t', index=False)
                print(f"Modified events file for {os.path.basename(eventspath)}")

        else:
            print(f"Trial type value '6' already contained in events file. Skipping modification for {os.path.basename(eventspath)}")

        return eventsdat

