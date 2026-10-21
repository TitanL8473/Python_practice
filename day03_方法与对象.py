#今天学到了：
#1.char.lower` 是方法，要调用 `char.lower()`
#2.char.lower` 是函数对象，不是字符，永远不在元音集合里。改成：`char.lower()`
#3.遍历字典 `for subject,score in scores`直接遍历字典只会拿到 key（科目名），不能拆成 `subject, score`
# 字典遍历键值对要用 `.items()`：`for subject, score in scores.items()`
#4.初始值 `score_1=None`，比较 `score < score_1`

class Book:
    def __init__(self,title,price):
        self.title=title
        self.price=price
    def info(self):
        return f"《{self.title}》,售价{self.price}元"
print(Book("python入门",799).info())
def count_vowels(w):
    counts = 0
    for char in w:
        if char.lower() in {'a','e','i','o','u'}:
            counts+=1
    return counts
count_vowels('Hello World')
def best_subject(scores):
    subject_1=None
    score_1=-999
    for subject,score in scores.items():
        if score >score_1:
            subject_1=subject
            score_1=score
    print(subject_1,score_1)
best_subject({"语文":70,"数学":85,"英语":60})



