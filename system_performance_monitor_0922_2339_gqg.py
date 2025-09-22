# 代码生成时间: 2025-09-22 23:39:45
import psutil
import requests
import time
from datetime import datetime

"""
System Performance Monitoring Tool
This tool monitors system performance metrics such as CPU usage, memory usage,
disk usage, and network usage. It sends these metrics to a remote server
using the requests library.

Attributes:
    None

Methods:
    monitor_system_performance(): Monitors and sends system performance metrics.

Example:
    >>> monitor_system_performance()

Note:
    This tool assumes that the remote server is listening on port 8080
    and accepts JSON data.
"""

def monitor_system_performance():
    """Monitors and sends system performance metrics."""
    while True:
        try:
            # Get CPU usage percentage
            cpu_usage = psutil.cpu_percent(interval=1)

            # Get memory usage
            memory = psutil.virtual_memory()
            memory_usage = memory.percent
            memory_free = memory.available

            # Get disk usage
            disk = psutil.disk_usage('/')
            disk_usage = disk.percent
            disk_free = disk.free

            # Get network usage
            network = psutil.net_io_counters()
            network_sent = network.bytes_sent
            network_recv = network.bytes_recv

            # Create a dictionary to store the metrics
            metrics = {
                'timestamp': datetime.now().isoformat(),
                'cpu_usage': cpu_usage,
                'memory_usage': memory_usage,
                'memory_free': memory_free / (1024 ** 3),  # Convert to GB
                'disk_usage': disk_usage,
                'disk_free': disk_free / (1024 ** 3),  # Convert to GB
                'network_sent': network_sent,
                'network_recv': network_recv
            }

            # Send the metrics to the remote server
            response = requests.post('http://localhost:8080/metrics', json=metrics)

            # Check if the request was successful
            if response.status_code == 200:
                print(f'Metrics sent successfully: {metrics}')
            else:
                print(f'Failed to send metrics: {response.text}')

        except requests.exceptions.RequestException as e:
            print(f'Error sending metrics: {e}')
        except Exception as e:
            print(f'Error monitoring system performance: {e}')

        # Wait for 10 seconds before sending the next set of metrics
        time.sleep(10)

if __name__ == '__main__':
    monitor_system_performance()
