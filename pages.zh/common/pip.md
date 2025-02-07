# pip

> Python 包管理工具。
> 用于安装和管理 Python 软件包，从 Python Package Index (PyPI) 或其他包索引中获取。
> 更多信息：<https://pip.pypa.io>.

- 安装一个包：

`pip install {{package_name}}`

- 卸载一个包：

`pip uninstall {{package_name}}`

- 显示已安装包的列表：

`pip list`

- 显示有关一个包的信息：

`pip show {{package_name}}`

- 使用 requirements 文件安装多个包：

`pip install -r requirements.txt`

- 安装指定版本的包：

`pip install {{package_name}}=={{version_number}}`

- 安装特定版本以上的包：

`pip install {{package_name}}>={{version_number}}`

- 创建或更新 requirements 文件以包含当前环境中所有包及其版本：

`pip freeze > requirements.txt`

- Hirain 内源 --retries 10 可以增加延时时间和次数

`pip install -i https://mirrors.hirain.com/repository/Pypi/simple --trusted-host mirrors.hirain.com {{package_name}}`
