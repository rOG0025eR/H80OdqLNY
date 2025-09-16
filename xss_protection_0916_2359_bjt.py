# 代码生成时间: 2025-09-16 23:59:46
import re
import html

"""
XSS Protection Module
This module provides basic protection against XSS attacks by sanitizing user input.
"""

class XSSProtector:
    """Class responsible for sanitizing input to prevent XSS attacks."""

    def __init__(self):
        # List of allowed tags for sanitization (can be extended)
        self.allowed_tags = ["b", "i", "em", "strong", "u", "p", "br", "ul", "ol", "li", "h1", "h2", "h3", "h4", "h5", "h6"]

    def sanitize_input(self, input_str):
        """Sanitize the input string to prevent XSS attacks."""
        # Use html.unescape to decode HTML entities
        sanitized_str = html.unescape(input_str)
        # Use regex to remove unwanted tags
        sanitized_str = re.sub("<[^>]*>", "", sanitized_str)
        # Allow only specific tags
        for tag in self.allowed_tags:
            sanitized_str = sanitized_str.replace(f"<{tag}>", "")
            sanitized_str = sanitized_str.replace(f"</{tag}>", "")
        return sanitized_str

    def is_safe(self, input_str):
        """Check if the input string is safe from XSS attacks."""
        try:
            sanitized_str = self.sanitize_input(input_str)
            # If no exception, the input is considered safe
            return True
        except Exception as e:
            # Log the exception (implementation depends on logging preferences)
            print(f"Error sanitizing input: {e}")
            return False

# Example usage
if __name__ == "__main__":
    protector = XSSProtector()
    user_input = "<script>alert('XSS')</script>"
    if protector.is_safe(user_input):
        print("Input is safe.")
    else:
        print("Input is unsafe.")
