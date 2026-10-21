#我学到了
#1._init_.py的作用是告诉python当前所在文件夹为一个python包，里面的py文件可以被导入
#2.loader.py的作用是清洗原始数据，以便于进行后续操作
#2.REQUIRED_COLUMNS表示必须存在的列，少列直接报错
#3.NUMERIC_COLUMNS表示应该为数字的列，清洗时强制转数值，转失败（文字、空）就变成 NaN。
#4.REQUIRED_NOT_NULL表示不允许为空的关键字段，只要这些列是空，直接删掉这一行数据。
#5.`load_raw(path)`：原始读取，只做一件事，`pd.read_csv`读出原始 DataFrame，**不清洗**
#6.`check_columns(df)`：列校验函数，检查必填列是否存在，缺列抛出异常`ValueError`，提前拦截错误文件。
#7.pd.to_numeric(df[col], errors="coerce")指定列转为数字，`errors="coerce"`：转不成数字→设为 NaN；
#8.`dropna(subset=REQUIRED_NOT_NULL)`：删掉关键字段为空的行；
#9.`drop_duplicates(subset="主键", keep="first")`：按唯一标识去重，保留第一条；
#10.`sort_values(多列)`：多条件排序，先按排在前面的条件排序，按从小到大；
#11.`reset_index(drop=True)`：排序、删行之后，序号会乱，重置索引，`drop=True`丢掉旧索引；
#12.if __name__ == "__main__":表示只有运行__main__文件才会执行后续操作
#13.main作用是执行loader里数据清洗函数，进行数据清洗
#14.missing = [c for c in REQUIRED_COLUMNS if c not in df.columns]为列表推导式
#15.subset=["crack_id"]意思是只看这一个
#16.def load_raw(path):return pd.read_csv(path),需要return
#17.to_string保证数据好看且不被省略
#18.统计不同值出现的次数
