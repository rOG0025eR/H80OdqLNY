# 代码生成时间: 2025-08-27 23:04:25
import psutil
import sys
import subprocess

"""
A simple process manager written in Python using the psutil library.
This script allows the user to list, kill, and start processes.
"""

class ProcessManager:
    def __init__(self):
        """Initialize the process manager."""
        self.processes = []

    def list_processes(self):
        """List all running processes with their PIDs and names."""
        self.processes = []
        for proc in psutil.process_iter(['pid', 'name']):
            try:
                process_info = proc.info
                self.processes.append((process_info['pid'], process_info['name']))
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        for pid, name in self.processes:
            print(f"PID: {pid}, Name: {name}")

    def kill_process(self, pid):
        """Kill a process by its PID."""
        try:
            process = psutil.Process(pid)
            process.terminate()
            process.wait()
            print(f"Process {pid} has been terminated.")
        except psutil.NoSuchProcess:
            print(f"No process with PID {pid} found.")
        except psutil.AccessDenied:
            print(f"Permission denied to terminate process {pid}.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def start_process(self, command):
        """Start a new process with the given command."""
        try:
            subprocess.Popen(command, shell=True)
            print(f"Process started with command: {command}")
        except Exception as e:
            print(f"An error occurred: {e}")

def main():
    manager = ProcessManager()
    if len(sys.argv) < 2:
        print("Usage: python process_manager.py <command>")
        return

    command = ' '.join(sys.argv[1:])
    if command.startswith("list"):
        manager.list_processes()
    elif command.startswith("kill"):
        if len(sys.argv) < 3:
            print("Please provide a PID to kill.")
            return
        pid = int(sys.argv[2])
        manager.kill_process(pid)
    elif command.startswith("start"):
        manager.start_process(command.split(" ", 1)[1])
    else:
        print("Invalid command. Please use 'list', 'kill <PID>', or 'start <command>'.")

if __name__ == "__main__":
    main()