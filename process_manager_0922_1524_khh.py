# 代码生成时间: 2025-09-22 15:24:42
import psutil
import sys

"""
A simple process manager implemented with Python and the psutil library.
It allows users to list, kill, and search for processes.
"""

class ProcessManager:
    """Class to manage system processes."""

    def __init__(self):
        # Initialize the process manager
        pass

    def list_processes(self):
        """
        List all running processes with their PID, name, and status.
        Returns a list of tuples containing process information.
        """
        processes = []
        for proc in psutil.process_iter(['pid', 'name', 'status']):
            try:
                processes.append((proc.info['pid'], proc.info['name'], proc.info['status']))
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                # Handle exceptions related to process access and iteration
                continue
        return processes

    def kill_process(self, pid):
        """
        Attempt to kill a process by its PID.
        Raises an exception if the process does not exist or cannot be killed.
        """
        try:
            process = psutil.Process(pid)
            process.terminate()
            process.wait()  # Wait for the process to terminate
            return True
        except psutil.NoSuchProcess:
            raise ValueError(f"Process with PID {pid} does not exist.")
        except psutil.AccessDenied:
            raise PermissionError(f"Access denied to terminate process with PID {pid}.")
        except Exception as e:
            raise e

    def search_for_processes(self, name):
        """
        Search for processes with a matching name.
        Returns a list of PIDs for processes matching the given name.
        """
        matching_processes = []
        for proc in psutil.process_iter(['pid', 'name']):
            try:
                if proc.info['name'] == name:
                    matching_processes.append(proc.info['pid'])
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
        return matching_processes

if __name__ == '__main__':
    # Create an instance of the ProcessManager
    manager = ProcessManager()

    # Example usage of the ProcessManager
    try:
        # List all processes
        processes = manager.list_processes()
        for pid, name, status in processes:
            print(f"PID: {pid}, Name: {name}, Status: {status}")

        # Kill a specific process by PID
        # manager.kill_process(1234)  # Uncomment and replace with a valid PID to kill a process

        # Search for processes by name
        # process_pids = manager.search_for_processes('chrome.exe')  # Replace with a valid process name
        # print(f"Found processes with PIDs: {process_pids}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except PermissionError as pe:
        print(f"Error: {pe}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
