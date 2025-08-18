# 代码生成时间: 2025-08-18 10:22:55
import psutil
import sys

"""
Process Manager

This script allows the user to manage system processes using the psutil library.
It provides functionality to list, terminate, and kill system processes.

Attributes:
    None

Methods:
    list_processes(): Lists all running processes.
    terminate_process(pid): Terminates a process by its PID.
    kill_process(pid): Kills a process by its PID.
"""


def list_processes():
    """Lists all running processes."""
    print("Listing all running processes...")
    for proc in psutil.process_iter(['pid', 'name', 'status']):
        print(f"PID: {proc.info['pid']}, Name: {proc.info['name']}, Status: {proc.info['status']}")


def terminate_process(pid):
    """Terminates a process by its PID."""
    try:
        process = psutil.Process(pid)
        process.terminate()
        process.wait()  # Wait for the process to terminate
        print(f"Process {pid} terminated successfully.")
    except psutil.NoSuchProcess:
        print(f"No process found with PID {pid}.")
    except psutil.AccessDenied:
        print(f"Access denied to terminate process {pid}.")
    except Exception as e:
        print(f"An error occurred: {e}")


def kill_process(pid):
    """Kills a process by its PID."""
    try:
        process = psutil.Process(pid)
        process.kill()
        process.wait()  # Wait for the process to terminate
        print(f"Process {pid} killed successfully.")
    except psutil.NoSuchProcess:
        print(f"No process found with PID {pid}.")
    except psutil.AccessDenied:
        print(f"Access denied to kill process {pid}.")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    """Main function to handle user input and execute corresponding actions."""
    while True:
        print("
Process Manager Menu:
1. List Processes
2. Terminate Process
3. Kill Process
4. Exit")
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            list_processes()
        elif choice == '2':
            pid = int(input("Enter the PID of the process to terminate: "))
            terminate_process(pid)
        elif choice == '3':
            pid = int(input("Enter the PID of the process to kill: "))
            kill_process(pid)
        elif choice == '4':
            print("Exiting Process Manager.")
            sys.exit()
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == '__main__':
    main()