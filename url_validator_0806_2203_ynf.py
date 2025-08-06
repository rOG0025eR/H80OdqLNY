# 代码生成时间: 2025-08-06 22:03:52
import requests
from requests.exceptions import RequestException

"""
This module provides a function to validate the validity of a URL by checking if it's reachable via HTTP GET requests.
"""

def validate_url(url):
    """
    Validates a URL by attempting to make an HTTP GET request.
    
    Args:
        url (str): The URL to be validated.
    
    Returns:
        bool: True if the URL is valid and reachable, False otherwise.
    """
    try:
        # Attempt to make a GET request to the URL with a timeout of 5 seconds.
        response = requests.get(url, timeout=5)
        # If the request is successful and the status code is 200, the URL is considered valid.
        return response.status_code == 200
    except RequestException as e:
        # If any request-related error occurs, log the error and return False.
        print(f"An error occurred while validating the URL: {e}")
        return False

# Example usage:
if __name__ == '__main__':
    test_url = "http://example.com"
    is_valid = validate_url(test_url)
    print(f"The URL '{test_url}' is {'valid' if is_valid else 'invalid'}.")