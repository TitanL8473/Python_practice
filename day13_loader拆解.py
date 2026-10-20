# Day 13 · loader.py 逐步拆解（单文件，可直接运行）
#
# 目的：让你【亲眼看到】每个函数在做什么，再自己组装成 src/loader.py
#
# 运行：  python day13_loader拆解.py     （在 202610安排 里跑）
#
# 顺序：6 个小步，每步都有输出，看完你就懂了。

import pandas as pd
from pathlib import Path

HERE = Path(__file__).resolve().parent
CSV = HERE / "day9_data" / "crack_inventory.csv"


# ============================================================
# 第 1 步 · load_raw —— 原样读进来，先看看它有多"脏"
# ============================================================
print("=" * 60)
print("第 1 步 · load_raw：原样读进来")
print("=" * 60)

df_raw = pd.read_csv(CSV)

print("形状 :", df_raw.shape)
print("width_mm 的类型 :", df_raw["width_mm"].dtype, "  ← 注意！不是 float64")
print()
print("问题在哪：")
print(df_raw["width_mm"].head(8).to_string())
print()
print("→ 因为有一条写的是文字「未测」，pandas 把【整列】都当字符串处理了。")
print("→ 所以检查一下：有多少个不是数字？")
print(df_raw["width_mm"].isna().sum(), "个是空的（读进来就是 NaN）")


# ============================================================
# 第 2 步 · check_columns —— 缺列就当场喊停
# ============================================================
print()
print("=" * 60)
print("第 2 步 · check_columns：缺列就 raise")
print("=" * 60)

REQUIRED_COLUMNS = [
    "crack_id", "tunnel", "mileage_m", "component", "crack_type",
    "length_mm", "width_mm", "depth_mm", "grade", "found_date",
]

# 先演示用：正常数据应该通过
missing = [c for c in REQUIRED_COLUMNS if c not in df_raw.columns]
print("缺的列：", missing, " ← 空列表 = 都齐了，没问题")

# 再故意造一个缺列的，看它怎么拦
bad = df_raw.drop(columns=["grade"])
missing2 = [c for c in REQUIRED_COLUMNS if c not in bad.columns]
print("故意删掉 grade 后，缺的列：", missing2)
try:
    if missing2:
        raise ValueError(f"数据缺少必需的列：{missing2}")
except ValueError as ex:
    print("✅ 成功拦截：", ex)
print()
print("→ 这一行 list 推导式在干嘛：遍历 REQUIRED_COLUMNS，把【不在 df.columns 里】的挑出来。")
print("   [c for c in 清单 if c not in df.columns]  ← 就是 Day 2 学的列表推导式")


# ============================================================
# 第 3 步 · to_numeric —— 把「未测」变成 NaN
# ============================================================
print()
print("=" * 60)
print("第 3 步 · pd.to_numeric(errors='coerce')")
print("=" * 60)

df = df_raw.copy()
print("转换前 width_mm 类型 :", df["width_mm"].dtype)

df["width_mm"] = pd.to_numeric(df["width_mm"], errors="coerce")

print("转换后 width_mm 类型 :", df["width_mm"].dtype, " ← 变 float64 了")
print("转换后空值个数       :", df["width_mm"].isna().sum(), " ← 空的 + 未测 都变成 NaN")
print()
print("→ errors='coerce' 的意思是：「转不动的，别报错，给我变成 NaN」。")
print("   如果不加这个参数，遇到「未测」会直接崩：")
try:
    pd.to_numeric(df_raw["width_mm"])
except ValueError as ex:
    print("   💥", str(ex)[:80], "...")


# ============================================================
# 第 4 步 · ★ dropna(subset=) vs dropna() —— 今天最重要的一步
# ============================================================
print()
print("=" * 60)
print("第 4 步 · ★ dropna 的两种删法，差别巨大")
print("=" * 60)

# 先把所有数字列都转了
NUMERIC_COLUMNS = ["mileage_m", "length_mm", "width_mm", "depth_mm", "recheck_width_mm"]
for col in NUMERIC_COLUMNS:
    df[col] = pd.to_numeric(df[col], errors="coerce")

print("现在总行数：", len(df))
print()

print("【错误做法】df.dropna()  —— 任何一列有空就删这行")
wrong = df.dropna()
print("   剩下：", len(wrong), "行    ← 复检列大面积是空的，全被删了！")

print()
print("【正确做法】df.dropna(subset=[只检查关键列])")
REQUIRED_NOT_NULL = ["mileage_m", "length_mm", "width_mm", "depth_mm", "grade"]
right = df.dropna(subset=REQUIRED_NOT_NULL)
print("   剩下：", len(right), "行    ← 只删了真正没法用的那 3 条")

print()
print("→ 为什么？因为「还没复检」是【合法状态】，不能因为复检列空就把整条记录扔掉。")
print("→ 哪些空能接受、哪些不能，是【业务判断】，不是技术判断。这是今天最值钱的一句。")


# ============================================================
# 第 5 步 · drop_duplicates —— 去掉重复的裂缝编号
# ============================================================
print()
print("=" * 60)
print("第 5 步 · drop_duplicates")
print("=" * 60)

print("去重前：", len(right), "行，crack_id 重复的有", right["crack_id"].duplicated().sum(), "条")
dedup = right.drop_duplicates(subset=["crack_id"], keep="first")
print("去重后：", len(dedup), "行，crack_id 重复的有", dedup["crack_id"].duplicated().sum(), "条")


# ============================================================
# 第 6 步 · 排序 + 重新编号
# ============================================================
print()
print("=" * 60)
print("第 6 步 · sort_values + reset_index")
print("=" * 60)

final = dedup.sort_values(["tunnel", "mileage_m"]).reset_index(drop=True)
print("最终：", final.shape[0], "行 ×", final.shape[1], "列")
print(final.head(3).to_string())
print()
print("→ reset_index(drop=True) 的作用：删行之后行号会断（0,1,5,9...），这一步重新从 0 排。")


# ============================================================
# 对照：这就是你要写的 loader.py（把上面 6 步装进函数）
# ============================================================
print()
print("=" * 60)
print("最终结果（你要达到的就是这个）")
print("=" * 60)
print(f"形状：{final.shape[0]} 行 × {final.shape[1]} 列       ← 期望 116 行 × 12 列")
print(f"width_mm 类型：{final['width_mm'].dtype}              ← 期望 float64")
print(f"crack_id 重复：{final['crack_id'].duplicated().sum()}                       ← 期望 0")
print("隧道分布：")
print(final["tunnel"].value_counts().to_string())
print("→ 期望：白鹤岭 43 / 凤凰山 38 / 狮子山 35")


# ============================================================
# 现在，把它变成 src/loader.py 里的 4 个函数
# ============================================================
# 上面 6 步其实是这样的分工：
#
#   第 1 步          →  def load_raw(path)
#   第 2 步          →  def check_columns(df)
#   第 3、4、5、6 步 →  def clean(df)          ← 里面按顺序调这四步
#   全部串起来        →  def load(path)
#
# 照着上面的代码，一段一段搬进函数里就行 —— 逻辑你已经全看过了。
