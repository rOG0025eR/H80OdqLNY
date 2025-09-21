# 代码生成时间: 2025-09-21 19:39:04
import requests
import json

"""
API响应格式化工具，用于格式化API响应数据。
"""

class ApiResponseFormatter:
    """API响应格式化类"""

def __init__(self, base_url):
    """初始化函数"""
    self.base_url = base_url
    """API的基础URL"""

def format_response(self, endpoint, method='GET', params=None, data=None, headers=None):
    """格式化API响应数据"""
    if method.upper() not in ['GET', 'POST', 'PUT', 'DELETE']:
        raise ValueError('Unsupported HTTP method')

    url = f"{self.base_url}/{endpoint}"
    response = requests.request(method, url, params=params, data=data, headers=headers)
    """发送HTTP请求并获取响应"""

    try:
        # 尝试解析JSON响应内容
        response_data = response.json()
    except ValueError:
        # 如果响应内容不是JSON格式，返回原始响应内容
        response_data = response.text

    # 格式化响应数据
    formatted_data = self._format_data(response_data)
    return formatted_data

def _format_data(self, data):
    """格式化响应数据"""
    if isinstance(data, dict):
        # 如果数据是字典，递归格式化每个键值对
        return {key: self._format_data(value) for key, value in data.items()}
    elif isinstance(data, list):
        # 如果数据是列表，递归格式化每个元素
        return [self._format_data(item) for item in data]
    else:
        # 如果数据是其他类型，直接返回
        return data

def main():
    """主函数，用于测试API响应格式化工具"""
    base_url = 'https://api.example.com'
    formatter = ApiResponseFormatter(base_url)

    endpoint = 'users'
    method = 'GET'
    params = {'limit': 10}
    headers = {'Authorization': 'Bearer token'}

    try:
        formatted_data = formatter.format_response(endpoint, method, params, headers=headers)
        print('Formatted Response:', formatted_data)
    except Exception as e:
        print('Error:', str(e))
def __name__ == '__main__':
    main()