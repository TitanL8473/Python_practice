#今天学到了：
#1. with open(文件地址,'r',encoding='utf-8') as file:
#2.len函数可以输出文本的行数
#3.文件位置data.txt 和 day4.py 在同一个文件夹（202610安排）count_lines("data.txt")
#4.try与except,- `except 错误类型:`：**只捕捉这一类错误，except:`（不带类型）：捕捉全部错误（所有其他情况
def safe_div(a,b):
    if b!=0:
        return a/b
    else:
        return None
print(safe_div(6,0))
def count_lines(text):
    with open(text,'r',encoding='utf-8') as file:
        li=file.readlines()
        if len(li) !=0:
            print(len(li))
        else:
            print('-1')
count_lines('data.txt')
def safe_div(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        return None
def count_lines(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        return len(lines)            # 注意：是 return，不是 print
    except FileNotFoundError:
        print(f"文件不存在:{path}")
        return -1                    # 数字 -1，不是字符串 '-1'
