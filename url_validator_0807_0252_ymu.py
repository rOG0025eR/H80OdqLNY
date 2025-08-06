# 代码生成时间: 2025-08-07 02:52:20
import requests
import urllib.parse

class URLValidator:
    """
    A class to validate the validity of URLs.
    """

def validate_url(url):
    """
    Validate the URL's structure and check if it is reachable.
    
    Args:
        url (str): The URL to be validated.
    
    Returns:
        dict: A dictionary with validation status and message.
    """
    try:
        # Parse the URL to check its structure
        parsed_url = urllib.parse.urlparse(url)
        if not all([parsed_url.scheme, parsed_url.netloc]):
            return {"valid": False, "message": "Invalid URL structure."}
        
        # Check if the URL is reachable
        response = requests.head(url, allow_redirects=True, timeout=5)
        if response.status_code == 200:
            return {"valid": True, "message": "URL is valid and reachable."}
        else:
            return {"valid": False, "message": f"URL is not reachable. Status code: {response.status_code}."}
    except requests.RequestException as e:
        return {"valid": False, "message": f"An error occurred: {str(e)}."}
    except Exception as e:
        return {"valid": False, "message": f"An unexpected error occurred: {str(e)}."}

# Example usage
if __name__ == '__main__':
    url_to_validate = "http://example.com"
    result = validate_url(url_to_validate)
    print(result)