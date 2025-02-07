ruyi.gao@BionicPlatDev:~$ tip Dockerfile
# Dockerfile

> Docker镜像构建脚本。
> 包含一系列指令，用于定义如何创建一个 Docker 镜像。
> 更多信息：<https://docs.docker.com/engine/reference/builder/>.

- 指定基础镜像（所有 Dockerfile 必须以 FROM 开始）：

`FROM {{base_image}}`

- 维护者信息（可选，推荐使用 LABEL 替代）：

`LABEL maintainer="your_email@example.com"`

- 设置环境变量：

`ENV {{key}}={{value}}`

- 将本地文件或目录复制到容器中：

`COPY {{source_path}} {{destination_path}}`

- 在构建过程中执行命令（每条 RUN 指令都会创建一个新的层）：

`RUN {{command}}`

- 暴露端口（仅标记该端口，实际映射在运行时设置）：

`EXPOSE {{port_number}}`

- 设置容器启动时默认执行的命令：

`CMD ["{{executable}}", "{{param1}}", "{{param2}}"]`

- 定义要运行的可执行文件或命令，覆盖 CMD：

`ENTRYPOINT ["{{executable}}", "{{param1}}", "{{param2}}"]`

- 设置工作目录（相当于 cd 命令）：

`WORKDIR /path/to/workdir`

- 安装软件包管理器中的软件包（对于 Debian/Ubuntu 基础镜像）：

`RUN apt-get update && apt-get install -y \
    {{package_name_1}} \
    {{package_name_2}} \
    && rm -rf /var/lib/apt/lists/*`

- 替换下载源
`RUN sed -i 's|http://pub.crdc.hirain.com/ubuntu|https://mirrors.hirain.com/repository/Ubuntu/|g' /etc/apt/sources.list && \`

- 下载远程文件到镜像中：

`ADD {{source_url_or_path}} {{destination_path}}`

- 执行构建时的 shell 脚本：

`RUN chmod +x /path/to/script.sh && /path/to/script.sh`

- 定义匿名卷（数据卷），确保数据持久化：

`VOLUME ["/path/to/volume"]`

- 使用 ARG 指令定义构建参数，在构建时可以传递值给它：

`ARG {{variable_name}}`

- 为镜像添加元数据标签：

`LABEL {{key}}="{{value}}"`

- 禁止交互命令

`ENV DEBIAN_FRONTEND=noninteractive`

- 根据Dockerfile创建镜像，Dockerfile文件和当前目录对应
`docker build -t ubuntu_test:1.0.0 .`