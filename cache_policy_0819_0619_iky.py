# 代码生成时间: 2025-08-19 06:19:17
import requests
from cachecontrol import CacheControlAdapter
from cachecontrol.caches import FileCache

class CachePolicy:
    """实现了简单的缓存策略，使用requests和cachecontrol库。"""
    def __init__(self, cache_dir='cache'):
        """初始化缓存策略。

        Args:
            cache_dir (str): 缓存目录路径，默认为当前目录下的'cache'文件夹。
        """
        self.cache_dir = cache_dir
        self.session = requests.Session()
        self.cache = FileCache(cache_dir)
        self.session.mount('http://', CacheControlAdapter(self.cache))
        self.session.mount('https://', CacheControlAdapter(self.cache))

    def fetch(self, url):
        """从指定URL获取数据，并应用缓存策略。

        Args:
            url (str): 需要获取数据的URL。

        Returns:
            str: 从URL获取的数据，如果URL在缓存中，则返回缓存的数据。
        """
        try:
            response = self.session.get(url)
            response.raise_for_status()  # 检查请求是否成功
            return response.text
        except requests.RequestException as e:
            print(f"请求错误: {e}")
            return None

    def clear_cache(self):
        """清除缓存。"""
        self.cache.clear()

# 使用示例
if __name__ == '__main__':
    cache_policy = CachePolicy()
    url = 'https://api.example.com/data'
    data = cache_policy.fetch(url)
    if data:
        print(data)
    cache_policy.clear_cache()