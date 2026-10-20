import pandas as pd

REQUIRED_COLUMNS = [
    "crack_id", "tunnel", "mileage_m", "component", "crack_type",
    "length_mm", "width_mm", "depth_mm", "grade", "found_date",
]

NUMERIC_COLUMNS = ["mileage_m", "length_mm", "width_mm", "depth_mm", "recheck_width_mm"]

REQUIRED_NOT_NULL = ["mileage_m", "length_mm", "width_mm", "depth_mm", "grade"]

def load_raw(path):
    return pd.read_csv(path)

def check_columns(df):
    missing = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing:
        raise ValueError(f"数据缺少必需的列：{missing}")
    return True

def clean(df):
    check_columns(df)

    for col in NUMERIC_COLUMNS:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    df = df.dropna(subset=REQUIRED_NOT_NULL)
    df = df.drop_duplicates(subset=["crack_id"], keep="first")
    df = df.sort_values(["tunnel", "mileage_m"]).reset_index(drop=True)
    return df


def load(path):
    df = load_raw(path)
    df = clean(df)
    return df
