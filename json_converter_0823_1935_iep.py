# 代码生成时间: 2025-08-23 19:35:10
import json
import requests

"""
JSON数据格式转换器

该程序使用requests框架来发送HTTP请求，并从API接收JSON数据。
然后，它将接收到的JSON数据转换为另一种格式（如字符串或Python字典）。

属性:
- url: 要请求的API的URL。
- data: 要发送给API的数据。
- json_format: 转换后的数据格式。
"""

class JSONConverter:
    def __init__(self, url):
        """初始化JSONConverter类。"""
        self.url = url

    def convert_json(self, data, json_format='string'):
        """将JSON数据转换为指定格式。"""
        try:
            # 发送POST请求
            response = requests.post(self.url, json=data)
            # 检查响应状态码
            response.raise_for_status()
            # 将JSON响应数据转换为指定格式
            if json_format == 'string':
                return json.dumps(response.json())
            elif json_format == 'dict':
                return response.json()
            else:
                return f"Unsupported format: {json_format}"
        except requests.RequestException as e:
            # 处理请求异常
            return f"Request error: {e}"
        except json.JSONDecodeError as e:
            # 处理JSON解析异常
            return f"JSON decode error: {e}"
        except Exception as e:
            # 处理其他异常
            return f"Unexpected error: {e}"

# 示例用法
if __name__ == '__main__':
    url = 'https://api.example.com/data'
    data = {'key': 'value'}
    converter = JSONConverter(url)
    
    # 将JSON数据转换为字符串
    json_string = converter.convert_json(data, 'string')
    print(json_string)

    # 将JSON数据转换为字典
    json_dict = converter.convert_json(data, 'dict')
    print(json_dict)