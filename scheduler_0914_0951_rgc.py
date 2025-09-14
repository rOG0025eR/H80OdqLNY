# 代码生成时间: 2025-09-14 09:51:05
import requests
import schedule
import time
from threading import Thread

"""
定时任务调度器
功能说明：
1. 使用schedule库进行定时任务调度
2. 使用requests库发送HTTP请求
3. 捕获并处理异常
"""

# 全局变量
SCHEDULER = schedule.Scheduler()


def job_function():
    """
    定时任务函数
    说明：
    1. 使用requests库发送GET请求
    2. 打印响应内容
    3. 捕获并处理异常
    """
    try:
        # 发送GET请求
        response = requests.get("http://example.com/api/")
        # 打印响应内容
        print(response.text)
    except requests.exceptions.RequestException as e:
        # 打印异常信息
        print(f"请求异常：{e}")


def start_scheduler():
    """
    启动定时任务调度器
    说明：
    1. 使用schedule库添加定时任务
    2. 启动调度器
    """
    # 添加定时任务，每10秒执行一次job_function函数
    SCHEDULER.every(10).seconds.do(job_function)
    # 启动调度器
    SCHEDULER.start()
    print("定时任务调度器启动成功")


def run_in_background():
    """
    在后台线程中运行调度器
    """
    thread = Thread(target=start_scheduler)
    thread.daemon = True
    thread.start()

if __name__ == '__main__':
    # 在后台线程中运行调度器
    run_in_background()
    # 阻塞主线程，防止程序退出
    while True:
        time.sleep(1)