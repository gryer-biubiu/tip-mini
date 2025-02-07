# tar

> 归档实用程序。
> 用于创建和提取归档文件（.tar），并通常与压缩方法结合使用，例如 gzip (.tar.gz 或 .tgz)、bzip2 (.tar.bz2) 或 xz (.tar.xz).
> 更多信息：<https://www.gnu.org/software/tar>.
> 
v (verbose): 显示处理过程中的详细信息，通常是指显示正在被处理的文件名。
x (extract): 从归档中提取文件。
z (gzip): 使用 gzip 程序解压缩数据。这表示该档案是用 gzip 压缩的。
f (file): 指定接下来的参数是要操作的文件名。
>
- 创建一个未压缩的归档文件：
`tar -cf {{archive.tar}} {{file1 file2 ...}}`

- 创建一个 gzip 压缩的归档文件：
`tar -czf {{archive.tar.gz}} {{file1 file2 ...}}`

- 使用相对路径从指定目录创建一个 gzip 压缩的归档文件：
`tar -czf {{archive.tar.gz}} --directory={{path/to/directory}} .`

- (解压)详细地将（可能压缩的）归档文件提取到当前目录中：
`tar -xvf {{source.tar[.gz|.bz2|.xz]}}`

- (解压)将（可能压缩的）归档文件解压到指定的目标目录中：
`tar -xf {{source.tar[.gz|.bz2|.xz]}} --directory={{destination_directory}}`

- (解压)解压到特定的目录

`tar vxzf archive.tar.gz -C /path/to/destination`

- (压缩)根据存档后缀自动选择压缩程序创建压缩归档文件：
`tar -caf {{archive.tar.xz}} {{file1 file2 ...}}`

- (压缩) 根据存档后缀压缩所有文件为tar.gz：
`tar -caf {{archive.tar.xz}} .`

- 详细列出 tar 文件的内容（包括文件权限、所有者、大小和时间戳等信息）：
`tar -tvf {{source.tar}}`

- 从归档文件中仅提取与模式匹配的文件（例如所有 HTML 文件）：
`tar -xf {{source.tar}} --wildcards "{{*.html}}"`

- 添加文件到已存在的 tar 归档中（注意：此功能不支持压缩归档）：
`tar -rf {{archive.tar}} {{new_file}}`

- 从归档中删除文件（注意：此功能不支持压缩归档）：
`tar --delete -f {{archive.tar}} {{file_to_remove}}`

- 按照大小进行分包处理
`split -b 5G archive.tar.gz archive.tar.gz.`