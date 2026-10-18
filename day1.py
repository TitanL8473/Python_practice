#1.`return sum` 必须退出 for 循环之后再写，你原来缩进在 for 里面，遍历第一个字符就直接返回，循环终止。
#2.**大小写问题**：原代码无法识别大写 `A E I O U`，加 `.lower()` 解决。
#3.变量名：不建议用`sum`做变量，会覆盖内置`sum()`函数，改成`sum_count`。
def shout(text):
    return f'{text}!'
text=input("输入你要喊的话:")
print(shout(text))

def count_vowels(word):
    count=0
    vowels=['a','e','i','o','u']
    for char in word:
        if char.lower() in vowels:
            count+=1
    return count
word=input("请输入您想要统计元音个数的单词:")
print(count_vowels(word))