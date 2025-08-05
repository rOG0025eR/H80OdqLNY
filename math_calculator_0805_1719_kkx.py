# 代码生成时间: 2025-08-05 17:19:57
import requests

"""
A simple math calculator using Python's requests library to perform operations."""

class MathCalculator:
    """Class to perform mathematical operations."""

    def __init__(self, base_url):
        """Initialize the calculator with a base URL."""
        self.base_url = base_url

    def add(self, a, b):
        """Add two numbers."""
        return self.send_request('add', {'a': a, 'b': b})

    def subtract(self, a, b):
        """Subtract two numbers."""
        return self.send_request('subtract', {'a': a, 'b': b})

    def multiply(self, a, b):
        """Multiply two numbers."""
        return self.send_request('multiply', {'a': a, 'b': b})

    def divide(self, a, b):
        """Divide two numbers."""
        if b == 0:
            raise ValueError('Cannot divide by zero.')
        return self.send_request('divide', {'a': a, 'b': b})

    def send_request(self, operation, payload):
        """Send a POST request to the server with the operation and payload."""
        url = f"{self.base_url}/{operation}"
        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            raise SystemExit(f'HTTP error occurred: {http_err}')
        except requests.exceptions.RequestException as err:
            raise SystemExit(f'Error occurred: {err}')

# Example usage:
if __name__ == '__main__':
    calculator = MathCalculator('http://math-service.com')

    try:
        print('Addition Result:', calculator.add(5, 3))
        print('Subtraction Result:', calculator.subtract(10, 4))
        print('Multiplication Result:', calculator.multiply(7, 6))
        print('Division Result:', calculator.divide(20, 4))
    except ValueError as ve:
        print(ve)