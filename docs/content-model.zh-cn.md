# 内容模型

机器契约为 [catalog-contract.json](../data/catalog-contract.json) v2。资源事实存于 data/resources，双语正文存于 content/en 与 content/zh-cn。

## 阅读层与数据层

- locales.summary：直接说明用途与场景，是 README 与网站卡片的共同介绍。
- locales.context：可选的选择说明，补充适用人群、门槛或关键边界。不要重复 summary。
- cost_note 与 show_cost：费用记录始终存在；只有具体且影响选择时才展示。
- 正文：保留稳定 Markdown 地址；出现二级章节时，目录自动提供“用法与选择”入口。目录里的关键条件不能只藏在详情中。
- local_content：用于本项目原创模板和指南，目录链接到仓库内正文，而非把参考资料当作原创资源的主页。
- related：资源关系；正文中的本地资源链接必须登记，生成后保持同语言跳转。

完整写法与示例见 [编辑规范](editorial-policy.zh-cn.md)。不规定统一字数，不强迫所有资源写成长文。

## 双语与修订

revision 表示记录修订；based_on_revision 和 content_sha256 检查正文同步。哈希只证明文件版本一致，不代表事实或翻译已经审核。

修改正文后，编辑者核对两种语言，再运行 review_record.py 记录已审核语言。只完成一种语言时保留草稿，使用 check --draft；正式发布拒绝草稿和过期译文。

## 收录与状态

publication 采用 draft / listed，表示是否进入目录，不表示由真人审核。原 sample 在本轮迁移为 listed，反映此前已经进入 README 的事实，不追加不存在的审核声明。

status 采用 documented / needs-review / archived / unavailable。待复核资源暂留主目录；归档和失效资源退出搜索、任务路线和主题图库，在 README 历史区保留原因与详情地址。历史详情与素材继续生成，避免旧链接失效。

非 documented 状态必须包含 maintenance.date 和双语 maintenance.reason。具体退出、恢复与定期复核规则见 [维护机制](maintenance.zh-cn.md)。
