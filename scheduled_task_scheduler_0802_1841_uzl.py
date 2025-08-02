# 代码生成时间: 2025-08-02 18:41:04
import requests
import schedule
import time
from datetime import datetime

"""
定时任务调度器，使用schedule库来安排定时任务。
这个脚本将演示如何使用requests框架在指定时间点发送HTTP请求。
"""

# 定义一个函数，用于发送HTTP请求
def job():
    """发送HTTP请求的函数"""
    print(f"Job executed at {datetime.now()}
")
    try:
        # 可以替换为实际的URL和请求方法
        response = requests.get('https://httpbin.org/get')
        response.raise_for_status()
        print(f"Response from server: {response.json()}
")
    except requests.RequestException as e:
        print(f"An error occurred: {e}
")

# 使用schedule库安排任务
schedule.every(10).minutes.do(job)  # 每10分钟执行一次job函数

# 阻塞主线程，持续运行调度器
while True:
    schedule.run_pending()
    time.sleep(1)  # 避免CPU占用过高
