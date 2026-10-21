#我学到了
#1.pandas处理**带表头的表格文件（csv/excel）**
#2.pd.read_csv是 pandas 的函数：读取 csv 文件，把文件内容读成 DataFrame（pandas 表格）
#3.name['pga_g']，pd读出的文件可以直接通过表头来引用数据、
#4.sort_values('pga_g',ascending=False).head(3)引用pga_g的数据,按照降序，打印前三行
#5.groupby('damage_level').agg().reset_index()`groupby('列名')`：**分组**。把整张表格，按照`damage_level`（损伤等级）分成多组，相同损伤等级的行归到一组
#6.agg 里面格式：`新列名 = ('原始列名', 统计函数)`
#7.lambda x:round(x.mean(),1)中`lambda x: ...`：匿名函数，自定义计算逻辑
#8.`reset_index()`：把索引还原成普通列，输出的表格结构更规整，方便后续保存 csv
#9.to_csv(path, index=False, encoding='utf-8-sig')中`to_csv()`：pandas 的**写文件**方法，和`read_csv()`是一对
#10.`index=False`：**不要把 pandas 自动生成的行索引（0,1,2…）写入 csv**。如果写 True，导出 csv 会多出一列无意义的序号。
#11.`encoding='utf-8-sig'`：编码格式。**解决 Excel 打开 csv 中文乱码**，Windows 下推荐这个编码；普通 utf-8 在 Excel 打开中文容易乱码。
import pandas as pd
from pathlib import Path
HERE=Path(__file__).resolve().parent
DATA=HERE/'sample_data'
json_data=DATA/'params.json'
csv_data=DATA/'tunnel_response.csv'

'''print("=" * 56)
print("第 0 步 · 读成表格")
print("=" * 56)

df=pd.read_csv(csv_data)

print(df.head(3))
print(df.shape)
print(list(df.columns))
print(df.dtypes)
print(df['pga_g'])
print(df['pga_g'].max())
print(df['pga_g']>0.8)
print(df[df['pga_g']>0.8])
print(len(df[df['pga_g']>0.8]))
print(df.sort_values('pga_g',ascending=False).head(3))'''

def load_table(path):
    result=pd.read_csv(path)
    return result

tr=load_table(csv_data)
print(tr)

def strong_data(name):
    result=name[name['pga_g']>0.8]
    return result

print(strong_data(tr))

def damage_summary(name):
    result=name.groupby('damage_level').agg(
        测点数=('point_id','count'),
        平均位移mm=('disp_mm',lambda x:round(x.mean(),1))
    ).reset_index()
    return result

print(damage_summary(tr))

def save_table(table,path):
    table.to_csv(path,index=False,encoding='utf-8-sig')
    return path

print(save_table(damage_summary(tr),DATA/'day11汇总文件.csv'))
