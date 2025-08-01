# 代码生成时间: 2025-08-01 14:14:41
import requests
import json
import random
import string
from datetime import datetime, timedelta

"""
测试数据生成器

该模块用于生成模拟测试数据，包括随机字符串、数字和日期。
可以使用这些数据进行自动化测试。
"""

class TestDataGenerator:
    """
    测试数据生成器类
    """

    def __init__(self):
        pass

    def generate_random_string(self, length=10):
        """
        生成随机字符串
        :param length: 字符串长度
        :return: 随机字符串
        """
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

    def generate_random_number(self):
        """
        生成随机数字
        :return: 随机数字
        """
        return random.randint(1000, 9999)

    def generate_random_date(self, days_back=0):
        """
        生成随机日期
        :param days_back: 与当前日期的天数差
        :return: 随机日期
        """
        today = datetime.now()
        date = today - timedelta(days=random.randint(0, days_back))
        return date.strftime('%Y-%m-%d')

    def generate_test_data(self, data_type='string'):
        """
        生成测试数据
        :param data_type: 数据类型 (string, number, date)
        :return: 测试数据
        """
        if data_type == 'string':
            return self.generate_random_string()
        elif data_type == 'number':
            return self.generate_random_number()
        elif data_type == 'date':
            return self.generate_random_date()
        else:
            raise ValueError('Unsupported data type')

# 示例用法
if __name__ == '__main__':
    generator = TestDataGenerator()
    print('Random String: ', generator.generate_test_data('string'))
    print('Random Number: ', generator.generate_test_data('number'))
    print('Random Date: ', generator.generate_test_data('date'))
