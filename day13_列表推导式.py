# 看懂这一行：
#     missing = [c for c in REQUIRED_COLUMNS if c not in df.columns]
#
# 它 = for 循环 + if 判断 + append，压成一行。

REQUIRED = ["crack_id", "tunnel", "mileage_m", "grade"]


# ============================================================
# 第 1 步 · 先搞懂 not in
# ============================================================
print("=" * 50)
print("第 1 步 · in 和 not in")
print("=" * 50)

have = ["crack_id", "tunnel", "width_mm"]

print('"crack_id" in  have :', "crack_id" in have)       # True  有
print('"grade"    in  have :', "grade" in have)          # False 没有
print()
print('"grade"    not in have :', "grade" not in have)   # True  没有 → not in 就是 True
print('"crack_id" not in have :', "crack_id" not in have)  # False 有 → not in 就是 False
print()
print("→ in 问「在不在」，not in 就是反过来的答案。")


# ============================================================
# 第 2 步 · 普通写法（先看懂这个）
# ============================================================
print()
print("=" * 50)
print("第 2 步 · 用 for 循环写一遍")
print("=" * 50)

def check_loop(required, have):
    missing = []                    # 准备一个空篮子
    for c in required:              # 把要求的列一个个拿出来
        if c not in have:           # 如果这个列【不在】现有的里
            missing.append(c)       # 就丢进篮子
    return missing                  # 交篮子

print("全都有    :", check_loop(REQUIRED, ["crack_id", "tunnel", "mileage_m", "grade", "width_mm"]))
print("少了 grade:", check_loop(REQUIRED, ["crack_id", "tunnel", "mileage_m"]))
print("只剩一个  :", check_loop(REQUIRED, ["crack_id"]))


# ============================================================
# 第 3 步 · 同一件事，列表推导式（一行版）
# ============================================================
print()
print("=" * 50)
print("第 3 步 · 压缩成一行")
print("=" * 50)

def check_comprehension(required, have):
    return [c for c in required if c not in have]
    #      ↑    ↑                ↑
    #   装什么  从哪拿          什么条件下才装

print("全都有    :", check_comprehension(REQUIRED, ["crack_id", "tunnel", "mileage_m", "grade", "width_mm"]))
print("少了 grade:", check_comprehension(REQUIRED, ["crack_id", "tunnel", "mileage_m"]))
print("只剩一个  :", check_comprehension(REQUIRED, ["crack_id"]))


# ============================================================
# 第 4 步 · 对照表（记住这张）
# ============================================================
print()
print("=" * 50)
print("第 4 步 · 一一对应")
print("=" * 50)
print("""
  普通写法                          列表推导式
  ─────────────────────────────    ────────────────────────────────
  missing = []                     [
  for c in required:                 c                  ← 装什么
      if c not in have:              for c in required  ← 从哪拿
          missing.append(c)          if c not in have   ← 什么条件下才装
  return missing                   ]

  所以：
      [  要装的东西   for 变量 in 一堆东西   if 条件  ]
       ↑                                    ↑
     没有 if 就是全部都要                    加了 if 就是筛
""")

print("换句话说，这个式子读作：")
print("  「把 required 里每一个 c 拿出来，只要 c 不在 have 里，就把 c 装进列表」")
