# curl

> 向 / 从一个服务器传输数据。
> 支持大多数协议，包括 HTTP, FTP, 和 POP3.
> 更多信息：<https://curl.se/docs/manpage.html>.

-X: 指定请求方法（如 GET, POST, PUT, DELETE 等）。
-d: 在 HTTP 请求中提交数据。通常与 POST 或 PUT 方法一起使用。
-H: 添加 HTTP 头部信息。
-u: 提供用户名和密码用于 HTTP 基本认证。
-o: 将输出写入到文件而不是标准输出。
-L: 如果服务器报告重定向，则自动跟随。
-v: 显示请求和响应的详细信息，有助于调试。
-I: 只请求资源的头部信息。
-k: 对于 HTTPS 请求，允许 curl 忽略 SSL 证书问题。
-C: 断点续传功能，当下载中断后可以从断点继续。
-b: 使用指定的 cookie 发送请求或读取/写入 cookie 文件。
-c: 将响应中的 cookie 保存到指定文件。

- 发送 GET 请求到指定的 URL：
`curl {{URL}}`

- 下载文件并保存为指定名称：
`curl -o {{filename}} {{URL}}`

- 发送 POST 请求，并在请求体中包含数据：
`curl -X POST {{URL}} -d "{{data}}"`

- 上传文件到服务器（例如使用 PUT 方法）：
`curl -X PUT -T {{local_file_path}} {{URL}}`

- 发送带自定义头部的请求：
`curl -H "Content-Type: application/json" {{URL}}`

- 使用基本认证发送请求：
`curl -u {{username}}:{{password}} {{URL}}`

- 发送 JSON 数据作为请求体：
`curl -X POST -H "Content-Type: application/json" -d '{{json_data}}' {{URL}}`

- 跟随重定向（HTTP 3xx 响应码）：
`curl -L {{URL}}`

- 显示详细的请求和响应头信息：
`curl -v {{URL}}`

- 只下载响应头而不获取页面内容：
`curl -I {{URL}}`

- 设置超时时间（秒）：
`curl --max-time {{seconds}} {{URL}}`

- 断点续传下载大文件：
`curl -C - -O {{URL}}`

- 通过代理服务器发送请求：
`curl -x {{proxy_url}}:{{port}} {{URL}}`

- 忽略 SSL 证书验证（适用于自签名证书的情况，但不推荐用于生产环境）：
`curl -k {{HTTPS_URL}}`

- 同时进行多个下载（多线程下载）：
`curl -Z {{URL1}} {{URL2}} ...`

- 使用 cookie 进行请求：
`curl -b "cookie_name=cookie_value" {{URL}}`

- 保存响应 cookie 到文件（对于登录等操作有用）：
`curl -c {{cookie_jar_file}} {{URL}}`

- 读取本地 cookie 文件发送请求：
`curl -b {{cookie_jar_file}} {{URL}}`
