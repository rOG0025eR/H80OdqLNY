# 代码生成时间: 2025-09-07 12:20:06
import requests
from bs4 import BeautifulSoup

"""
XSS Protection Module
This module provides functionality to detect and protect against XSS attacks.
It uses BeautifulSoup to sanitize input strings.
"""

class XSSProtector:
    """Class to handle XSS protection."""
    # List of allowed tags and attributes for HTML content
    ALLOWED_TAGS = ['b', 'strong', 'i', 'em', 'u', 'p', 'br', 'ol', 'ul', 'li', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'blockquote', 'code', 'pre']
    ALLOWED_ATTRIBUTES = ['href', 'src', 'alt', 'title', 'style']

    def __init__(self):
        # Initialize the XSS protector
        pass

    def sanitize(self, user_input):
        """Sanitize the user input to prevent XSS attacks."""
        sanitized_input = BeautifulSoup(user_input, 'html.parser')

        # Remove all tags not in the allowed list
        for tag in sanitized_input.find_all():
            if tag.name not in self.ALLOWED_TAGS:
                tag.decompose()

        # Remove all attributes not in the allowed list
        for tag in sanitized_input.find_all():
            for attribute in list(tag.attrs.keys()):
                if attribute not in self.ALLOWED_ATTRIBUTES:
                    del tag.attrs[attribute]

        return str(sanitized_input)

    def check_url(self, url):
        """Check if the URL is safe from XSS attacks."""
        try:
            response = requests.get(url)
            response.raise_for_status()

            # Sanitize the HTML content of the URL
            html_content = response.text
            sanitized_html = BeautifulSoup(html_content, 'html.parser')

            # Remove all scripts and iframes from the HTML content
            for script in sanitized_html.find_all('script'):
                script.decompose()
            for iframe in sanitized_html.find_all('iframe'):
                iframe.decompose()

            return str(sanitized_html)
        except requests.RequestException as e:
            print(f"Error checking URL: {e}")
            return None

# Example usage
if __name__ == '__main__':
    protector = XSSProtector()

    # Sanitize user input
    user_input = "<script>alert('XSS')</script>"
    sanitized_input = protector.sanitize(user_input)
    print(f"Sanitized user input: {sanitized_input}")

    # Check URL for XSS
    url = "http://example.com"
    sanitized_url = protector.check_url(url)
    if sanitized_url:
        print(f"Sanitized URL content: {sanitized_url}")