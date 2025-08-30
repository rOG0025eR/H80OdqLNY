# 代码生成时间: 2025-08-31 04:50:48
import json
import requests

"""
JSON数据格式转换器

这个程序使用requests框架从一个URL获取JSON数据，
然后将其转换为指定的格式并打印出来。
"""


class JSONConverter:
    def __init__(self, url, output_format='pretty'):
        self.url = url
        self.output_format = output_format

    def fetch_json(self):
        """
        从指定的URL获取JSON数据
        """
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # 检查请求是否成功
            return response.json()
        except requests.RequestException as e:
            print(f"请求错误: {e}")
            return None

    def convert_json(self, data, format='pretty'):
        """
        将JSON数据转换为指定的格式
        """
        if data is None:
            return None

        if format == 'pretty':
            return json.dumps(data, indent=4, ensure_ascii=False)
        elif format == 'compact':
            return json.dumps(data, ensure_ascii=False)
        else:
            print("不支持的格式")
            return None

    def run(self):
        """
        运行JSON转换器，从URL获取数据并转换
        """
        data = self.fetch_json()
        if data:
            converted_data = self.convert_json(data, self.output_format)
            if converted_data:
                print(converted_data)

# 示例用法
if __name__ == '__main__':
    url = 'http://your-api-url.com/data'  # 替换为实际的API URL
    converter = JSONConverter(url, output_format='pretty')
    converter.run()