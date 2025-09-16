# 代码生成时间: 2025-09-16 18:39:14
import requests
from bs4 import BeautifulSoup

class WebContentGrabber:
    """
    A simple web content grabber to fetch and parse web pages.
    """

    def __init__(self, url):
        """
        Initialize the grabber with a URL to fetch.
        """
        self.url = url
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': 'Mozilla/5.0'})

    def fetch_content(self):
        """
        Fetch the content of the webpage.
        """
        try:
            response = self.session.get(self.url)
            response.raise_for_status()  # Raise an HTTPError if the HTTP request returned an unsuccessful status code
            return response.text
        except requests.RequestException as e:
            print(f"An error occurred while fetching the content: {e}")
            return None

    def parse_content(self, content):
        """
        Parse the fetched content using BeautifulSoup.
        """
        if content is None:
            return None
        soup = BeautifulSoup(content, 'html.parser')
        return soup

    def get_title(self, soup):
        """
        Get the title of the webpage from the parsed content.
        """
        if soup is None:
            return None
        return soup.title.string if soup.title else None

    def get_paragraphs(self, soup):
        """
        Get all paragraphs from the parsed content.
        """
        if soup is None:
            return []
        paragraphs = soup.find_all('p')
        return [p.get_text() for p in paragraphs]

# Example usage:
if __name__ == '__main__':
    url = 'https://example.com'
    grabber = WebContentGrabber(url)
    content = grabber.fetch_content()
    
    if content:
        soup = grabber.parse_content(content)
        title = grabber.get_title(soup)
        paragraphs = grabber.get_paragraphs(soup)
        
        print(f'Title: {title}')
        print('Paragraphs:')
        for paragraph in paragraphs:
            print(paragraph)