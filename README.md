# Python_practice

从 2026 年 10 月开始，系统补 Python 的学习记录。

背景：交通运输工程专业硕士，研究方向为隧道抗震与损伤分析。
目标是把手上的科研数据变成「能用代码处理的东西」，逐步走向
智慧交通 / CAE 工业软件方向。

**每天一个文件，记录当天的练习与心得。**

## 目录

| 文件                                 | 主题                          |
|------------------------------------|-----------------------------|
| `day1.py`                          | 重启：函数、类、字典基础                |
| `day2.py`                          | 字典遍历与函数封装                   |
| `day3.py`                          | 类与对象                        |
| `day4.py`                          | 异常处理（try / except）          |
| `day5.py`                          | 代码卫生：命名、返回值、运算符优先级          |
| `day6_main.py` / `day6_mytools.py` | 模块化：自己写模块并 import           |
| `day7.py`                          | Git 与版本控制（实践记录）             |
| `day8.py`                          | pathlib：遍历文件夹、路径处理          |
| `day9.py`                          | json / csv 读写（隧道地震响应监测数据示例） |
| `day10.py`                         | numpy：数组与整体运算               |
| `day11.py`                         | pandas：表格、筛选、groupby 分组统计   |
| `day12.py`                         | matplotlib:画图               |
| day13.py                           | 项目框架搭建                      |

## 示例数据

`day9_data/` 下是一份隧道衬砌地震响应监测的示例数据：

- `tunnel_response.csv` —— 11 个测点的 PGA、位移、损伤等级
- `params.json` —— 仿真参数配置（嵌套结构）

用于练习 csv / json / numpy / pandas 的读写与分析。

## 环境

- Python 3.13
- numpy、pandas

```bash
pip install numpy pandas matplotlib
```

## 说明

每个文件开头都有 `# 我学到了` 的笔记，记录当天真正想明白的东西。
代码不追求优雅，追求「自己能讲清楚每一行在干什么」。
