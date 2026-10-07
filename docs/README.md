# 设计与内容维护入口

优先阅读 [英文 README](../README.md) 或 [中文 README](../README.zh-CN.md)：两者均可独立浏览资源、场景和主题图片。网站仅提供更方便的检索与浏览。

当前内容：225 项资源、7 篇场景指南、15 个带图主题，覆盖 10 个分类；全部提供中英双语内容，并同步到 README 与静态网站。1.0 本地内容版已形成，公开发布单独进行。

1. 阅读 [项目设计](project-design.zh-cn.md)，确认项目的长期边界。
2. 阅读 [内容规范](content-model.zh-cn.md) 与 [编辑规范](editorial-policy.zh-cn.md)，了解分层条目与来源维护方式。
3. 打开 [内容目录](samples.zh-cn.md)，浏览 232 个条目；[English catalog](samples.en.md) 对应英文版本。
4. 查看 [验收记录](validation.zh-cn.md)，区分自动检查、编辑审核和真实使用。

## 对标与内容组织

[五个参考项目的吸收与改进](reference-projects.zh-cn.md) 记录各项目的优点、采用方式与可检查的结果。`data/navigation.json` 维护 40 个用途分组和 11 个任务入口，与两份 README 和网站共用。

## 本地预览

在仓库根目录执行 `python3 scripts/catalog.py build`，再执行 `python3 -m http.server 18765 --bind 127.0.0.1 --directory site/preview`，打开 <http://127.0.0.1:18765/>。端口若被占用可自行更换。默认英文；选择中文后保持当前资源页面。

不需要下载依赖。正式构建使用 `python3 scripts/catalog.py build --release`，输出 `site/dist`，详见 [1.0 内容版](release-1.0.zh-cn.md)。生成目录已忽略，不手改其中内容。

## 维护命令

- `python3 scripts/catalog.py check`：数据、双语、分类、关系、图片与正文链接检查。
- `python3 scripts/catalog.py build`：先检查，再生成两份 README、页面和两份内容目录。
- `python3 -m unittest discover -s scripts -p 'test_*.py'`：验证错误资料不会静默通过。

英文贡献入口：[CONTRIBUTING.md](../CONTRIBUTING.md)。

## 当前改版

[维护机制](maintenance.zh-cn.md) 说明草稿、复核、归档与恢复；[编辑规范](editorial-policy.zh-cn.md) 说明用途、场景和选择条件的分层写法。新增模板是本项目原创内容，可直接从目录打开复制。
