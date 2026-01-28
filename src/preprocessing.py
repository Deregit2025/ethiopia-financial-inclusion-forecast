import pandas as pd
import numpy as np

def clean_fi_data(df):
    """
    Basic preprocessing for Ethiopia FI dataset.
    - Drops rows without observation_date
    - Fills missing pillar values with 'unknown'
    - Converts value_numeric to float
    """
    # Drop rows missing observation_date
    df = df.dropna(subset=['observation_date'])
    
    # Fill missing pillar
    if 'pillar' in df.columns:
        df['pillar'] = df['pillar'].fillna('unknown')
    
    # Ensure numeric columns
    if 'value_numeric' in df.columns:
        df['value_numeric'] = pd.to_numeric(df['value_numeric'], errors='coerce')
    
    # Optional: fill other missing categorical columns
    for col in ['record_type', 'indicator_code', 'category', 'source_name']:
        if col in df.columns:
            df[col] = df[col].fillna('unknown')
    
    return df

def add_growth_rate(df, indicator_code):
    """
    Add simple year-on-year growth rate for an indicator.
    Creates a new column 'growth_rate' for that indicator.
    """
    sub = df[df['indicator_code'] == indicator_code].sort_values('observation_date')
    sub['growth_rate'] = sub['value_numeric'].pct_change() * 100
    df.loc[sub.index, 'growth_rate'] = sub['growth_rate']
    return df
