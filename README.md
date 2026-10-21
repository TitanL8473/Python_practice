# Python_practice

2026 年 10 月起，系统补 Python 的学习记录，以及第一个分析项目。

**背景**：交通运输工程专业硕士，研究方向为 **裂缝病害的大数据采集与分析**。
**目标**：把科研数据变成真正能跑的工具，逐步走向智慧交通 / 基础设施数字化方向。

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

> 状态：Day 13 完成数据清洗模块（`loader.py`），Day 14 起做分析模块。

---

## 学习记录（Day 1 – 13）

| 文件 | 主题 |
|---|---|
| `day1.py` | 重启：函数、返回值、字典基础 |
| `day2.py` | 字典遍历与函数封装 |
| `day3.py` | 类与对象 |
| `day4.py` | 异常处理（try / except） |
| `day5.py` | 代码卫生：命名、返回值、运算符优先级 |
| `day6_main.py` / `day6_mytools.py` | 模块化：自己写模块并 import |
| `day7.py` | Git 与版本控制（实践笔记） |
| `day8.py` | pathlib：路径处理、文件夹遍历 |
| `day9.py` | json / csv 读写 |
| `day10.py` | numpy：数组与整体运算 |
| `day11.py` | pandas：表格、筛选、groupby 分组统计 |
| `day12.py` | matplotlib：把数据画成图 |
| `day13.py` | **学习笔记**：包结构、loader 设计、列表推导式 |

每个文件开头都有 `# 我学到了` 的笔记，记录当天真正想明白的东西。

---

## 其他

| 文件 / 目录 | 内容 |
|---|---|
| `day9_data/` | 示例数据：隧道地震响应监测、裂缝病害台账 |
| `day12_figure/` | Day 12 生成的分析图 |
| `git推送速查.md` | Git 日常命令与常见报错排错 |

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
