# run-clang-tidy.py

> 一个Python脚本，用于在项目上运行clang-tidy静态分析工具。
> 它可以帮助你自动检查代码中的潜在问题并提供修复建议。
> 更多信息：<https://clang.llvm.org/extra/clang-tidy/>.
> GitHub 地址：https://github.com/llvm/llvm-project  文件路径：clang-tools-extra/clang-tidy/tool/run-clang-tidy.py

- 具体使用方法
`python3 run-clang-tidy.py [选项] [文件/目录过滤]`
-checks=<规则>	指定启用的检查规则（如 -checks='modernize-*,clang-analyzer-*'）。
-fix	自动修复可修复的问题（需提前备份代码！）。
-p <build_dir>	指定编译数据库路径（默认从当前目录查找）。
-exclude=<正则表达式>	排除匹配的文件或目录（如 -exclude='.*/third_party/.*'）。
-output=<格式>	输出格式（如 -output=clang-warning 或 -output=json）。
-
-
- 全项目检查并生成报告，使用 4 线程，启用所有现代 C++ 检查项，结果输出到文件：

`python3 run-clang-tidy.py -j 4 -checks='modernize-*' -p build/ > clang-tidy-report.txt`

- 指定额外的检查项（例如，添加"checkName"检查）：

`python3 run-clang-tidy.py -p {{编译数据库路径}} -checks='-*,checkName' {{文件或目录}}`

- 排除测试代码，排除所有 test 目录下的文件：

`python3 run-clang-tidy.py -j 4 -exclude='.*/test/.*' -p build/`

- 仅显示发现的问题而不进行修复：

`python3 run-clang-tidy.py -p {{编译数据库路径}} -header-filter='.*' {{文件或目录}}`

- 将发现的问题输出到文件中：

`python3 run-clang-tidy.py -p {{编译数据库路径}} -export-fixes={{输出文件.yaml}} {{文件或目录}}`

- 显示帮助信息和可用选项：

`python3 run-clang-tidy.py --help`