#今天学到了：
#1:split() 默认：按任意空白（空格、换行、制表符）切分，自动忽略连续空白
#2.len("abc") # len 是内置函数，接收对象作为参数;s = "hello world",s.split() # split 是字符串s的方法，依附于字符串对象
def count_vowels(wo):
    counts = 0
    for ch in wo:
        if ch.lower() in {'a','e','i','o','u'}:
            counts+=1
    return counts
print(count_vowels("Hello world"))
def best_subject(subjects):
    su_0=None
    score_0=-999
    for key,value in subjects.items():
        if score_0<value:
            su_0=key
            score_0=value
    return su_0
print(best_subject({"语文": 70, "数学": 85, "英语": 60}))
def average(numbers):
    av=0
    nu=0
    for number in numbers:
        nu+=1
        av+=number
        out=av/nu
    return out
print(average([70, 85, 92.5]))
def solve_quadratic(a,b,c):
    d=b*b-4*a*c
    if d<0:
        return None
    else:
        x1 = ((-b) + (d ** (1 / 2))) / (2 * a)
        x2 = ((-b) - (d ** (1 / 2))) / (2 * a)
        return x1,x2
print(solve_quadratic(1, -3, 2))
bad = r"D:\notes\data.txt"
def count_words(words):
    words_counts=len(words.split())
    return words_counts
print(count_words("hello world\n你好 世界 再见"))
def count_lines(text):
    try:
        with open(text,'r',encoding='utf-8') as file:
            li=file.readlines()
            return len(li)
    except FileNotFoundError:
        print('文件不存在')
        return -1
    