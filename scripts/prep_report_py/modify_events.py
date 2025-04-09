import os
import pandas as pd
import numpy as np
from pathlib import Path


def add_reactiontime_regressor(eventsdf, trial_type_col='trial_type', resp_trialtype: list = ['response'], 
                                response_colname: str = 'response_time', rtreg_name: str ='rt_reg', 
                                onset_colname: str = 'onset', duration_colname: str = 'duration', 
                                new_trialtype: str = None, resp_in_ms: bool = False):
    """
    Pull reaction time regressor rows and add them to the dataframe as regressor.
    Assumes reaction times are in milliseconds; converts [times] / 1000 to convert to seconds for "duration".

    Parameters
    ----------
    eventsdf : DataFrame containing event data with response times.
    trial_type_col (str): Column name for identifying response trials.
    resp_trialtype (list): Values in trial_type_col that have associated response times.
    response_colname (str): Column name containing response time.
    rtreg_name (str): Name for new reaction time regressor.
    onset_colname (str): Name for onset times column.
    duration_colname (str): Name for duration times column.
    new_trialtype (str): Column name to store the new regressor trial type.
    resp_in_ms (bool): Whether response time is in milliseconds (convert to seconds if True).

    Returns
    -------
    DataFrame with reaction time regressor rows added.
    """
    # Set name for new trialtype column
    new_trial_name = new_trialtype if new_trialtype else trial_type_col

    if isinstance(resp_trialtype, str):
        resp_trialtype = [resp_trialtype]

    # Filter and copy relevant rows
    rt_reg_rows = eventsdf[eventsdf[trial_type_col].isin(resp_trialtype)].copy()
    rt_reg_rows[new_trial_name] = rtreg_name

    # Compute duration
    if resp_in_ms:
        rt_reg_rows[duration_colname] = rt_reg_rows[response_colname] / 1000
    else:
        rt_reg_rows[duration_colname] = rt_reg_rows[response_colname]

    # Replace NAs with 0 and report how many were replaced
    na_count = rt_reg_rows[duration_colname].isna().sum()
    rt_reg_rows[duration_colname] = rt_reg_rows[duration_colname].fillna(0)

    print(f"[INFO] Replaced {na_count} missing or None RT duration values with 0.")

    # Select relevant columns and concatenate
    rt_reg_rows = rt_reg_rows[[onset_colname, duration_colname, new_trial_name]]

    # sort and reset to avoid fitlins convolution error
    result_rts = pd.concat([eventsdf, rt_reg_rows], ignore_index=True).sort_values(by="onset", ascending=True).reset_index(drop=True)
    
    return result_rts


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
                return eventsdat
        else:
            print(f"Trial type value '6' already contained in events file. Skipping modification for {os.path.basename(eventspath)}")
            return None
    else:
        return None


def ds000002(eventspath: str, task: str):
    """
    Process event data for ds000002 by modifying trial types if applicable. 
    Per DOI: 10.1016/j.neuroimage.2005.08.010, 'PCL trials alone were modeled ...  A nuisance regressor was added, 
    which consisted of trials on which no response was made.'
    
    Parameters:
    eventspath (str): path to the events .tsv file
    task (str): task name for dataset (regulate, learning, training, prelearning)
    
    Returns:
    modified events files
    """

    if task in ["deterministicclassification", "mixedeventrelatedprobe", "probabilisticclassification"]:
        eventsdat = pd.read_csv(eventspath, sep='\t')

        if "missed" in eventsdat['trial_type'].values or eventsdat['trial_type'].isna().any():
            # dropping unclear NaN values -- rest blocks?
            eventsdat = eventsdat.dropna(subset=['duration', 'trial_type'])

            # A nuisance regressor was added, which consisted of trials on which no response was made 
            # setting as trial_type == 'missed'. Will convolve and include as nuisance
            eventsdat.loc[eventsdat['response_time'].isna(), 'trial_type'] = 'missed'
            return eventsdat_cpy

        else:
            print(f"Trial type value 'missed' already contained in events file. Skipping modification for {os.path.basename(eventspath)}")
            return None

