# repo
> Repo 是一个命令行工具，它建立在 Git 之上，用于管理 Android 开发中的多个相关 Git 仓库。
> 更多信息：https://source.android.com/setup/develop/repo.

- 初始化一个新的客户端工作目录（必须首先设置 $REPO_URL 环境变量指向 repo 工具的存储位置）：

`repo init -u {{manifest_url}}`

- 同步Manifest中定义的所有项目到本地：

`repo sync`

- 列出所有检查出来的项目：

`repo list`

- 查看每个项目的工作区状态：

`repo status`

- 在所有项目中开始一个新的分支：

`repo start {{branch_name}} --all`

- 提交更改到所有项目：

`repo commit`

- 将当前分支的变化上传到Gerrit代码审查系统：

`repo upload`

- 获取repo所有仓commit信息
`repo forall -c 'git log --author="@xxx.com" --grep="^JIRA TICKET" --grep="^Reference:" --grep="^Product:" | python gitLogParser.py -project_name ${REPO_PROJECT}' > output.txt`

- 用于导出当前 Repo 项目的工作区配置到一个指定的 XML 文件中
`repo manifest -r -o ${workspace}/manifest.xml`