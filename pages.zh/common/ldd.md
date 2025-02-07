# ldd

> 显示动态链接库依赖。
> 用于检查可执行文件或共享对象（.so 文件）依赖的共享库。
> 更多信息：<https://man7.org/linux/man-pages/man1/ldd.1.html>.

- 显示指定可执行文件或共享对象的依赖库：

`ldd {{path/to/executable_or_shared_object}}`

- 检查标准输入中的每个文件的依赖库（通常与 echo 或者其他命令结合使用）：

`ldd {{path/to/file}}`

- 强制 ldd 使用特定的动态链接器：

`LD_USE_LOAD_BIAS=1 ldd {{path/to/executable_or_shared_object}}`

- 只显示直接依赖的共享库，而不包括间接依赖：

`ldd --list {{path/to/executable_or_shared_object}} | grep '=>'`

- 显示详细的调试信息（对于诊断问题很有用）：

`ldd --verbose {{path/to/executable_or_shared_object}}`

- 检查是否存在缺失的依赖库（如果输出中出现 "not found" 则表示存在缺失库）：

`ldd {{path/to/executable_or_shared_object}}`

- 在容器或者 chroot 环境中使用 ldd 时，确保正确的 glibc 和其他必要的库被包含在环境中。