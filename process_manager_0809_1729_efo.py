# 代码生成时间: 2025-08-09 17:29:11
import os
import subprocess
import sys

"""
进程管理器
这个模块提供进程管理功能，包括启动、停止和查看进程列表。
"""


class ProcessManager:
    """
    进程管理器类
    提供进程管理功能，包括启动、停止和查看进程列表。
    """

    def __init__(self):
        """
        初始化进程管理器
        """
        self.process_list = {}

    def start_process(self, name, command):
        """
        启动一个进程
        :param name: 进程名称
        :param command: 要执行的命令
        """
        try:
            process = subprocess.Popen(command, shell=True)
            self.process_list[name] = process
            print(f"Process {name} started with PID {process.pid}")
        except Exception as e:
            print(f"Failed to start process {name}: {e}")

    def stop_process(self, name):
        """
        停止一个进程
        :param name: 进程名称
        """
        process = self.process_list.get(name)
        if process:
            try:
                process.terminate()
                process.wait()
                print(f"Process {name} stopped")
            except Exception as e:
                print(f"Failed to stop process {name}: {e}")
        else:
            print(f"Process {name} not found")

    def list_processes(self):
        """
        列出所有进程
        """
        print("Running processes:")
        for name, process in self.process_list.items():
            print(f"{name} (PID: {process.pid})")

    def handle_signal(self, sig, frame):
        """
        处理信号，用于优雅地关闭进程
        """
        print("Shutting down...")
        for process in self.process_list.values():
            process.terminate()
            process.wait()
        sys.exit(0)

if __name__ == "__main__":
    """
    主函数
    """
    manager = ProcessManager()
    manager.start_process("example", "sleep 10")
    manager.list_processes()
    
    # 注册信号处理器
    signal.signal(signal.SIGINT, manager.handle_signal)
    signal.signal(signal.SIGTERM, manager.handle_signal)
    
    # 等待信号
    signal.pause()