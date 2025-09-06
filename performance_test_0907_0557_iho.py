# 代码生成时间: 2025-09-07 05:57:35
import requests
import json
from time import time

"""
Performance Test Script

This script is designed to perform performance testing on a given API endpoint.
It sends a specified number of requests to the endpoint and measures the response time.
"""

class PerformanceTest:
    def __init__(self, url, headers=None, data=None, method='GET', num_requests=100):
        """
        Initialize the PerformanceTest class.

        Args:
        url (str): The URL of the API endpoint to test.
        headers (dict, optional): The headers to include in the request. Defaults to None.
        data (dict, optional): The data to send with the request. Defaults to None.
        method (str, optional): The HTTP method to use. Defaults to 'GET'.
        num_requests (int, optional): The number of requests to send. Defaults to 100.
        """
        self.url = url
        self.headers = headers if headers else {}
        self.data = data
        self.method = method
        self.num_requests = num_requests

    def send_requests(self):
        """
        Send the specified number of requests to the API endpoint.

        Returns:
        list: A list of response times in seconds.
        """
        response_times = []
        for _ in range(self.num_requests):
            try:
                start_time = time()
                response = requests.request(self.method, self.url, headers=self.headers, data=self.data)
                response.raise_for_status()  # Raise an exception for bad status codes
                end_time = time()
                response_times.append(end_time - start_time)
            except requests.RequestException as e:
                print(f"Request failed: {e}")
        return response_times

    def calculate_average_response_time(self, response_times):
        """
        Calculate the average response time from a list of response times.

        Args:
        response_times (list): A list of response times in seconds.

        Returns:
        float: The average response time.
        """
        if not response_times:
            return 0
        return sum(response_times) / len(response_times)

    def run_test(self):
        """
        Run the performance test and print the average response time.
        """
        response_times = self.send_requests()
        average_response_time = self.calculate_average_response_time(response_times)
        print(f"Average response time: {average_response_time:.2f} seconds")

# Example usage
if __name__ == '__main__':
    url = 'https://api.example.com/data'
    headers = {'Content-Type': 'application/json'}
    data = {'key': 'value'}
    test = PerformanceTest(url, headers, data, method='POST', num_requests=1000)
    test.run_test()