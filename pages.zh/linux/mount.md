# mount

> 文件系统挂载工具。
> 用于将文件系统（如磁盘分区、ISO镜像、网络文件系统等）挂载到指定的挂载点。
> 更多信息：<https://man7.org/linux/man-pages/man8/mount.8.html>.

- 挂载设备或远程文件系统：
`sudo mount {{/dev/device}}`

- 挂载设备或远程文件系统到指定目录：
`sudo mount {{/dev/device}} {{/path/to/mount_point}}`

- 挂载 ISO 镜像文件：
`sudo mount -o loop {{path/to/image.iso}} {{/path/to/mount_point}}`

- 挂载时设置只读权限：
`sudo mount -o ro {{/dev/device}} {{/path/to/mount_point}}`

- 挂载 NFS 共享：
`sudo mount -t nfs {{remote_host:/remote/path}} {{/path/to/mount_point}}`

- 使用 UUID 或标签来挂载分区（推荐做法，避免因设备名称变化导致的问题）：
`sudo mount /dev/disk/by-uuid/{{UUID}} {{/path/to/mount_point}}`
`sudo mount /dev/disk/by-label/{{LABEL}} {{/path/to/mount_point}}`

- 挂载并设置特定选项（例如：noexec, nosuid, nodev 禁止执行脚本、禁止 SUID 和 GUID 位、禁止特殊设备文件）：
`sudo mount -o noexec,nosuid,nodev {{/dev/device}} {{/path/to/mount_point}}`

- 查看所有已挂载的文件系统：
`mount`

- 查看特定路径是否被挂载：
`mount | grep {{/path/to/check}}`

- 卸载文件系统：
`sudo umount {{/path/to/mount_point}}`

- 强制卸载（当正常卸载失败时使用，需谨慎）：
`sudo umount -l {{/path/to/mount_point}}` # 懒卸载，等待所有进程完成后卸载
`sudo umount -f {{/path/to/mount_point}}` # 强制卸载

- 挂载 tmpfs（内存中的临时文件系统）：
`sudo mount -t tmpfs -o size=512m tmpfs {{/path/to/mount_point}}`

- 编辑 `/etc/fstab` 文件以实现开机自动挂载：
编辑 `/etc/fstab` 文件，添加一行如下格式的内容：
`{{/dev/device}} {{/path/to/mount_point}} {{filesystem_type}} defaults 0 0`