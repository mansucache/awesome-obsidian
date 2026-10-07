# 维护机制

## 日常修改

修改资源事实与说明后，核对相关来源和两种语言。新增条目还需加入一个主分组；场景路线可以交叉引用。

完成双语审阅后执行：

    python3 scripts/review_record.py dataview --bump --reviewed en zh-cn
    python3 scripts/catalog.py check --release
    python3 -m unittest discover -s scripts -p 'test_*.py'
    python3 scripts/catalog.py build --release

辅助命令更新修订号、已审核语言与正文哈希，不核验来源，也不刷新来源日期。更改 summary 或 context 时同步正文；来源日期只在实际核对后修改。

只完成英文可用 --bump --reviewed en。未审核语言会变为 stale，记录进入 draft；可运行 check --draft 检查结构。完成另一语言后运行 --reviewed zh-cn，不再次 bump。确认全部信息可收录，再将 publication 明确改为 listed。草稿可以提交讨论，但不能通过正式发布检查。

## 复核与退出

- documented：当前正常收录。
- needs-review：收到有效疑问或检查异常，记录日期、双语原因和下一步，暂不自动删除。
- archived：确认已停止维护且保留历史参考价值，退出主目录、路线和图库，历史区说明原因。
- unavailable：确认资源已不可用，同样退出主目录并保留历史入口；必要时在原因中给替代方向。

一次超时、403、429 或长时间没有提交不构成退出证据。确认官方说明、项目迁移或持续失效后再改状态。一般疑似失效至少复查一次，涉及争议时在纠错讨论中保留维护者回应时间；不统一设定机械删除天数。

恢复资源时补充新来源、重新核对双语内容和依赖，再改回 documented。彻底删除记录时同步清理导航和 related；数量减少是合法结果，不需要补无价值条目维持数字。

## 定期检查

运行 python3 scripts/catalog.py report 获取编辑复核队列。超过 90 天未核对是复查提醒，平台未知也是信息缺口，不是自动拒收标准。

独立的 Periodic resource review 工作流每周检查全部已收录资源的来源链接，有限重试，在 Actions 摘要保留错误与复核队列。该工作流不发评论、不创建 issue、不自动删条目；网络异常不阻断普通内容 PR。推送后才能在远端实际运行，本地配置通过不等于远端任务已成功。

维护者每周查看报告，优先处理确定迁移和持续 404/410，再处理价格、归档状态及平台差异。检查器返回成功不证明内容事实正确。原 1.0 的规模数字保留在版本记录中，不再作为后续发布门槛。

## 辅助检查

- check：严格检查当前记录与双语内容。
- check --draft：仅对显式草稿中的 stale 译文放宽修订号与哈希检查，仍检查链接、资源关系和内容语法。
- check --release：严格检查，并要求不存在草稿且有可展示内容。
- sources：输出去重的来源地址，供独立链接检查器使用。
- report：输出需要编辑复核的信号，不修改记录。

README 和网站由同一批字段生成；历史记录不计入主目录数量。第三方图片与许可仍需保留来源文件。
