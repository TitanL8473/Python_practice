# Python_practice

2026 年 10 月起，系统补 Python 的学习记录，以及第一个分析项目。

**背景**：交通运输工程专业硕士，研究方向为 **裂缝病害的大数据采集与分析**。
**目标**：把科研数据变成真正能跑的工具，逐步走向智慧交通 / 基础设施数字化方向。

> **关于本文档**：GitHub 文件列表右边那列显示的是「该文件最后一次被哪个提交改动」，
> 由 Git 自动生成、**无法自定义**，所以它不能说明文件内容。
> **想知道每个文件讲了什么，看下面这张知识点表。**

---

## 项目：crack_report —— 裂缝病害台账分析工具

把一份带脏数据的隧道裂缝巡检台账，清洗成可信数据，再算出病害分布与**裂缝发展速率**。

| 环节 | 内容 |
|---|---|
| 输入 | 3 座隧道、120 条裂缝巡检记录（12 个字段） |
| 清洗 | 列校验 → 类型转换 → 去空值 → 去重 → 排序（120 → 116 条） |
| 分析 | 按等级/构件分组统计、发展速率（mm/年）、养护优先级 |
| 输出 | 统计表 + 分布图（`output/`） |

```bash
cd crack_report
python main.py
```

```
crack_report/
├── data/raw/            原始数据（只读，绝不写入）
├── output/              所有结果写这里
├── src/
│   ├── loader.py        数据加载与清洗
│   └── analysis.py      统计分析
└── main.py              入口
```

**用到的技术点**：包结构（`__init__.py`）、模块拆分与 import、`pd.to_numeric(errors="coerce")`、
`dropna(subset=...)`、`drop_duplicates`、`groupby` + 命名聚合、`pd.to_datetime`、时间差计算。

> 状态：Day 13 完成数据清洗模块（`loader.py`），Day 14 起做分析模块。

---

## 学习记录（Day 01 – 13）

### 基础语法

| 文件 | 涉及的知识点 |
|---|---|
| `day01.py` | 函数 `return` 的位置（必须在 `for` 循环**外面**）、字符串 `.lower()` 做大小写归一、不要用 `sum` 当变量名（会覆盖内置函数） |
| `day02.py` | 字典 `.items()` 取键值对（**必须加括号**）、`return` 写在循环里的坑（第一次循环就返回）、函数封装 |
| `day03.py` | 方法 vs 函数：`char.lower` 是**方法对象**，必须 `char.lower()` 才是调用结果、字符串处理 |
| `day04.py` | `with open(...) as f` 读文件、`encoding="utf-8"`、用 `len()` 数行数、同目录相对路径 |
| `day05.py` | `split()` 的默认行为（按任意空白切分、自动忽略连续空白）、内置函数与运算符优先级、代码卫生 |

### 模块与工具

| 文件 | 涉及的知识点 |
|---|---|
| `day06_mytools.py` | 自己写模块：把函数放进独立文件，供别处复用 |
| `day06_main.py` | `import day06_mytools` 与 `from day06_mytools import count_vowels` 两种导入方式 |
| `day07.py` | Git 三个区（工作区 / 暂存区 / 本地仓库）、`add` 是「挑出哪些改动」、`commit` 是「按下快门存档」 |
| `day08.py` | `pathlib.Path`、`Path(__file__).resolve().parent` 定位脚本目录、`.name` / `.suffix`、`glob()` 遍历文件、列表推导式 |

### 数据处理

| 文件 | 涉及的知识点 |
|---|---|
| `day09.py` | `json.load(f)` 读 json、`csv.DictReader` 把每行读成字典、`to_string()` 防止列被省略、按字段分组统计 |
| `day10.py` | `np.array`、`shape` / `dtype`、整体运算（`arr * 2`）、`mean/max/min/std`、布尔索引 `arr[arr > 0.8]` |
| `day11.py` | `pd.read_csv`、条件筛行 `df[df["列"] > 值]`、`groupby` + `agg` 命名聚合、`reset_index()`、`to_csv(index=False)` |
| `day12.py` | matplotlib 画图、`agg` 后端设置、`plot` 的 marker / linestyle / color、中文字体 `rcParams`、`savefig(dpi, bbox_inches)` |

### 项目笔记

| 文件 | 涉及的知识点 |
|---|---|
| `day13.py` | **18 条学习笔记**：`__init__.py` 让文件夹成为包、`REQUIRED_COLUMNS` / `NUMERIC_COLUMNS` / `REQUIRED_NOT_NULL` 三者分工、`pd.to_numeric(errors="coerce")` 的 coerce、`dropna(subset=)` 与 `dropna()` 的区别、`if __name__ == "__main__"`、列表推导式 |

---

## 其他

| 文件 / 目录 | 内容 |
|---|---|
| `sample_data/` | 示例数据：隧道地震响应监测（`tunnel_response.csv` / `params.json`）、裂缝病害台账（`crack_inventory.csv`）、故意做坏的样例（`_bad_example.csv`） |
| `day12_figure/` | Day 12 生成的分析图 |
| `git推送速查.md` | Git 日常命令、三步推送流程、9 条常见报错排错 |
| `data.txt` | 早期练习用的示例文本 |

---

## 环境

- Python 3.13
- numpy / pandas / matplotlib

```bash
pip install numpy pandas matplotlib
```

---

## 说明

代码不追求优雅，追求**能讲清楚每一行在干什么**。
每个文件开头都有 `# 我学到了` 的笔记，记录当天真正想明白的东西。
