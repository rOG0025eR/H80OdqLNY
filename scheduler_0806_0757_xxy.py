# 代码生成时间: 2025-08-06 07:57:47
import requests
import schedule
import time

"""
定时任务调度器
"""

# 定义一个任务函数，这里以发送HTTP请求为例
def job_task():
    """发送GET请求的任务函数"""
    url = 'http://example.com/api'  # 这里替换成目标API的URL
    try:
        response = requests.get(url)
        response.raise_for_status()  # 如果响应状态码不是200，抛出异常
        print('任务执行成功，响应内容：', response.text)
    except requests.RequestException as e:
        print('任务执行失败：', e)

# 设置定时任务
schedule.every(10).minutes.do(job_task)  # 每10分钟执行一次job_task函数

"""
主函数，用于启动调度器和保持程序运行
"""
def main():
    print('定时任务调度器启动...')
    while True:
        schedule.run_pending()  # 执行即将到来的任务
        time.sleep(1)  # 休眠1秒，避免CPU占用过高

if __name__ == '__main__':
    main()
