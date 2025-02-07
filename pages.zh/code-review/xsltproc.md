# xsltproc

> 一个命令行工具，用于应用XSLT样式表到XML文档上。
> 更多信息：<http://xmlsoft.org/XSLT/xsltproc2.html>.

- 应用XSLT样式表转换XML文档：

`xsltproc {{样式表.xsl}} {{输入文件.xml}} -o {{输出文件.html}}`

- 直接显示转换结果而不保存到文件：

`xsltproc {{样式表.xsl}} {{输入文件.xml}}`

- 显示版本信息：

`xsltproc --version`

- 设置参数给XSLT样式表（例如，传递一个名为"paramName"的参数和值"paramValue"）：

`xsltproc --stringparam paramName paramValue {{样式表.xsl}} {{输入文件.xml}} -o {{输出文件.html}}`