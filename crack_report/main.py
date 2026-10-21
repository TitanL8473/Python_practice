from pathlib import Path
from src.loader import load

HERE = Path(__file__).resolve().parent
DATA = HERE / "data" / "raw" / "crack_inventory.csv"

if __name__=="__main__":
    df=load(DATA)
    print(f"{df.shape}")
    print(df.head(3))
    print(df.head(3).to_string)
    print(df.dtypes)
    print(df.dtypes.to_string)
    print(df["tunnel"])
    print(df["tunnel"].value_counts())
