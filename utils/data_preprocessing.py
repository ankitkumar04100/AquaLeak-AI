import pandas as pd

def preprocess_data(df):
    """
    Preprocess water usage data for model input.
    Handles missing values, scaling, and feature selection.
    """
    # Example: Fill missing values with mean
    df = df.fillna(df.mean())

    # Optional: select only numeric columns for model
    numeric_cols = df.select_dtypes(include='number').columns
    df = df[numeric_cols]

    return df
