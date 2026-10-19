# 我学到了
# 1.
import matplotlib

matplotlib.use("agg")
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False
HERE = Path(__file__).resolve().parent
DATA = HERE / 'day9_data'
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

