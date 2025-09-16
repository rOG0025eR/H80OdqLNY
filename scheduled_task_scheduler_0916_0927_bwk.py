# 代码生成时间: 2025-09-16 09:27:13
import requests
import schedule
import time
from threading import Thread

"""
定时任务调度器，用于定期执行HTTP请求任务。

Attributes:
    None

Methods:
    run_task: 定义要执行的任务
    schedule_tasks: 安排任务的调度计划
    start_scheduler: 开始执行调度任务
"""

class ScheduledTaskScheduler:
    def __init__(self):
        # 初始化调度器
        self.jobs = {}

    def run_task(self, url):
        """
        定义要执行的任务。
        向指定的URL发送GET请求。
        Args:
            url (str): 目标URL
        """
        try:
            response = requests.get(url)
            response.raise_for_status()  # 检查响应状态码
            print(f"请求成功，状态码：{response.status_code}")
        except requests.RequestException as e:
            print(f"请求失败：{e}")

    def schedule_tasks(self, url, interval):
        """
        安排任务的调度计划。
        Args:
            url (str): 目标URL
            interval (int): 任务执行的间隔时间（秒）
        """
        self.jobs[url] = schedule.every(interval).seconds.do(self.run_task, url=url)
        print(f"任务已安排，URL：{url}，间隔：{interval}秒")

    def start_scheduler(self):
        """
        开始执行调度任务。
        """
        while True:
            schedule.run_pending()
            time.sleep(1)

# 示例用法
if __name__ == '__main__':
    scheduler = ScheduledTaskScheduler()
    scheduler.schedule_tasks('https://api.example.com/data', 10)  # 每10秒执行一次任务
    t = Thread(target=scheduler.start_scheduler)
    t.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("调度器已停止")
