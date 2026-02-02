import pandas as pd
import os

def load_raw_data(main_path="../data/raw/ethiopia_fi_unified_data.csv",
                  impact_path="../data/raw/Impact_sheet.csv"):
    """
    Load the Ethiopia FI dataset from CSVs.
    Returns a tuple: (main_data_df, impact_links_df)

    Raises:
        FileNotFoundError: if either file does not exist
        ValueError: if required columns are missing
    """
    # -----------------------------
    # 1. Check file existence
    # -----------------------------
    for file_path in [main_path, impact_path]:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

    # -----------------------------
    # 2. Load CSV files
    # -----------------------------
    try:
        main_df = pd.read_csv(main_path)
        impact_df = pd.read_csv(impact_path)
    except Exception as e:
        raise IOError(f"Error reading CSV files: {e}")

    # -----------------------------
    # 3. Validate required columns
    # -----------------------------
    required_main_cols = ['record_id', 'record_type', 'indicator_code', 'observation_date']
    required_impact_cols = ['record_id', 'related_indicator', 'impact_direction']

    missing_main = [c for c in required_main_cols if c not in main_df.columns]
    missing_impact = [c for c in required_impact_cols if c not in impact_df.columns]

    if missing_main:
        raise ValueError(f"Missing required columns in main data: {missing_main}")
    if missing_impact:
        raise ValueError(f"Missing required columns in impact links: {missing_impact}")

    # -----------------------------
    # 4. Convert dates
    # -----------------------------
    for df in [main_df, impact_df]:
        if 'observation_date' in df.columns:
            df['observation_date'] = pd.to_datetime(df['observation_date'], errors='coerce')

    return main_df, impact_df


def load_reference_codes(path="../data/raw/reference_codes.xlsx"):
    """
    Load reference codes from Excel.

    Raises:
        FileNotFoundError: if file does not exist
        ValueError: if file is empty
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"Reference codes file not found: {path}")

    try:
        df = pd.read_excel(path)
    except Exception as e:
        raise IOError(f"Error reading reference codes Excel: {e}")

    if df.empty:
        raise ValueError(f"Reference codes file is empty: {path}")

    return df
