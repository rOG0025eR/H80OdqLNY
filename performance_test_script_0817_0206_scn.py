# 代码生成时间: 2025-08-17 02:06:51
# performance_test_script.py

# This script performs performance testing on a given URL using the requests library.

import requests
import time
from concurrent.futures import ThreadPoolExecutor
import threading


# Constants
THREAD_COUNT = 100  # Number of threads for concurrent requests
REQUEST_COUNT = 1000  # Number of requests each thread will perform
URL = 'http://example.com'  # The URL to perform performance testing on


# Function to perform a single HTTP GET request
def perform_get_request(session, url):
    try:
        response = session.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print(f'Request successful: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Request failed: {e}')


# Function to create a session and perform a specified number of requests
def perform_requests(url, thread_count, request_count):
    with requests.Session() as session:
        with ThreadPoolExecutor(max_workers=thread_count) as executor:
            futures = []
            for _ in range(request_count):
                future = executor.submit(perform_get_request, session, url)
                futures.append(future)
            for future in futures:
                future.result()  # Wait for all threads to complete


# Main function to start the performance testing
def main(url, thread_count, request_count):
    # Record the start time
    start_time = time.time()

    # Perform requests
    perform_requests(url, thread_count, request_count)

    # Record the end time
    end_time = time.time()

    # Calculate the duration of the test
    duration = end_time - start_time
    print(f'Performance test completed in {duration:.2f} seconds')


# Entry point of the script
if __name__ == '__main__':
    main(URL, THREAD_COUNT, REQUEST_COUNT)
