# 代码生成时间: 2025-09-13 21:39:41
import requests

"""
A Python script that demonstrates the use of the Requests framework to fetch
web content and implements responsive layout design by checking the
response for certain keywords indicating that the page is responsive.
"""

# Constants for the URL and headers
BASE_URL = 'http://example.com'
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# Function to make a GET request and check for responsive layout
def check_responsive_layout(url):
    """
    Fetches the HTML content of the provided URL and checks for
    the presence of certain keywords that indicate a responsive layout.
    
    Args:
    url (str): The URL to fetch the HTML content from.
    
    Returns:
    bool: True if the layout is responsive, False otherwise.
    
    Raises:
    requests.RequestException: If there is an issue with the request.
    """
    try:
        # Make a GET request to the specified URL
        response = requests.get(url, headers=HEADERS)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Check for keywords related to responsive design
            keywords = ['meta name="viewport"', '@media screen', 'max-width', '@media only screen', 'min-width']
            for keyword in keywords:
                if keyword in response.text:
                    return True
            # If none of the keywords are found, the layout is not responsive
            return False
        else:
            raise ValueError(f'Failed to retrieve content: Status code {response.status_code}')
    except requests.RequestException as e:
        # Handle any exceptions that occur during the request
        print(f'An error occurred: {e}')
        return False

# Main function to run the script
def main():
    """
    The main function to run the script. It checks the responsiveness of the
    layout for the provided base URL.
    """
    # Check if the layout is responsive for the base URL
    is_responsive = check_responsive_layout(BASE_URL)
    if is_responsive:
        print(f'The layout of {BASE_URL} is responsive.')
    else:
        print(f'The layout of {BASE_URL} is not responsive.')

# Entry point of the script
if __name__ == '__main__':
    main()