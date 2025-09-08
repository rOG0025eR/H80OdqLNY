# 代码生成时间: 2025-09-08 17:04:09
import requests

class InventoryManager:
    """
    A simple inventory management system using Python and Requests.
    This class handles basic operations such as adding, updating, and deleting inventory items.
    """

    def __init__(self, base_url):
        """
        Initialize the InventoryManager with a base URL for API requests.
        :param base_url: The base URL of the inventory API.
        """
        self.base_url = base_url

    def add_item(self, item_id, item_name, quantity):
        """
        Add a new item to the inventory.
        :param item_id: The unique identifier for the item.
        :param item_name: The name of the item.
        :param quantity: The initial quantity of the item.
        :return: A dictionary with the result of the operation.
        """
        url = f"{self.base_url}/items"
        data = {"id": item_id, "name": item_name, "quantity": quantity}
        response = requests.post(url, json=data)
        if response.status_code == 201:
            return {"status": "success", "message": "Item added successfully."}
        else:
            return {"status": "error", "message": f"Failed to add item: {response.text}"}

    def update_item(self, item_id, quantity):
        """
        Update the quantity of an existing item in the inventory.
        :param item_id: The unique identifier for the item.
        :param quantity: The new quantity of the item.
        :return: A dictionary with the result of the operation.
        """
        url = f"{self.base_url}/items/{item_id}"
        data = {"quantity": quantity}
        response = requests.put(url, json=data)
        if response.status_code == 200:
            return {"status": "success", "message": "Item updated successfully."}
        else:
            return {"status": "error", "message": f"Failed to update item: {response.text}"}

    def delete_item(self, item_id):
        """
        Delete an item from the inventory.
        :param item_id: The unique identifier for the item.
        :return: A dictionary with the result of the operation.
        """
        url = f"{self.base_url}/items/{item_id}"
        response = requests.delete(url)
        if response.status_code == 204:
            return {"status": "success", "message": "Item deleted successfully."}
        else:
            return {"status": "error", "message": f"Failed to delete item: {response.text}"}

# Example usage:
if __name__ == "__main__":
    # Create an instance of InventoryManager with the base URL of the inventory API
    inventory = InventoryManager("http://example.com/api/")

    # Add a new item to the inventory
    result = inventory.add_item("001", "Widget", 100)
    print(result)

    # Update the quantity of an existing item
    result = inventory.update_item("001", 50)
    print(result)

    # Delete an item from the inventory
    result = inventory.delete_item("001")
    print(result)