# bitbake

> Yocto Project 的核心构建工具。
> 用于解析配方（recipes）、处理依赖关系、编译代码、打包软件包等。
> 更多信息：<https://docs.yoctoproject.org/bitbake/>.

- 构建指定的包或镜像：
`bitbake {{package_or_image_name}}`

- 查看某个包的依赖树：
`bitbake -g {{package_or_image_name}}`

- 清理并重新构建指定的包或镜像：
`bitbake -c clean {{package_or_image_name}} && bitbake {{package_or_image_name}}`

- 只执行某个特定的任务（例如编译而不进行安装）：
`bitbake {{package_or_image_name}} -c {{task_name}}`

- 强制重新构建指定的包或镜像，忽略缓存：
`bitbake {{package_or_image_name}} -f`

- 编译并调试某一层中的所有包：
`bitbake -k world`

- 显示可用的构建目标：
`bitbake-layers show-recipes`

- 显示有关特定包的信息（包括版本、提供者等）：
`bitbake -s | grep {{package_name}}`

- 显示有关特定任务的信息：
`bitbake -c listtasks {{package_or_image_name}}`

- 生成 shell 环境脚本以便于交互式调试：
`bitbake -e {{package_or_image_name}} > environment.sh`

- 执行清理操作以释放磁盘空间：
`bitbake -c cleansstate {{package_or_image_name}}`

- 检查构建环境是否设置正确：
`bitbake -e | grep ^B`

- 启用更详细的日志输出：
`BBMASK="" bitbake {{package_or_image_name}} -D`

- 在遇到错误时停止构建而不是继续尝试其他任务：
`bitbake -k {{package_or_image_name}}` （注：去掉 `-k` 选项）

- 使用多个线程加速构建过程（根据 CPU 核心数调整数值）：
`PARALLEL_MAKE="-j{{number_of_cores}}" bitbake {{package_or_image_name}}`

- 查看和设置 BitBake 的配置变量：
编辑 `conf/local.conf` 文件，添加或修改变量。