def ds000102(eventspath: str, task: str):
    """
    Process event data for ds000102: adding rt regressor. 

    Parameters:
    eventspath (str): path to the events .tsv file
    task (str): task name for dataset (regulate, learning, training, prelearning)
    
    Returns:
    modified events files
    """

    if task in ["flanker"]:
        eventsdat = pd.read_csv(eventspath, sep='\t')

        if "rt_reg" not in eventsdat['trial_type'].values:
            # create rt regressor

            # RT appears important, adding RT 'rt_reg' into trial_type column. Missed is included, set to 0 by func since NaN
            # include 'rt_reg' in spec file
            eventsdat_cpy = eventsdat.copy()
            cols_rt = ['congruent_correct', 'incongruent_incorrect', 'incongruent_correct', 'congruent_incorrect'] 
            eventsdat_cpy = add_reactiontime_regressor(eventsdf=eventsdat_cpy, trial_type_col='trial_type', resp_trialtype = cols_rt, 
            response_colname = 'response_time', rtreg_name ='rt_reg', resp_in_ms = False)
            
            # Sort by 'onset' column from low to high
            eventsdat_cpy = eventsdat_cpy.sort_values(by='onset', ascending=True)
            return eventsdat_cpy

        else:
            print(f"Trial type value 'missed' already contained in events file. Skipping modification for {os.path.basename(eventspath)}")
            return None



def ds000109(eventspath: str, task: str):
    """
    Process event data for ds000109 by modifying trial types if applicable. 
    Per DOI: 10.1523/JNEUROSCI.5511-11.2012, Dropping NaN in timing columns that are incorrect
    
    Parameters:
    eventspath (str): path to the events .tsv file
    task (str): task name for dataset (regulate, learning, training, prelearning)
    
    Returns:
    modified events files
    """

    if task in ["theoryofmindwithmanualresponse"]:
        eventsdat = pd.read_csv(eventspath, sep='\t')

        # Check if there are any NAs in the specified columns or trial_type has spaces
        if eventsdat[['onset', 'duration', 'trial_type']].isna().any().any() or eventsdat['trial_type'].str.contains(r'\s', na=False).any():
            print("**NaN dropped and trial_type spaces removed**")
            # Only run this if there are NAs in those columns
            eventsdat_cpy = eventsdat.dropna(subset=['onset', 'duration', 'trial_type'])
            eventsdat_cpy.loc[:, 'trial_type'] = eventsdat_cpy['trial_type'].str.replace(' ', '')

            return eventsdat_cpy
        else:
            print("No NaNs found in the specified columns. Skipping modification.")
            return None


def ds000115(eventspath: str, task: str):
    """
    Process event data for ds000115 by modifying trial types if applicable. 
    Modifying to not use '-' in python column names. Do not use '_' to replace as that is a parsing value in PyBIDS
    Parameters:
    eventspath (str): path to the events .tsv file
    task (str): task name for dataset (regulate, learning, training, prelearning)
    
    Returns:
    modified events files
    """

    if task in ["letter0backtask", "letter1backtask", "letter2backtask"]:
        eventsdat = pd.read_csv(eventspath, sep='\t')

        # Check if there are hyphens or whitespace in 'trial_type'
        if eventsdat['trial_type'].astype(str).str.contains(r'[-\s]', na=False).any():
            print("Cleaning 'trial_type' values: removing hyphens and spaces")
            # remove hyphens and whitespace from 'trial_type'
            eventsdat.loc[:, 'trial_type'] = eventsdat['trial_type'].str.replace(r'[-\s]', '', regex=True)
            return eventsdat

        else:
            print("No NaNs found in the specified columns. Skipping modification.")
            return None