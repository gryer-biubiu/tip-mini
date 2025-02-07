# Yocto Project

> 开源协作项目，用于创建高度定制化的 Linux 发行版。
> 提供了一套完整的工具链、构建系统（BitBake）、元数据（recipes 和 layers）以及文档。
> 更多信息：<https://www.yoctoproject.org>.
> 汇总和集成和一次性编译所有程序

- 初始化 Yocto 构建环境：
`source {{yocto_setup_script}}`

- 更新 BitBake 配置并获取最新的层（layers）：
`repo sync`

- 构建一个完整的镜像（例如 core-image-minimal）：
`bitbake {{image_name}}`

- 查看所有可用的镜像和包：
`bitbake -s`
`bitbake-layers show-recipes`

- 添加额外的层到构建配置中：
`bitbake-layers add-layer {{path/to/layer}}`

- 移除不再需要的层：
`bitbake-layers remove-layer {{path/to/layer}}`

- 创建自定义配置文件以覆盖默认设置（如机器配置、distro 特性等）：
编辑 `conf/local.conf` 文件添加或修改配置项。

- 启用调试功能以便更容易地进行故障排除：
在 `conf/local.conf` 中添加 `DEBUG_BUILD = "1"`

- 构建特定的软件包而不是整个镜像：
`bitbake {{package_name}}`

- 清理某个软件包或镜像的构建产物：
`bitbake -c clean {{package_or_image_name}}`

- 重新构建某个软件包或镜像而不使用缓存：
`bitbake -c cleansstate {{package_or_image_name}} && bitbake {{package_or_image_name}}`

- 使用 SDK 进行开发：
`./{{image_name}}-toolchain.sh`

- 打包 SDK 以便分发给其他开发者：
`bitbake -c populate_sdk {{image_name}}`

- 在不完全重建的情况下更新镜像中的单个包：
`bitbake -c deploy_update {{package_name}}`

- 生成补丁以提交上游贡献：
`devtool modify {{package_name}}`
`devtool finish {{package_name}} {{layer_path}}`

- 搜索可用的包或配方：
`bitbake-layers show-recipes | grep {{search_term}}`
`bitbake-layers search {{package_or_recipe_name}}`

- 构建完成后查看生成的映像和日志：
检查 `tmp/deploy/images/{{machine_name}}/` 目录下的文件。