# 我学到了
#1matplotlib.use ("agg") #matplotlib 的 agg 后端设置，顺序很关键。必须先导入 matplotlib，再设置 use ("agg")，最后导入 pyplot
#2.plt.plot 绘制折线图。marker 设置点标记，linestyle 线型，color 线条颜色，label 图例文字。plt.xlabel plt.ylabel 设置 x 轴 y 轴坐标轴名称
#3..plt.title 设置图表标题;plt.grid (True, alpha=0.3) 绘制网格线，alpha 控制透明度，数值越小越淡
#4.plt.tight_layout自动调整图布局，防止标题坐标轴文字被截断.plt.savefig 保存图片。dpi 是分辨率，数值越大图片越清晰；bbox_inches='tight' 裁掉图片四周多余白边
#5.plt.close关闭画布，释放内存。多次绘图必须写，防止多张图叠加、占用大量内存
#5.#plt.legend()：显示图例;图例就是图里的小说明框，用来解释图上不同线条或者柱子代表什么含义;图例的文字来自绘图函数里的label参数

import matplotlib

matplotlib.use("agg")
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False
HERE = Path(__file__).resolve().parent
DATA = HERE / 'sample_data'
csv = DATA / 'tunnel_response.csv'
DATA_figure=HERE/'day12_figure'

print("=" * 56)
print("第 0 步 · 第一张图")
print("=" * 56)

df = pd.read_csv(csv)
print(df)

def plot_decay(data):
    out1 = DATA_figure/'_图一_衰减曲线.png'
    plt.figure(figsize=(8, 5))
    plt.plot(data['distance_m'], data['pga_g'], marker='o', linestyle='-', color="#c0392b", label='实测PGA')
    plt.xlabel('距震中距离(m)')
    plt.ylabel('峰值加速度PGA(g)')
    plt.title('隧道衬砌地震响应沿纵向衰减')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(out1, dpi=300, bbox_inches='tight')
    plt.close()
    return out1

plot_decay(df)

def plot_damage(data):
    out2 = DATA_figure/'_图二_各隧道等级的衬砌平均位移柱形图.png'
    order = ['none', 'slight', 'moderate', 'severe']
    ave = data.groupby('damage_level')['disp_mm'].mean().round(2).reindex(order)
    print(ave)
    plt.figure(figsize=(8, 5))
    plt.bar(ave.index, ave.values, color='#b0762a')
    plt.xlabel('损伤等级')
    plt.ylabel('平均位移')
    plt.title('各隧道等级的衬砌平均位移柱形图')
    plt.savefig(out2, dpi=300, bbox_inches='tight')
    plt.close()
    return out2

plot_damage(df)

