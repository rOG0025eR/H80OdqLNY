# 代码生成时间: 2025-08-25 18:07:14
import requests
import json
from typing import Any, Dict

"""
Config Manager responsible for managing configurations via HTTP requests.
"""

class ConfigManager:
    def __init__(self, base_url: str):
        """
        Initialize the ConfigManager with the base URL of the config server.
        :param base_url: The URL of the config server.
        """
        self.base_url = base_url

    def get_config(self, endpoint: str) -> Dict[str, Any]:
        """
        GET a configuration from the specified endpoint.
        :param endpoint: The endpoint for the configuration.
        :return: A dictionary containing the configuration.
        :raises: requests.RequestException if the request fails.
        """
        url = f"{self.base_url}/{endpoint}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise SystemExit(f"Failed to retrieve config from {url}: {e}")

    def set_config(self, endpoint: str, config_data: Dict[str, Any]) -> None:
        """
        POST a new configuration to the specified endpoint.
        :param endpoint: The endpoint for the configuration.
        :param config_data: A dictionary containing the new configuration data.
        :raises: requests.RequestException if the request fails.
        """
        url = f"{self.base_url}/{endpoint}"
        try:
            response = requests.post(url, json=config_data)
            response.raise_for_status()
        except requests.RequestException as e:
            raise SystemExit(f"Failed to set config at {url}: {e}")

    def update_config(self, endpoint: str, config_data: Dict[str, Any]) -> None:
        """
        PUT an updated configuration to the specified endpoint.
        :param endpoint: The endpoint for the configuration.
        :param config_data: A dictionary containing the updated configuration data.
        :raises: requests.RequestException if the request fails.
        """
        url = f"{self.base_url}/{endpoint}"
        try:
            response = requests.put(url, json=config_data)
            response.raise_for_status()
        except requests.RequestException as e:
            raise SystemExit(f"Failed to update config at {url}: {e}")

    def delete_config(self, endpoint: str) -> None:
        """
        DELETE a configuration from the specified endpoint.
        :param endpoint: The endpoint for the configuration.
        :raises: requests.RequestException if the request fails.
        """
        url = f"{self.base_url}/{endpoint}"
        try:
            response = requests.delete(url)
            response.raise_for_status()
        except requests.RequestException as e:
            raise SystemExit(f"Failed to delete config at {url}: {e}")

# Example usage:
if __name__ == "__main__":
    config_manager = ConfigManager("http://example.com/config")
    try:
        config = config_manager.get_config("application")
        print("Retrieved config: ", config)
    except SystemExit as e:
        print(e)