# 代码生成时间: 2025-08-12 16:34:18
import requests

class AccessControl:
    """访问权限控制类"""
    def __init__(self, base_url, headers):
        """
        :param base_url: 基础URL
        :param headers: 请求头，包含认证信息
        """
        self.base_url = base_url
        self.headers = headers

    def check_access(self, endpoint):
        """检查访问权限
        
        :param endpoint: 请求的端点
        :return: 权限检查结果
        """
        try:
            url = f"{self.base_url}{endpoint}"
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()  # 抛出HTTPError异常，如果响应状态不是200
            return {"status": "success", "data": response.json()}
        except requests.exceptions.HTTPError as http_err:
            return {"status": "error", "message": f"HTTP error occurred: {http_err}"}
        except Exception as err:
            return {"status": "error", "message": f"Other error occurred: {err}"}

# 示例用法
if __name__ == '__main__':
    base_url = "https://api.example.com/"
    headers = {"Authorization": "Bearer YOUR_ACCESS_TOKEN"}
    
    # 创建访问控制实例
    access_controller = AccessControl(base_url, headers)
    
    # 检查特定端点的访问权限
    endpoint = "protected-resource"
    result = access_controller.check_access(endpoint)
    print(result)