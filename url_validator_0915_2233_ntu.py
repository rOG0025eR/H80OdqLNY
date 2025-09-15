# 代码生成时间: 2025-09-15 22:33:42
import requests
import urllib.parse

"""
A simple URL validator that checks if a given URL is valid and accessible.
This module uses the requests library to send a HEAD request to the URL.
If the URL responds with a 200 status code, it is considered valid.
"""


class URLValidator:
    def __init__(self, url):
        """Initialize the URLValidator with a URL."""
        self.url = url
        
    def is_valid(self):
        """Check if the URL is valid and accessible.
        Returns True if the URL is valid, False otherwise."""
        try:
            # Sending a HEAD request to the URL to validate it without downloading the content
            response = requests.head(self.url)
            # Check if the status code is 200, indicating the URL is valid and accessible
            return response.status_code == 200
        except requests.RequestException as e:
            # Handle any exceptions that occur during the request, such as connection errors
            print(f"An error occurred: {e}")
            return False
        except ValueError:
            # Handle the case where the URL is not properly formatted
            print("Invalid URL format.")
            return False

    def __str__(self):
        """Return a string representation of the URLValidator."""
        return f"URLValidator(url={self.url})"


def main():
    # Example usage of the URLValidator class
    url = "http://www.example.com"
    validator = URLValidator(url)
    if validator.is_valid():
        print(f"The URL {url} is valid.")
    else:
        print(f"The URL {url} is not valid.")

if __name__ == "__main__":
    main()
