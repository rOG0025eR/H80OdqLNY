# 代码生成时间: 2025-09-03 01:13:56
import requests
import json

# 用户权限管理系统
class UserPermissionManager:
    """
    用户权限管理系统，通过HTTP请求与后端API交互。
    """
    def __init__(self, api_url):
        """
        初始化UserPermissionManager对象。
        :param api_url: 后端API的基础URL
        """
        self.api_url = api_url

    def add_user(self, username, password, permissions):
        """
        添加新用户。
        :param username: 用户名
        :param password: 密码
        :param permissions: 用户权限列表
        :return: API响应的JSON数据
        """
        try:
            url = f"{self.api_url}/users"
            data = {"username": username, "password": password, "permissions": permissions}
            response = requests.post(url, json=data)
            response.raise_for_status()  # 检查HTTP响应状态码是否为200
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error adding user: {e}")
            return None

    def update_user_permissions(self, username, new_permissions):
        """
        更新用户权限。
        :param username: 用户名
        :param new_permissions: 新的权限列表
        :return: API响应的JSON数据
        """
        try:
            url = f"{self.api_url}/users/{username}/permissions"
            data = {"permissions": new_permissions}
            response = requests.put(url, json=data)
            response.raise_for_status()  # 检查HTTP响应状态码是否为200
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error updating user permissions: {e}")
            return None

    def delete_user(self, username):
        """
        删除用户。
        :param username: 用户名
        :return: API响应的JSON数据
        """
        try:
            url = f"{self.api_url}/users/{username}"
            response = requests.delete(url)
            response.raise_for_status()  # 检查HTTP响应状态码是否为200
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error deleting user: {e}")
            return None

# 使用示例
if __name__ == "__main__":
    api_url = "http://localhost:8000/api"
    manager = UserPermissionManager(api_url)

    # 添加用户
    user_data = {"username": "john", "password": "password123", "permissions": ["read", "write"]}
    add_response = manager.add_user(**user_data)
    print(json.dumps(add_response, indent=2))

    # 更新用户权限
    permissions = ["read", "write", "delete"]
    update_response = manager.update_user_permissions("john", permissions)
    print(json.dumps(update_response, indent=2))

    # 删除用户
    delete_response = manager.delete_user("john")
    print(json.dumps(delete_response, indent=2))