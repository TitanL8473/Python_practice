#我学到了
#1.属性（查看不用通过比较就可以得到的信息，不加括号）；方法（执行计算，要加括号 `()`
#2.np.array()创建数组
#3. - `data[n]`：取第 n 行，`data[:, n]`：取全部行，第 n 列
#4.return 多个变量：会返回元组
#5.`round(a,b) 只能对单个数字使用，表示a取b位小数
#6. tr=np.loadtxt(file, delimiter=',', skiprows=1, usecols=(1,2,3))，读取文本文件（csv、txt），直接加载成 numpy 二维数组
#7. `delimiter=','`：分隔符，文件里数字是**逗号隔开**（csv 文件）
#8.. `skiprows=1`：**跳过第 1 行**。csv 第一行一般是表头（文字标题，不是数字），不能读，所以跳过。写 skiprows=2 就会跳过前两行。
#9. `usecols=(1,2,3)`：**只读取第 1、2、3 列**（列从 0 开始编号！），其他列直接忽略，只把这 3 列装进数组
import numpy as np
from pathlib import Path

HERE=Path(__file__).resolve().parent
DATA=HERE/'day9_data'
csv_path=DATA/'tunnel_response.csv'
json_path=DATA/'params.json'

pga_list=[0.42, 0.51, 0.63, 0.78, 0.91, 1.05, 0.96, 0.82, 0.68, 0.55, 0.44]
pga=np.array(pga_list)

print(pga)
print(pga.shape)
print(pga.dtype)
print(len(pga))
print(pga*100)
print(pga.mean())
print(pga.max())
print(pga.min())
print(round(pga.std(),2))
print(pga[pga>0.8])

def load_columns(file):
    tr=np.loadtxt(file,delimiter=',',skiprows=1,usecols=(1,2,3))
    return tr

response=load_columns(csv_path)
print(response)
print(response.shape)
print(response.dtype)

def stats(data):
    points=len(data)
    most_pga=data[:,1].max()
    average_motion=round(data[:,2].mean(),1)
    high_data=len(data[data[:,1]>0.8])
    high_data_average_motion=round((data[data[:,1]>0.8])[:,2].mean(),2)
    result={
        '测点数':points,
        "最高PGA": most_pga,
        "平均位移mm": average_motion,
        "高PGA测点数": high_data,
        "高PGA平均位移": high_data_average_motion
    }
    return result

print(stats(response))
