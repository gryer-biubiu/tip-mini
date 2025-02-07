# scp

> 安全复制 (Secure Copy) 实用程序。
> 通过 SSH 协议安全地在本地与远程系统间复制文件和目录。
> 更多信息：<https://linux.die.net/man/1/scp>.

- 将本地文件复制到远程主机：

`scp {{local_file_path}} {{username}}@{{remote_host}}:{{remote_directory}}`

- 将远程主机上的文件复制到本地：

`scp {{username}}@{{remote_host}}:{{remote_file_path}} {{local_directory}}`

- 将整个目录从本地复制到远程主机：

`scp -r {{local_directory}} {{username}}@{{remote_host}}:{{remote_directory}}`

- 从远程主机复制整个目录到本地：

`scp -r {{username}}@{{remote_host}}:{{remote_directory}} {{local_directory}}`

- 使用特定端口连接远程主机：

`scp -P {{port_number}} {{local_file_path}} {{username}}@{{remote_host}}:{{remote_directory}}`