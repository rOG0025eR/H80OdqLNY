# 代码生成时间: 2025-09-11 07:32:22
import requests
import psutil
import json

# 定义一个系统性能监控工具类
class SystemPerformanceMonitor:
    """监控系统性能。"""

    def __init__(self, url):
        """初始化监控工具。"""
        self.url = url

    def get_cpu_usage(self):
        """获取CPU使用率。"""
        return psutil.cpu_percent(interval=1)

    def get_memory_usage(self):
        """获取内存使用情况。"""
        memory = psutil.virtual_memory()
        return memory.percent, memory.total, memory.used, memory.free

    def get_disk_usage(self):
        """获取磁盘使用情况。"""
        disk = psutil.disk_usage('/')
        return disk.percent, disk.total, disk.used, disk.free

    def get_network_usage(self):
        """获取网络使用情况。"""
        network_io = psutil.net_io_counters()
        return network_io.bytes_sent, network_io.bytes_recv

    def send_data_to_server(self, data):
        """将监控数据发送到服务器。"""
        try:
            response = requests.post(self.url, json=data)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error sending data to server: {e}")

    def monitor_and_send(self):
        """监控系统性能并发送数据到服务器。"""
        data = {
            "cpu_usage": self.get_cpu_usage(),
            "memory_usage": self.get_memory_usage(),
            "disk_usage": self.get_disk_usage(),
            "network_usage": self.get_network_usage()
        }
        return self.send_data_to_server(data)

# 主函数
if __name__ == "__main__":
    # 服务器URL
    server_url = "http://your-server-url.com/monitor"

    # 创建监控工具实例
    monitor = SystemPerformanceMonitor(server_url)

    # 监控并发送数据
    result = monitor.monitor_and_send()
    print(json.dumps(result, indent=4))
