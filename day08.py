#今天学到了:
#1.`from pathlib import Path`：导入路径工具类 Path
#2.`HERE = Path(__file__).resolve().parent`；`__file__`：当前这个`.py`文件本身；`.resolve()`拿到完整绝对路径，`.parent`取它所在的文件夹，
#3.- `path.name`：path对应文件名（`data.txt`） `path.suffix`：文件后缀（`.txt`）`path.parent.name`：这个文件所在文件夹名字
#4.- `folder.glob("*.py")`：只看当前一层，不会钻进子文件夹`*.py`：匹配所有后缀 py 的文件，用途：列出当前文件夹所有 python 脚本名字
#5.`list()`把扫描结果转成列表，`len()`数一共有多少个 py 文件。用途：统计整个目录树里面全部 py 文件总数
#6. cd "D:\2026-10-10-20-22-17\py-toolbox",在终端里，切换进入 `py-toolbox` 这个 Git 项目文件夹。
#7.git add .   - 把文件加入暂存区，告诉 Git：这些文件的改动，我准备保存成新版本了。这个点`.` 代表当前文件夹下所有改动过的文件（新增、修改的全部文件）。
#8.git commit -m "feat: pathlib 文件遍历工具"- `git commit`：在本地电脑生成一份永久代码快照（版本），把刚刚 add 选中的改动保存。
#9.`-m "描述文字"`：写提交备注，记录这次做了什么。
#10.`feat:` 是约定规范，代表 feature（新增功能）。这里就是：新增 pathlib 文件遍历相关工具代码。
#11.git push 把刚才本地 commit 做好的版本，**推送到远程仓库（Gitee/GitHub 等云端）**

from pathlib import Path
HERE = Path(__file__).resolve().parent

def describe(path):
    return f"{path.name} | 后缀 {path.suffix} | 上级目录 {path.parent.name}"

print(describe(HERE / "data.txt"))

def list_py_files(folder):
    py_name_list = [p.name for p in folder.glob('*.py')]
    return sorted(py_name_list)
print(list_py_files(HERE))

def count_all_py(folder):
    return len(list(folder.rglob("*.py")))
print(count_all_py(HERE))

def count_lines(path):
    try:
        with open(path,'r',encoding='utf-8') as file:
            return len(file.readlines())
    except FileNotFoundError:
        print("文件不存在")
        return -1
print(count_lines(HERE/"data.txt"))
print(count_lines(HERE / "没有这个文件.txt"))


