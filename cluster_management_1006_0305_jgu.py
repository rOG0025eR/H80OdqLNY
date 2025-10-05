# 代码生成时间: 2025-10-06 03:05:27
import requests

class ClusterManager:
    """
    ClusterManager provides functionality to manage a cluster of servers
    through HTTP requests.

    Attributes:
        base_url (str): The base URL of the cluster management API.
        headers (dict): Headers for the HTTP requests.
    """

    def __init__(self, base_url):
        self.base_url = base_url
        self.headers = {'Content-Type': 'application/json'}

    def add_node(self, node_data):
        """
        Adds a new node to the cluster.

        Args:
            node_data (dict): A dictionary containing the node's details.

        Returns:
            tuple: A tuple containing the HTTP status code and the response message.
        """
        url = self.base_url + '/nodes'
        try:
            response = requests.post(url, json=node_data, headers=self.headers)
            return response.status_code, response.json()
        except requests.RequestException as e:
            return 500, {'error': str(e)}

    def remove_node(self, node_id):
        """
        Removes a node from the cluster.

        Args:
            node_id (str): The ID of the node to remove.

        Returns:
            tuple: A tuple containing the HTTP status code and the response message.
        """
        url = self.base_url + f'/nodes/{node_id}'
        try:
            response = requests.delete(url, headers=self.headers)
            return response.status_code, response.json()
        except requests.RequestException as e:
            return 500, {'error': str(e)}

    def list_nodes(self):
        """
        Lists all nodes in the cluster.

        Returns:
            tuple: A tuple containing the HTTP status code and the response message.
        """
        url = self.base_url + '/nodes'
        try:
            response = requests.get(url, headers=self.headers)
            return response.status_code, response.json()
        except requests.RequestException as e:
            return 500, {'error': str(e)}

    def update_node(self, node_id, node_data):
        """
        Updates an existing node in the cluster.

        Args:
            node_id (str): The ID of the node to update.
            node_data (dict): A dictionary containing the updated node details.

        Returns:
            tuple: A tuple containing the HTTP status code and the response message.
        """
        url = self.base_url + f'/nodes/{node_id}'
        try:
            response = requests.put(url, json=node_data, headers=self.headers)
            return response.status_code, response.json()
        except requests.RequestException as e:
            return 500, {'error': str(e)}


# Example usage:
if __name__ == '__main__':
    base_url = 'http://example.com/api/cluster'
    manager = ClusterManager(base_url)
    
    node = {'id': 'node1', 'ip': '192.168.1.1'}
    status, response = manager.add_node(node)
    print(f'Added node with status {status}: {response}')
    
    node_id = 'node1'
    status, response = manager.remove_node(node_id)
    print(f'Removed node {node_id} with status {status}: {response}')
    
    status, response = manager.list_nodes()
    print(f'Listed nodes with status {status}: {response}')
    
    updated_node = {'ip': '192.168.1.2'}
    status, response = manager.update_node(node_id, updated_node)
    print(f'Updated node {node_id} with status {status}: {response}')