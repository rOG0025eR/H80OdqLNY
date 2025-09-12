# 代码生成时间: 2025-09-13 05:30:34
import requests
from requests.exceptions import RequestException

"""
A simple web content fetcher tool using Python and Requests library.
This tool fetches content from a specified URL and handles common errors.
"""

class WebContentFetcher:
    def __init__(self, url):
        """
        Initialize the WebContentFetcher with a URL.
        :param url: The URL of the webpage to fetch content from.
        """
        self.url = url

    def fetch_content(self):
        """
        Fetch the content of the webpage.
        :return: The content of the webpage as a string.
        :raises RequestException: If a network-related error occurs.
        """
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Raise an HTTPError if the HTTP request returned an unsuccessful status code.
            return response.text
        except RequestException as e:
            # Handle any exceptions that occur during the request.
            print(f"An error occurred: {e}")
            return None

def main():
    # Example usage of the WebContentFetcher
    url = "https://example.com"
    fetcher = WebContentFetcher(url)
    content = fetcher.fetch_content()
    if content:
        print("Webpage content fetched successfully.")
        print(content)
    else:
        print("Failed to fetch webpage content.")

if __name__ == "__main__":
    main()