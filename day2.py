#今天学到了:
# 1.字典获取所有键值对的方法是 `.items()`，**必须加小括号**；
#2.`return` 在 for 循环里面，第一次循环就直接返回，只能输出第一条科目，后面的科目不会遍历。
#`3.m_score="-999"` 带双引号，是字符串；你本意是数字，应该写 `m_score=-999`，这样易于比较
#4. Python 普通输出用内置函数`print()`，不存在`print_line()`。
#5. 报错风险：尝试导入不存在的函数，会触发`ImportError`

dct_score={"语文":86,"数学":79,"英语":68}
def show_scores(d):
    for key,value in d.items():
        print(f"{key}:{value}")
show_scores(dct_score)
def maximate_scores(d):
    subject=None
    m_score=-999
    for key,value in d.items():
        if value>m_score:
            m_score=value
            subject=key
    return subject,m_score
print(maximate_scores(dct_score))
