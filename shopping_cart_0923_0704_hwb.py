# 代码生成时间: 2025-09-23 07:04:05
import requests

class ShoppingCart:
    """
    ShoppingCart class to manage the shopping cart functionality.
    It handles adding items, removing items, and showing the cart's contents.
    """

def __init__(self, base_url):
    """
    Initialize the ShoppingCart instance with the base URL of the API.
    :param base_url: str, the base URL of the API
    """
    self.base_url = base_url
    self.session = requests.Session()

    def add_item(self, item_id):
        """
        Add an item to the shopping cart.
        :param item_id: int, the ID of the item to add
        :raises ValueError: if the item cannot be added
        """
        url = f"{self.base_url}/cart/add/{item_id}"
        try:
            response = self.session.post(url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise ValueError(f"Failed to add item {item_id}: {e}")

    def remove_item(self, item_id):
        """
        Remove an item from the shopping cart.
        :param item_id: int, the ID of the item to remove
        :raises ValueError: if the item cannot be removed
        """
        url = f"{self.base_url}/cart/remove/{item_id}"
        try:
            response = self.session.delete(url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise ValueError(f"Failed to remove item {item_id}: {e}")

    def show_cart(self):
        """
        Get the current contents of the shopping cart.
        :raises ValueError: if the cart cannot be retrieved
        """
        url = f"{self.base_url}/cart"
        try:
            response = self.session.get(url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise ValueError(f"Failed to retrieve cart: {e}")

# Example usage:
if __name__ == '__main__':
    base_url = "http://example.com/api"
    cart = ShoppingCart(base_url)
    try:
        cart.add_item(1)
        cart.add_item(2)
        print(cart.show_cart())
        cart.remove_item(1)
        print(cart.show_cart())
    except ValueError as e:
        print(e)