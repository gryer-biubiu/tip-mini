# lizard
> lizard 是一个用于计算代码复杂度的开源工具，支持多种编程语言。它能够分析源代码并报告如圈复杂度（cyclomatic complexity）、函数长度（NLOC）等指标，有助于提升代码质量和可维护性。
> 更多信息：[Lizard GitHub](https://github.com/terryyin/lizard)
> 
- 对指定路径下的代码进行分析：
`lizard path/to/your/code/or/file`

- 对单个文件或整个项目执行基本检查，并将输出重定向到文件中：
`lizard path/to/your/code/or/file > output.txt`

- 分析特定语言（例如 C 和 C++）的代码，并设置圈复杂度和函数参数数量的阈值：
`lizard -l cpp -l c -C 6 -t 3 path/to/your/code`

- 使用自定义阈值来标记超过特定 NLOC 或圈复杂度的函数：
`lizard -T nloc=100 -T cyclomatic_complexity=20 path/to/your/code`

- 排除某些目录或文件模式，避免分析测试代码或自动生成的代码：
`lizard -x"*/tests/*" -x"*.pb.*" path/to/your/code`

- 查看 lizard 支持的所有命令行选项和参数：
`lizard --help`

- 检查多个文件或目录下的所有文件，并排除特定路径，同时生成统计信息：
`lizard -x"${WORKSPACE}/build*" -x"${WORKSPACE}/services/*" path/to/your/sources/*.cpp --warnings_only`

- 应用复杂的过滤器集，包括排除特定规则、目录和文件，以及调整输出格式：
`lizard -l cpp -l c -L 100 -C 6 -a 10 -t 3 -T nloc=100 -x"*/stub/*" -x"*/tests/*" -x"*.pb.*" -x"${WORKSPACE}/build*" -x"${WORKSPACE}/diffsys/*" "${WORKSPACE}" > "${OUTPUT_FILE}"`
-
-
-l：指定要分析的语言。
-L：设置圈复杂度的阈值。
-C：每个函数允许的最大参数数量。
-a：设置平均 NLOC 的最大允许值。
-t：每个函数的最大允许参数数量。
-T：为不同的复杂度指标设定阈值。
-x：排除特定路径或文件模式。
"${WORKSPACE}"：指定要分析的代码根目录。
"${OUTPUT_FILE}"：将输出重定向到指定的文件。