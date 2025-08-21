# 代码生成时间: 2025-08-22 00:32:21
import requests
import json

# 配置测试服务器的URL和请求参数
TEST_URL = 'http://api.example.com/endpoint'
HEADERS = {'Content-Type': 'application/json'}

# 集成测试工具类
class IntegrationTestTool:
    def __init__(self, test_url, headers):
        self.test_url = test_url
        self.headers = headers

    def send_request(self, method, data=None):
        """
        发送HTTP请求到测试服务器
        :param method: 请求方法（GET, POST, PUT, DELETE等）
        :param data: 请求体数据，对于GET请求可以为None
        :return: 响应对象
        """
        try:
            if method.upper() == 'GET':
                response = requests.get(self.test_url, headers=self.headers)
            elif method.upper() == 'POST':
                response = requests.post(self.test_url, headers=self.headers, data=json.dumps(data))
            elif method.upper() == 'PUT':
                response = requests.put(self.test_url, headers=self.headers, data=json.dumps(data))
            elif method.upper() == 'DELETE':
                response = requests.delete(self.test_url, headers=self.headers)
            else:
                raise ValueError(f'Unsupported method: {method}')

            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f'Request failed: {e}')
            return None

    def test_get_request(self):
        """
        测试GET请求
        """
        print('Testing GET request...')
        response = self.send_request('GET')
        if response:
            print('GET response status code:', response.status_code)
            print('GET response body:', response.text)

    def test_post_request(self, data):
        """
        测试POST请求
        :param data: 要发送的数据
        """
        print('Testing POST request...')
        response = self.send_request('POST', data)
        if response:
            print('POST response status code:', response.status_code)
            print('POST response body:', response.text)

# 使用示例
if __name__ == '__main__':
    test_tool = IntegrationTestTool(TEST_URL, HEADERS)
    test_tool.test_get_request()
    test_data = {'key': 'value'}
    test_tool.test_post_request(test_data)