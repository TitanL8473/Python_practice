#我学到了：
#1.使用`json.load(f)`，读取硬盘上的 json 文件，直接转成 Python 字典
#2.`csv.DictReader`读取 csv，**每一行变成字典 row**，所有读取出来的值默认都是字符串
#3.`newline=''`：csv 读取专用，防止 Windows 出现多余空行
#4.`max(列表, key=lambda p:p['pga_g'])`：按 pga_g 找最大值对应的那一条测点数据
#5.- save_summary(summary, path) `summary`：你前面`stats`返回的**字典**， `path`：保存的文件路径
#6.json.dump(summary, f, indent=4, ensure_ascii=False)，`json.dump(字典, 文件对象)`：把 python 字典写入 json 文件
#7. `indent=4`：换行 + 缩进 4 空格，文件内容好看，不是挤成一行
#8.`ensure_ascii=False`：中文直接保存，不会变成`\uXXXX`编码
#9.def save_damage_csv(counts, path):文件存为csv文件
#10. `fieldnames = ["damage_level", "count"]`：定义表头两列名字
#11.`writer.writeheader()`：**写入表头第一行**
#12.`writer.writerow(字典)`：循环写每一行数据
#13.writer = csv.DictWriter(f, fieldnames=fieldnames)   【创建工具，只是做配置】
import csv
import json
from pathlib import Path
HERE=Path(__file__).resolve().parent
DATA=HERE/"day9_data"

def load_params(name):
    with open(DATA/name,encoding='utf-8') as f:
        params=json.load(f)
    return params

print(load_params('params.json'))

def load_points(name):
    with open(DATA/name,encoding='utf-8',newline='') as f:
        rows=list(csv.DictReader(f))

    points=[]
    for row in rows:
        points.append({
            'point_id':row['point_id'],
             'distance_m':float(row['distance_m']),
            'pga_g':float(row['pga_g']),
            'disp_mm':float(row['disp_mm']),
            'damage_level':row['damage_level'],
        })
    return points

print(load_points('tunnel_response.csv'))

def summarize(points):
    result={}
    result['测点数']=len(points)
    top=max(points,key=lambda p:p['pga_g'])
    result['最高pga测点']=top['point_id']
    result['最高pga']=top['pga_g']
    result['平均位移mm']=round(sum(p['disp_mm'] for p in points)/len(points),1)

    counts={}
    for p in points:
        level=p['damage_level']
        counts[level]=counts.get(level,0)+1
    result['损伤等级统计']=counts
    return result

print(summarize(load_points('tunnel_response.csv')))

def save_summary(summary, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=4, ensure_ascii=False)
    return path

def save_damage_csv(counts, path):
    fieldnames = ["damage_level", "count"]
    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for level, num in counts.items():
            writer.writerow({"damage_level": level, "count": num})
    return path

