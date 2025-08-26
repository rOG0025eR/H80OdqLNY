# 代码生成时间: 2025-08-26 23:43:55
import requests
import json

"""
HTTP Request Handler
This module handles HTTP requests using the requests library in Python.
It provides a simple structure for making GET and POST requests,
handling errors and displaying the response.

Attributes:
    None

Methods:
    handle_get_request(url): Handles a GET request to the specified URL.
    handle_post_request(url, data): Handles a POST request to the specified URL with provided data.
"""

def handle_get_request(url):
    """
    Handles a GET request to the specified URL.
    
    Args:
        url (str): The URL to which the GET request will be sent.
    
    Returns:
        dict: A dictionary containing the response status code and content.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return {"status_code": response.status_code, "content": response.text}
    except requests.exceptions.HTTPError as http_err:
        return {"status_code": response.status_code, "error": str(http_err)}
    except Exception as err:
        return {"error": str(err)}


def handle_post_request(url, data):
    """
    Handles a POST request to the specified URL with provided data.
    
    Args:
        url (str): The URL to which the POST request will be sent.
        data (dict): The data to be sent in the POST request.
    
    Returns:
        dict: A dictionary containing the response status code and content.
    """
    try:
        response = requests.post(url, data=json.dumps(data))
        response.raise_for_status()  # Raise an exception for HTTP errors
        return {"status_code": response.status_code, "content": response.text}
    except requests.exceptions.HTTPError as http_err:
        return {"status_code": response.status_code, "error": str(http_err)}
    except Exception as err:
        return {"error": str(err)}

# Example usage
if __name__ == "__main__":
    # GET request example
    get_url = "https://jsonplaceholder.typicode.com/todos/1"
    get_response = handle_get_request(get_url)
    print("GET Response: ", json.dumps(get_response, indent=2))

    # POST request example
    post_url = "https://jsonplaceholder.typicode.com/posts"
    post_data = {"title": "foo", "body": "bar", "userId": 1}
    post_response = handle_post_request(post_url, post_data)
    print("POST Response: ", json.dumps(post_response, indent=2))