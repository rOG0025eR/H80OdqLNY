# 代码生成时间: 2025-08-16 10:15:54
import requests

class InventoryManagement:
    """库存管理系统"""
    def __init__(self, base_url):
        """初始化库存管理系统"""
        self.base_url = base_url

    def get_inventory(self, inventory_id):
        """获取指定库存的信息"""
        url = f"{self.base_url}/inventory/{inventory_id}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching inventory: {e}")
            return None

    def add_inventory(self, inventory_data):
        """添加新的库存项"""
        url = f"{self.base_url}/inventory"
        try:
            response = requests.post(url, json=inventory_data)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error adding inventory: {e}")
            return None

    def update_inventory(self, inventory_id, inventory_data):
        """更新指定库存项"""
        url = f"{self.base_url}/inventory/{inventory_id}"
        try:
            response = requests.put(url, json=inventory_data)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error updating inventory: {e}")
            return None

    def delete_inventory(self, inventory_id):
        """删除指定库存项"""
        url = f"{self.base_url}/inventory/{inventory_id}"
        try:
            response = requests.delete(url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error deleting inventory: {e}")
            return None

# 示例用法
if __name__ == "__main__":
    base_url = "http://localhost:8000/api"
    inventory_manager = InventoryManagement(base_url)

    # 获取库存信息
    inventory_id = 1
    inventory_info = inventory_manager.get_inventory(inventory_id)
    print(f"Inventory Info: {inventory_info}
")

    # 添加库存项
    new_inventory = {"name": "Widget", "quantity": 10, "price": 19.99}
    add_result = inventory_manager.add_inventory(new_inventory)
    print(f"Add Inventory Result: {add_result}
")

    # 更新库存项
    update_inventory = {"quantity": 20}
    update_result = inventory_manager.update_inventory(1, update_inventory)
    print(f"Update Inventory Result: {update_result}
")

    # 删除库存项
    delete_result = inventory_manager.delete_inventory(1)
    print(f"Delete Inventory Result: {delete_result}")