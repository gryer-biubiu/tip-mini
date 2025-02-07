# fdisk

> 分区管理工具。
> 用于创建、编辑、删除和列出硬盘上的分区信息。
> 更多信息：<https://man7.org/linux/man-pages/man8/fdisk.8.html>.

- 启动交互式 `fdisk` 会话来管理指定设备：
`sudo fdisk {{/dev/device}}`

- 列出所有分区表（非交互式）：
`sudo fdisk -l`

- 创建一个新的 DOS 分区表（MBR）：
`sudo fdisk -cu {{/dev/device}}`
然后在交互模式下输入以下命令：
- `o` 创建一个新的空的 DOS 分区表
- `n` 添加新分区
- `p` 创建主分区或扩展分区
- `e` 创建扩展分区（如果需要）
- `w` 写入更改并退出

- 创建一个新的 GPT 分区表（适用于大容量磁盘）：
`sudo fdisk {{/dev/device}}`
然后在交互模式下输入以下命令：
- `g` 创建一个新的空的 GPT 分区表
- `n` 添加新分区
- `w` 写入更改并退出

- 删除现有分区：
`sudo fdisk {{/dev/device}}`
然后在交互模式下输入以下命令：
- `d` 删除一个分区
- 输入要删除的分区编号
- `w` 写入更改并退出

- 改变分区类型：
`sudo fdisk {{/dev/device}}`
然后在交互模式下输入以下命令：
- `t` 改变分区类型
- 输入要修改的分区编号
- 输入新的分区类型代码（例如：83 表示 Linux 文件系统）
- `w` 写入更改并退出

- 查看指定磁盘的分区信息（非交互式）：
`sudo fdisk -l {{/dev/device}}`

- 在不实际写入磁盘的情况下模拟操作：
`sudo fdisk -n {{/dev/device}}`

- 修改分区后刷新内核中的分区表而不重启系统：
`sudo partprobe {{/dev/device}}`