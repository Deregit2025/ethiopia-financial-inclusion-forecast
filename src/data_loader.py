import pandas as pd

def load_raw_data(path="../data/raw/ethiopia_fi_unified_data.xlsx"):
    """
    Load the Ethiopia FI unified dataset from XLSX.
    Assumes two sheets: 'ethiopia_fi_unified_data' and 'Impact_sheet'.
    Returns a tuple: (observations/events/targets df, impact_links df)
    """
    # Load main sheet
    data_df = pd.read_excel(path, sheet_name='ethiopia_fi_unified_data')
    
    # Load impact_links sheet
    impact_df = pd.read_excel(path, sheet_name='Impact_sheet')
    
    # Convert observation_date to datetime
    if 'observation_date' in data_df.columns:
        data_df['observation_date'] = pd.to_datetime(data_df['observation_date'], errors='coerce')
    
    if 'observation_date' in impact_df.columns:
        impact_df['observation_date'] = pd.to_datetime(impact_df['observation_date'], errors='coerce')
    
    return data_df, impact_df

def load_reference_codes(path="../data/raw/reference_codes.xlsx"):
    """Load reference codes from Excel"""
    return pd.read_excel(path)
