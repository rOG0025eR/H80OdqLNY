# 代码生成时间: 2025-10-05 17:43:48
import requests
import json


class HealthChecker:
    """
    A class to perform health checks on various services.
    """
    def __init__(self, service_urls):
        """
        Initialize the HealthChecker with a list of URLs to check.
        :param service_urls: A list of URLs for services to check.
        """
        self.service_urls = service_urls

    def check_service(self, url):
        """
        Check the health of a service by sending a GET request.
        :param url: The URL of the service to check.
        :return: A dictionary with the service status.
        """
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()  # Raises a HTTPError for bad responses
            return {
                'url': url,
                'status_code': response.status_code,
                'status': 'up'
            }
        except requests.exceptions.RequestException as e:
            return {
                'url': url,
                'status_code': None,
                'status': 'down',
                'error': str(e)
            }

    def check_all_services(self):
        """
        Check the health of all services.
        :return: A list of dictionaries with the status of each service.
        """
        results = []
        for url in self.service_urls:
            results.append(self.check_service(url))
        return results

    def report_health(self):
        """
        Print a report of the health check results.
        """
        results = self.check_all_services()
        for result in results:
            print(f"Service {result['url']} is {'up' if result['status'] == 'up' else 'down'}")
            if result['status'] == 'down':
                print(f"Error: {result['error']}")

# Example usage:
if __name__ == '__main__':
    service_urls = [
        "http://example.com/health",
        "http://anotherservice.com/status",
        # Add more service URLs as needed
    ]
    checker = HealthChecker(service_urls)
    checker.report_health()