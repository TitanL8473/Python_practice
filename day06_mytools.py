#我学到了：
#1.- 计数器要**在循环外面初始化为 0**,不要写在`for`循环内部，否则每次循环都会清零
def count_vowels(text):
    counts_vowels = 0
    for char in text:
        if char.lower() in {'a','e','i','o','u'}:
            counts_vowels+=1
    return counts_vowels
def average(number):
    try:
        sums=0
        counts_numbers=0
        for data in number:
            sums+=data
            counts_numbers+=1
        dividend=sums/counts_numbers
        return dividend
    except ZeroDivisionError:
        return '空列表，除零错误'

def best_subject(subjects):
    subject=None
    score=-999
    for key,value in subjects.items():
        if value>score:
            subject=key
            score=value
    return subject
def count_lines(path):
    try:
        with open(path,'r',encoding='utf-8') as file:
            line=file.readlines()
        return len(line)
    except FileNotFoundError:
        print('文件不存在')
    return -1
if __name__ == "__main__":
     print(">>> mytools 模块被加载了")
     print(">>> 自测结果:", count_vowels("Hello world"))