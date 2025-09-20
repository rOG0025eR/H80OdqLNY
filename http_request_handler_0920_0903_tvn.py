# 代码生成时间: 2025-09-20 09:03:15
import requests

"""
HTTP请求处理器模块，用于发送HTTP请求并处理响应。
"""

class HttpRequestHandler:
    def __init__(self, base_url):
        """初始化请求处理器，设置基础URL。

        :param base_url: 基础URL
        """
        self.base_url = base_url

    def send_request(self, endpoint, method, headers=None, params=None, data=None):
        """发送HTTP请求。

        :param endpoint: 请求的终点（路径）
        :param method: 请求方法（GET, POST, PUT, DELETE等）
        :param headers: 请求头
        :param params: 请求参数
        :param data: 请求体
        :return: 响应对象
        """
        try:
            if method.upper() == 'GET':
                response = requests.get(self.base_url + endpoint, headers=headers, params=params)
            elif method.upper() == 'POST':
                response = requests.post(self.base_url + endpoint, headers=headers, params=params, data=data)
            elif method.upper() == 'PUT':
                response = requests.put(self.base_url + endpoint, headers=headers, params=params, data=data)
            elif method.upper() == 'DELETE':
                response = requests.delete(self.base_url + endpoint, headers=headers, params=params)
            else:
                raise ValueError(f"Unsupported method: {method}")

            response.raise_for_status()  # 检查响应状态码
            return response
        except requests.RequestException as e:
            print(f"Request failed: {e}")
            return None

    def get(self, endpoint, headers=None, params=None):
        """发送GET请求。

        :param endpoint: 请求的终点（路径）
        :param headers: 请求头
        :param params: 请求参数
        :return: 响应对象
        """
        return self.send_request(endpoint, 'GET', headers=headers, params=params)

    def post(self, endpoint, headers=None, params=None, data=None):
        """发送POST请求。

        :param endpoint: 请求的终点（路径）
        :param headers: 请求头
        :param params: 请求参数
        :param data: 请求体
        :return: 响应对象
        """
        return self.send_request(endpoint, 'POST', headers=headers, params=params, data=data)

    def put(self, endpoint, headers=None, params=None, data=None):
        """发送PUT请求。

        :param endpoint: 请求的终点（路径）
        :param headers: 请求头
        :param params: 请求参数
        :param data: 请求体
        :return: 响应对象
        """
        return self.send_request(endpoint, 'PUT', headers=headers, params=params, data=data)

    def delete(self, endpoint, headers=None, params=None):
        """发送DELETE请求。

        :param endpoint: 请求的终点（路径）
        :param headers: 请求头
        :param params: 请求参数
        :return: 响应对象
        """
        return self.send_request(endpoint, 'DELETE', headers=headers, params=params)

# 示例用法
if __name__ == '__main__':
    base_url = 'https://jsonplaceholder.typicode.com'
    handler = HttpRequestHandler(base_url)
    
    # 发送GET请求
    response = handler.get('/posts/1')
    if response:
        print(response.json())
    
    # 发送POST请求
    post_data = {'title': 'foo', 'body': 'bar', 'userId': 1}
    response = handler.post('/posts', data=post_data)
    if response:
        print(response.json())
    
    # 发送PUT请求
    put_data = {'title': 'foo updated', 'body': 'bar updated', 'userId': 1}
    response = handler.put('/posts/1', data=put_data)
    if response:
        print(response.json())
    
    # 发送DELETE请求
    response = handler.delete('/posts/1')
    if response:
        print(response.json())