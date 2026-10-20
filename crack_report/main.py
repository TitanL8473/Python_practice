from pathlib import Path

from src.loader import load

HERE = Path(__file__).resolve().parent
DATA = HERE / "data" / "raw" / "crack_inventory.csv"

if __name__ == "__main__":
    df = load(DATA)

    print("=" * 56)
    print("裂缝病害台账加载成功")
    print("=" * 56)
    print(f"形状：{df.shape[0]} 行 × {df.shape[1]} 列")
    print(f"列名：{list(df.columns)}")
    print()
    print("前 3 行：")
    print(df.head(3).to_string())
    print()
    print("各列类型：")
    print(df.dtypes.to_string())
    print()
    print("隧道分布：")
    print(df["tunnel"].value_counts().to_string())
    print()
    print("病害等级分布：")
    print(df["grade"].value_counts().to_string())
    print()
    print(f"裂缝宽度范围：{df['width_mm'].min():.2f} ~ {df['width_mm'].max():.2f} mm")
    print(f"有复检记录的：{df['recheck_width_mm'].notna().sum()} / {len(df)} 条")
