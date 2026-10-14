# AQING AI Skill Lab

**以设计思维驱动的 AI 视觉创作 Skill 系统**  
*A design-driven collection of reusable AI creative skills.*

> v0.1.0 · 由 AQING 整理 · 中文优先 · [MIT License](LICENSE)

本仓库包含三套独立的 Agent Skills。它们不是“万能提示词”，而是把创作任务拆解为**可执行的步骤、可检查的约束、可复制的输出**。面向需要构思海报、设计 AI 视频、制作电影感人像的设计师与创作者。

## Skills

| Skill | 典型需求 | 核心输出 |
| --- | --- | --- |
| [`visual-story-director`](skills/visual-story-director/SKILL.md) | AI 短片、IP 剧情、动作衔接、视频生成提示词 | 故事目标、分镜表、状态连续性表、成片 Prompt、失败修复建议 |
| [`editorial-poster-designer`](skills/editorial-poster-designer/SKILL.md) | 品牌视觉、编辑海报、实验海报、商业主视觉 | 设计命题、概念路线、层级与色彩方案、视觉 Prompt、质检 |
| [`cinematic-portrait-director`](skills/cinematic-portrait-director/SKILL.md) | 电影级肖像、时尚编辑、人像写真、参考图一致性 | 气质定义、构图/镜头/布光策略、人像 Prompt、身份约束 |

## 开始使用

### A. 在支持 Agent Skills 的客户端中使用

1. 下载本仓库，找到 `skills/` 下想使用的**单个** Skill 文件夹。
2. 将文件夹复制到你所使用客户端的 Skill 目录，或按该客户端的导入说明安装。不同客户端的安装路径和功能不同；**本仓库不假设通用安装路径**。
3. 在对话中直接描述你的创作任务，或明确指定：`请使用 visual-story-director ...`。
4. 如缺少核心信息，Skill 会先问必要问题；信息足够时会按结构化流程产出。

### B. 普通 ChatGPT / 其他大模型手动使用

打开对应的 `SKILL.md`，将内容作为工作指令提供给支持长文本的助手；遇到 `references/` 中的说明再追加即可。**这不等价于客户端原生安装或自动触发 Skill**。

### C. 独立 Skill ZIP

发行包另提供三个独立 ZIP，每个 ZIP 仅有一个顶层 Skill 目录，方便按平台能力分别导入。整仓 ZIP 用于 GitHub 托管，**不要把整仓 ZIP 当作单个 Skill 上传**。

## 试用样例

- **短片**：「一个角色边看手机边走，差点撞到正前方电线杆，闪身躲过，再把易拉罐踢进垃圾桶。15 秒，9:16。请标出动作因果和物件位置。」
- **海报**：「设计一张非遗主题概念海报，3:4，表达『摘下面具是人，戴上面具是神』，只生成纯视觉稿，文字我后期自己排。」
- **人像**：「为成年女性设计冷感奢侈品 Editorial 个人写真，9:16，侧向强光、真实皮肤，不要网红滤镜；请给可复制的 Prompt。」

完整案例：每套 Skill 的 [`examples/`](skills/visual-story-director/examples/) 文件夹。

## 通用准则：AQING Creative QA

- **意图先于描述：**先弄清画面/短片要表达什么，再写 Prompt。
- **主体先于装饰：**用一个主视觉或核心事件建立识别，不靠元素堆砌。
- **关系先于形容词：**明确画面元素、镜头、动作、光影之间的关系。
- **可验证先于自信：**列出风险和复核点；生成结果未经看见，不宣称“已验证”。
- **最小修改：**用户要求局部更改时保留其他已确认的元素，不顺手重设计。

## 仓库结构

```text
AQING-AI-Skill-Lab/
├── README.md
├── LICENSE
├── CHANGELOG.md
├── CONTRIBUTING.md
├── .gitignore
├── skills/
│   ├── visual-story-director/
│   │   ├── SKILL.md
│   │   ├── references/
│   │   ├── assets/
│   │   └── examples/
│   ├── editorial-poster-designer/
│   │   ├── SKILL.md
│   │   ├── references/
│   │   ├── assets/
│   │   └── examples/
│   └── cinematic-portrait-director/
│       ├── SKILL.md
│       ├── references/
│       ├── assets/
│       └── examples/
├── scripts/validate_skills.py
└── tests/acceptance-scenarios.md
```

## 校验与范围

```bash
python scripts/validate_skills.py
```

校验脚本仅检查该仓库 `SKILL.md` 的元数据约束、目录命名、文件引用是否存在；**不会**衡量模型生成画质，也不等于小云雀、Codex 等特定平台的官方兼容性认证。另有 [人工验收场景](tests/acceptance-scenarios.md) 用于实际试跑。

## 关于工具与平台

- 本仓库是可携带的**指令型 Skill**；本身不含调用图片/视频模型的 API，不会自动生成图片或视频。
- 若所在平台具备图像生成/参考图/视频分析等能力，可按平台实际能力使用；若不支持，则只输出可执行方案及 Prompt。
- 不同视频模型的支持时长、参考图数量、分辨率及语法会变化，本文不虚构“官方参数”。
- 若用户指定原有角色或人脸参考，尊重使用权限。身份一致性是目标与检查项，不保证每次生成精确复刻。

## 开发与贡献

欢迎通过 Issue 提供**输入 → 实际输出 → 预期输出 → 复现条件**；不要上传未经授权的真人肖像、商业机密或第三方受版权保护的素材。详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 许可

项目源文本与脚本采用 [MIT](LICENSE)。第三方模型、平台、用户上传图片及输出素材的权利状态另行决定，MIT **不授权**不属于仓库作者的素材。

## 相关标准

- [Agent Skills 开放规范](https://agentskills.io/specification)
- [OpenAI Skills 文档](https://developers.openai.com/api/docs/guides/tools-skills)
