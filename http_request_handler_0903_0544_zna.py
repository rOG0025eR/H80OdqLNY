# 代码生成时间: 2025-09-03 05:44:20
import requests
from flask import Flask, request, jsonify

"""
HTTP请求处理器
"""

app = Flask(__name__)

"""
处理GET请求
"""
@app.route('/get', methods=['GET'])
def handle_get_request():
    # 获取查询参数
    query_params = request.args
    # 构造响应数据
    response_data = {
        'method': 'GET',
        'query_params': dict(query_params)
    }
    return jsonify(response_data)

"""
处理POST请求
"""
@app.route('/post', methods=['POST'])
def handle_post_request():
    try:
        # 获取JSON数据
        json_data = request.get_json()
        # 构造响应数据
        response_data = {
            'method': 'POST',
            'json_data': json_data
        }
        return jsonify(response_data)
    except Exception as e:
        # 错误处理
        error_response = {
            'error': str(e)
        }
        return jsonify(error_response), 400

"""
启动Flask应用
"""
if __name__ == '__main__':
    app.run(debug=True)