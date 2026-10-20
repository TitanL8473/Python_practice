# Git 推送速查（每天收工照着做）

## 日常三步（remote 已配好的情况下）

```powershell
cd "D:\OneDrive\桌面\PyCharm 文件\202610安排"

git add .                                    # ① 挑出要提交的文件
git commit -m "feat: Day13 项目骨架"          # ② 在本地存档
git push                                     # ③ 上传到 GitHub
```

**三步各有一步自检：**

| 步 | 命令 | 成功的标志 |
|---|---|---|
| ① | `git status` | 看到绿色/`A`/`M`，不是 `??` |
| ② | `git log --oneline` | 最上面多了一条新记录 |
| ③ | （看 push 输出） | `xxx..yyy  main -> main` |

**三条都对，才算完成。**

---

## 首次推送一个全新仓库（只做一次）

```powershell
cd "你的项目文件夹"
git init                                         # 让文件夹变成仓库
git add .
git commit -m "feat: 初始化"
git remote add origin https://github.com/用户名/仓库名.git    # 告诉它远程在哪
git push -u origin main                          # 首次要加 -u
```

之后就不用再 `git init` 和 `git remote add` 了。

---

## 每一步在干什么（对照理解）

```
你电脑上的文件
      │  ① git add .        挑出哪些改动要提交（放进暂存区）
      ▼
   暂存区
      │  ② git commit       打成一个版本快照（存在本地 .git 里）
      ▼
  本地仓库
      │  ③ git push         上传到 GitHub
      ▼
  GitHub 网页
```

**关键：GitHub 上「建了仓库」≠「代码上去了」。** 建仓库只是造了个空箱子，必须走完这三步才搬过去。

---

## 常见错误速查

| 你看到的 | 原因 | 怎么办 |
|---|---|---|
| `nothing specified, nothing added.` | `git add` 后面**漏了 `.`** | 改成 `git add .` |
| `nothing to commit, working tree clean` | 没有新改动，或已经提交过 | 正常，继续 `git push` |
| `nothing added to commit but untracked files present` | 没 add 就 commit | 先 `git add .` |
| `src refspec main does not match any` | 一次 commit 都没有就想 push | 先 add + commit |
| `'origin' does not appear to be a git repository` | 没配 remote | `git remote add origin <地址>` |
| `Everything up-to-date` | 本地没有新提交 | 正常，说明远程已是最新 |
| `Recv failure: Connection was reset` | 网络被掐 | **等几分钟重试**，或换手机热点 |
| `fatal: unable to access ... CONNECT tunnel failed` | 走了坏代理 | 检查代理设置 |

---

## 两个习惯

**① 提交信息用固定前缀**（这叫约定式提交，业界通用）

```
feat:  新功能       feat: Day13 项目骨架 + 数据清洗模块
fix:   修 bug       fix: 修正 main.py 的数据路径
docs:  改文档       docs: 更新 README 使用说明
chore: 杂项         chore: 注释掉临时调试打印
```

**② 每天收工就推，不要攒。**
攒一周的改动一次提交，等于没提交——**看commit记录的人想看的是"持续在做"，不是"一次性写完"。**

---

## 永远不要做的两件事

1. **不要 `git add` 整个 `.venv/`** —— 几千个第三方库文件，会把仓库撑爆
   （`.gitignore` 里已经挡了，venv 自己也带了一个 `.gitignore`）

2. **不要用 `git push -f`** —— 强制覆盖远程，会把别人的（或你自己之前的）提交抹掉
