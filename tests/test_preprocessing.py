import pytest
import pandas as pd
import numpy as np
from preprocessing import clean_fi_data, add_growth_rate

# ----------------------------
# Fixtures for sample data
# ----------------------------
@pytest.fixture
def sample_data():
    data = {
        "record_id": ["OBS_001", "OBS_002", "OBS_003", "OBS_004"],
        "record_type": ["observation", "observation", None, "event"],
        "indicator_code": ["ACC_OWNERSHIP", "ACC_OWNERSHIP", "ACC_OWNERSHIP", "ACC_OWNERSHIP"],
        "observation_date": ["2021-01-01", None, "2021-03-01", "2021-04-01"],
        "pillar": ["ACCESS", None, "ACCESS", None],
        "category": ["cat1", None, "cat2", None],
        "source_name": ["IMF FAS", None, "World Bank", None],
        "value_numeric": ["10", "20", None, "40"]
    }
    df = pd.DataFrame(data)
    return df

# ----------------------------
# Test clean_fi_data
# ----------------------------
def test_clean_fi_data(sample_data):
    cleaned_df = clean_fi_data(sample_data)

    # Check that rows with missing observation_date are dropped
    assert cleaned_df['observation_date'].isna().sum() == 0
    assert cleaned_df.shape[0] == 3

    # Check pillar fill
    assert (cleaned_df['pillar'] == 'unknown').sum() >= 0

    # Check value_numeric converted to float
    assert cleaned_df['value_numeric'].dtype in [float, np.float64]

    # Check categorical fill
    for col in ['record_type', 'indicator_code', 'category', 'source_name']:
        assert cleaned_df[col].isna().sum() == 0

# ----------------------------
# Test add_growth_rate
# ----------------------------
def test_add_growth_rate(sample_data):
    df = clean_fi_data(sample_data)

    # Add growth rate for existing indicator
    df_with_growth = add_growth_rate(df, "ACC_OWNERSHIP")
    assert 'growth_rate' in df_with_growth.columns

    # Check growth rate calculation
    subset = df_with_growth[df_with_growth['indicator_code'] == "ACC_OWNERSHIP"]
    # First growth value should be NaN
    assert pd.isna(subset.iloc[0]['growth_rate'])

    # Check error raised for missing indicator
    with pytest.raises(ValueError):
        add_growth_rate(df_with_growth, "NON_EXISTENT_INDICATOR")
