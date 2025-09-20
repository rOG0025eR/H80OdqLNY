# 代码生成时间: 2025-09-20 13:59:38
import requests

class ThemeSwitcher:
    """
    A class to handle theme switching for a web application using the REQUESTS framework.
    """

    def __init__(self, base_url, headers=None):
        """
        Initialize the ThemeSwitcher with the base URL and optional headers.
        :param base_url: The base URL of the web application's API.
        :param headers: Optional headers to include in the requests.
        """
        self.base_url = base_url
        self.headers = headers if headers else {}

    def switch_theme(self, theme_name):
        """
        Switch the theme of the web application.
        :param theme_name: The name of the theme to switch to.
        :return: A tuple containing the response status code and the response text.
        """
        url = f"{self.base_url}/api/theme/{theme_name}"
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()  # Raise an HTTPError if the HTTP request returned an unsuccessful status code
            return response.status_code, response.text
        except requests.exceptions.HTTPError as http_err:
            # Handle HTTP errors
            print(f"HTTP error occurred: {http_err}")
            return http_err.response.status_code, http_err.response.text
        except requests.exceptions.RequestException as err:
            # Handle other request-related errors
            print(f"An error occurred: {err}")
            return None, None

# Example usage:
if __name__ == '__main__':
    base_url = "http://example.com"  # Replace with the actual base URL of your web application
    theme_switcher = ThemeSwitcher(base_url)
    status_code, response_text = theme_switcher.switch_theme("dark")
    print(f"Status Code: {status_code}, Response Text: {response_text}")
