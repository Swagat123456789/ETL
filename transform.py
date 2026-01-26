def transform_data(df):
    """
    Transform data:
    - Convert name column to uppercase
    """
    df = df.copy()
    df.columns=df.columns.str.strip().str.lower()
    if "name" not in df.columns:
        raise KeyError(f"'name' column not found. Available columns: {df.columns.tolist()}")

    df["name"] = df["name"].str.upper()
    return df
