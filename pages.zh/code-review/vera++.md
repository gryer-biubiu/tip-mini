# vera++
> Vera++ 是一个用于对 C/C++ 代码进行风格检查和潜在错误检测的工具。它有助于保持代码的一致性和高质量。
> 更多信息：[Vera++ GitHub](https://github.com/verateam/vera)

- 初始化一个新的规则集配置文件：

`vera++ --create-config`

- 对单个文件执行基本检查：

`vera++ yourfile.cpp`

- 使用特定规则集(Profile)检查代码：

`vera++ -P general yourfile.cpp`

- 忽略特定规则编号：

`vera++ -e W001 yourfile.cpp`

- 查看所有可用规则：

`vera++ --list`

- 检查多个文件或目录下的所有文件，并生成统计报告：

`vera++ path/to/your/sources/*.cpp --report`

- 应用自定义排除规则文件来跳过某些文件的检查：
- general为profiles目录下的规则集（具体参考github）
`vera++ -p general -r /path/to/rules -s -d -e -S --exclusions /path/to/exclusions_file`
-
-
-s：显示简短信息。
-d：显示详细的错误信息。
-e：忽略配置文件中的所有例外设置。
-S：输出统计信息。
--exclusions "exclusions_file"：指定一个排除文件，其中列出不需要进行检查的文件或目录。
-show-rules：列出所有可用规则。
-profile <profile.xml>：指定自定义规则配置文件。
-exclude dir/*：排除特定目录或文件。
-output report.txt：生成报告文件。
-p general：指定使用的规则集名称为 general。
-r "${rules_path} "：指定自定义规则集所在的目录。