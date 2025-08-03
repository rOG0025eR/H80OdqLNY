# 代码生成时间: 2025-08-03 13:43:20
import psutil
import platform

"""
A simple Python script to analyze memory usage using the psutil library.
This script fetches the memory information of the system and prints it out.
"""


def get_memory_info():
    """
    Retrieves the memory information from the system.
    """
    try:
        mem = psutil.virtual_memory()
        return mem
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.Error) as e:
        print(f"An error occurred while fetching memory info: {e}")
        return None


def print_memory_info(mem_info):
    """
    Prints the memory information in a human-readable format.
    """
    total, available, used, free = mem_info
    print(f"Total: {total / (1024 ** 3):.2f} GB")
    print(f"Available: {available / (1024 ** 3):.2f} GB\)
    print(f"Used: {used / (1024 ** 3):.2f} GB\)
    print(f"Free: {free / (1024 ** 3):.2f} GB\)
    print(f"Percentage Used: {mem_info.percent}%")


def main():
    """
    Main function to orchestrate the memory usage analysis.
    """
    print(f"Memory usage analysis on {platform.system()} {platform.release()} ({platform.machine()}):\
")
    mem_info = get_memory_info()
    if mem_info:
        print_memory_info(mem_info)
    else:
        print("Failed to retrieve memory information.")

if __name__ == "__main__":
    main()