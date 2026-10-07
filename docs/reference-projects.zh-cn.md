# 参考项目：吸收与改进

对照日期：2026-10-07。本次阅读五个仓库的 README，并回到候选资源的原始项目核对功能。本文记录取舍；读者直接使用根目录中的中英文清单。

## 五个项目分别提供了什么

| 项目 | 值得吸收的优点 | 本项目中的实现 |
| --- | --- | --- |
| [kmaasrud/awesome-obsidian](https://github.com/kmaasrud/awesome-obsidian) | 生态覆盖广，外部工具进一步拆成转换、浏览器扩展和发布；区分整库模板与笔记模板，主题配图。 | 保留完整 README，增加迁移工具、终端集成、CSS 布局；模板细分，保留主题图片。 |
| [obsidian-pkm-vault/awesome-obsidian-vault](https://github.com/obsidian-pkm-vault/awesome-obsidian-vault) | 按用途组织库与网站，强调可下载内容，也给在线阅读入口。 | 增加个人管理、研究和查询示例库；条目明确是整库、模板或网站，收录 Hub 这样的可在线阅读也可下载的资源。 |
| [PKM-er/awesome-obsidian-zh](https://github.com/PKM-er/awesome-obsidian-zh) | 按功能细分插件，照顾中文输入、中文搜索、社区与学习入口。 | 增加 Easy Typing、Fuzzy Chinese Pinyin、Quiet Outline、AnyBlock、LifeOS 和 PKMer；提供独立中文任务入口，两种语言使用同一套资源。 |
| [awesome-obsidian/awesome-obsidian](https://github.com/awesome-obsidian/awesome-obsidian) | 分类计数直观，CSS、Dataview、Vault、工作流和集成各有位置；仓库采用结构化资料。 | 共享数据生成分类计数与双语目录；加入 CSS、Dataview 示例和启动器集成；导航自动检查遗漏、重复和错分。 |
| [danielrosehill/Awesome-Obsidian-AI-Tools](https://github.com/danielrosehill/Awesome-Obsidian-AI-Tools) | AI 不局限于聊天，覆盖本地模型、检索、Canvas、语音、分类与学习。 | AI 分为五组，增加 Local GPT、LLM Workspace、Cannoli、Aloud、Auto Classifier、Quiz Generator 和对话归档工具。 |

## 改进标准与当前结果

“更好”首先落实为更容易找到、理解和维护，不以条目数或 GitHub 星数作为结论。

| 标准 | 当前结果 | 复查方式 |
| --- | --- | --- |
| 不知道插件名称也能开始查找 | 10 个任务入口，连接具体资源 | README 顶部任务表；网站任务卡片 |
| 大分类内能够快速定位用途 | 10 个大类、41 个维护分组，多组类别展示二级导航 | README 小目录；网站用途筛选 |
| 独立阅读 README 可获取完整内容 | 221 个条目、15 个带图主题、中英文对齐 | 无需构建即可打开根 README 与本地图片 |
| 增加资源时不会丢失导航 | 每条资源恰好属于一个主要分组；任务入口可跨类引用 | 导航覆盖、重复与悬空链接测试 |
| 网站增强查找，不独占资源 | 搜索、分类、用途、费用可以组合，并保存到链接；切换语言保留筛选 | 本地浏览器检查 |
| 普通条目的维护成本可控 | 名称、原始链接、一句用途；收费项目简短标识 | 对照中英 README 与条目内容 |

1.0 共 221 条内容，其中 215 项资源与 6 篇原创场景指南。AI 分类有 28 项，模板与示例库有 15 项，外观分类包括 15 个带图主题与 5 项 CSS、配色资源。

## 取舍

- 采用用途分类与视觉浏览，不引入星数总分、奖牌排名、逐条克隆命令或冗长元数据。
- 资源句子根据原始项目重写，保留五个参考目录的致谢链接；没有整段复制目录介绍、CSS 或模板内容。
- 示例库、普通 Markdown 文档站和在线网站分别判断；不把所有可下载仓库都称为 Obsidian 模板。
- AnyBlock 的旧仓库地址已转到当前原始仓库。Topobon 候选的当前 README 主要介绍发布模板，本次未将其按个人示例库收录；NodeFlow 的功能工作流仍有重构说明，本次未把它作为成熟 AI 自动化工具加入。
- 更新日期和自动抓取的描述可以辅助发现，不直接决定推荐。对收费模式、模型依赖和具体功能仍查看原始说明。

本次没有证明本项目在全部资源数量、每个专业领域的深度或长期维护上超过这些项目。已经实现的优势是：双语完整目录、简洁条目、主题配图、任务入口与用途分类能够一起使用。1.0 已补齐静态网站构建与六篇场景指南，长期维护效果仍需通过持续更新检验。
