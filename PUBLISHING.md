# 发布到 GitHub · 最小步骤

1. 在 GitHub 新建一个**空的公开仓库**，命名为 `AQING-AI-Skill-Lab`。不要勾选自动添加 README 或 LICENSE（本地已经包含）。
2. 解压整仓 ZIP，进入 **包含 README.md 的仓库根目录**。
3. 在此目录运行：

```bash
python scripts/validate_skills.py

git init
git add .
git commit -m "feat: release three AI creative skills v0.1.0"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/AQING-AI-Skill-Lab.git
git push -u origin main
```

将 `YOUR_USERNAME` 替换为真实 GitHub 用户名。首次 `git push` 可能要求你先按 GitHub 的方式完成登录/身份验证；本仓库不包含账号或 Token。

**替代方式：**也可以在 GitHub 新仓库页面选择上传文件，上传**解压后的仓库内容**，确保 GitHub 根目录显示 `README.md`、`LICENSE`、`skills/`，而不是又套了多余一层目录。

## 发布后最先验证

- GitHub 首页能显示 `README.md` 的三套 Skill 链接。
- 三个 `SKILL.md` 顶部 YAML 字段完整，文件相对引用可点击。
- 用 `tests/acceptance-scenarios.md` 的各一个测试提示词，在实际目标 Agent 中试跑。
- 不要写“兼容某平台/已在某模型测试通过”，除非你真的完成了该平台的安装和任务验证。

## GitHub Release

创建 GitHub Release `v0.1.0` 时，可附整仓 ZIP 供浏览，以及每套独立 Skill ZIP 供单独导入。**一个独立 Skill ZIP 只包含一个顶层 Skill 目录**，其根目录是 `SKILL.md` 的父目录。

## 小云雀说明

上传到 GitHub 是开源发布，不等于已成功安装到小云雀。内测平台可能有专属上传格式、能力限制或审核条件，正式导入前以小云雀当期官方要求为准。
