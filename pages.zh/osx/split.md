# split

> 把一个文件拆分成几块。
> 更多信息：<https://keith.github.io/xcode-man-pages/split.1.html>.

- 分割一个文件，每个分割部分有 10 行（除了最后一个）：

`split -l {{10}} {{文件名}}`

- 用正则表达式拆分文件。匹配行将是下一个输出文件的第一行：

`split -p {{cat|^[dh]og}} {{文件名}}`

- 拆分一个文件，每个拆分中有 512 个字节（除了最后一个文件，使用 512K 表示 Kb，512M 表示 Mb）：

`split -b {{512}} {{文件名}}`

- 按照大小进行分包处理

`split -b 5G archive.tar.gz archive.tar.gz.`
