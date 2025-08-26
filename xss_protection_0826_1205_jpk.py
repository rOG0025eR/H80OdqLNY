# 代码生成时间: 2025-08-26 12:05:21
import re
import html

from flask import Flask, request, escape

# 初始化 Flask 应用
app = Flask(__name__)

# 定义一个简单的 XSS 过滤器
def xss_filter(data):
    # 转义 HTML 特殊字符以防止 XSS 攻击
    return html.escape(data)

# 路由：用于接收用户输入
@app.route("/input", methods=["GET", "POST"])
def input_handler():
    if request.method == "POST":
        # 获取用户输入并应用 XSS 过滤器
        user_input = request.form.get("user_input", "")
        safe_input = xss_filter(user_input)
        # 返回处理后的安全输出
        return f"<h1>Received: {safe_input}</h1>"
    else:
        # 如果是 GET 请求，返回输入表单
        return "<form method='post'><input type='text' name='user_input'><button type='submit'>Submit</button></form>"

# 错误处理：捕获并处理异常
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404 Page Not Found</h1>", 404

@app.errorhandler(500)
def internal_server_error(e):
    return "<h1>500 Internal Server Error</h1>", 500

# 运行 Flask 应用
if __name__ == '__main__':
    app.run(debug=True)
