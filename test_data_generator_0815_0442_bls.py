# 代码生成时间: 2025-08-15 04:42:04
import requests
import json

class TestDataGenerator:
    """
    A class to generate test data using a specified API endpoint.
    """

    def __init__(self, url):
        """
        Initializes the TestDataGenerator with the API endpoint URL.
        """
        self.url = url

    def generate_test_data(self, payload):
        """
        Generates test data by sending a POST request to the API endpoint.

        Args:
            payload (dict): The data to be sent in the POST request.

        Returns:
            str: The JSON response from the API as a string.

        Raises:
            requests.RequestException: If the POST request fails.
        """
        try:
            response = requests.post(self.url, json=payload)
            response.raise_for_status()  # Raises an HTTPError for bad responses
            return response.text
        except requests.RequestException as e:
            print(f"An error occurred: {e}")
            raise

# Example usage
if __name__ == '__main__':
    api_endpoint = "https://api.example.com/test-data"
    test_data_payload = {"field1": "value1", "field2": "value2"}

    generator = TestDataGenerator(api_endpoint)
    try:
        test_data_response = generator.generate_test_data(test_data_payload)
        print("Generated Test Data: ", test_data_response)
    except Exception as e:
        print(f"Failed to generate test data: {e}")