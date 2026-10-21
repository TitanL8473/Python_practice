import pandas as  pd

REQUIRED_COLUMNS=["crack_id", "tunnel", "mileage_m", "component", "crack_type",
                  "length_mm", "width_mm", "depth_mm", "grade", "found_date",]
NUMERIC_COLUMNS = ["mileage_m", "length_mm", "width_mm", "depth_mm", "recheck_width_mm"]
REQUIRED_NOT_NULL = ["mileage_m", "length_mm", "width_mm", "depth_mm", "grade"]

def load_raw(path):
    return pd.read_csv(path)

def check_columns(data):
    missing=[c for c in REQUIRED_COLUMNS if c not in data.columns]
    if missing:
        raise ValueError(f"缺少必须的列{missing}")

def clean(data):
    check_columns(data)
    for col in NUMERIC_COLUMNS:
        if col in data.columns:
            data[col]=pd.to_numeric(data[col],errors="coerce")
    data=data.dropna(subset=REQUIRED_NOT_NULL)
    data=data.drop_duplicates(subset=["crack_id"],keep="first")
    data=data.sort_values(["tunnel","mileage_m"]).reset_index(drop=True)
    return data

def load(path):
    result=load_raw(path)
    result=clean(result)
    return result
