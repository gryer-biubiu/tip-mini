# CTest
> 一个用于管理和运行项目测试的工具，集成于 CMake 中。 支持并行执行、过滤测试、输出格式化等功能，适用于自动化测试流程。
> 更多信息：https://cmake.org/cmake/help/latest/manual/ctest.1.html

- 启用测试并在 CMakeLists.txt 中添加一个测试：
`enable_testing()`
`add_test(NAME MyUnitTest COMMAND MyUnitTestExecutable)`

- 在构建目录下配置并编译项目后运行所有测试
`mkdir build && cd build`
`cmake ..`
`ctest -T test --timeout 300`

- 执行 CTest 运行测试，不压缩输出并设置单个测试超时时间为 600 秒`
`ctest -T test --no-compress-output --timeout 600`


- 以详细模式运行测试，并指定输出为 XML 格式
`ctest -T test --timeout 300 --output-on-failure -R MyUnitTest --test-output-size-max 1024 -O MyUnitTestOutput.xml`
-R MyUnitTest: 运行名称匹配 MyUnitTest 的测试。
--output-on-failure: 在测试失败时显示输出。
--test-output-size-max 1024: 设置最大输出大小为 1024 字节。
-O MyUnitTestOutput.xml: 将输出重定向到指定的 XML 文件中。

- 使用 xsltproc 工具将 CTest 生成的测试结果 XML 文件转换为 JUnit 格式的 XML 文件。(具体用法tip xsltproc)
- 通常是为了使这些测试结果能够在支持 JUnit 格式的工具（如 Jenkins、GitLab CI 等持续集成系统）中被解析和展示。
`xsltproc transform.xsl example.xml > output.html`