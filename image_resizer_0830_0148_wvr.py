# 代码生成时间: 2025-08-30 01:48:27
import os
import requests
from PIL import Image
from io import BytesIO
from urllib.parse import urljoin

"""
图片尺寸批量调整器

该脚本使用Python和requests框架，实现批量调整图片尺寸的功能。
支持从本地文件夹或远程URL读取图片，并将调整后的图片保存到指定目录。
"""

class ImageResizer:
    def __init__(self, target_width, target_height, input_dir=None, output_dir='./resized_images'):
        """
        初始化ImageResizer对象

        :param target_width: 目标宽度（像素）
        :param target_height: 目标高度（像素）
        :param input_dir: 输入目录（本地文件夹或远程URL）
        :param output_dir: 输出目录（默认为当前目录下的resized_images文件夹）
        """
        self.target_width = target_width
        self.target_height = target_height
        self.input_dir = input_dir
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)  # 创建输出目录

    def resize_image(self, image_path):
        """
        调整单张图片尺寸

        :param image_path: 图片路径（本地文件路径或远程URL）
        :return: None
        """
        try:
            if image_path.startswith('http'):
                # 从远程URL读取图片
                response = requests.get(image_path)
                response.raise_for_status()
                image = Image.open(BytesIO(response.content))
            else:
                # 从本地文件读取图片
                image = Image.open(image_path)

            # 调整图片尺寸
            image = image.resize((self.target_width, self.target_height))

            # 保存调整后的图片
            output_path = os.path.join(self.output_dir, os.path.basename(image_path))
            image.save(output_path)
            print(f'图片已调整尺寸并保存到：{output_path}')
        except Exception as e:
            print(f'调整图片尺寸失败：{e}')

    def resize_images(self):
        """
        批量调整图片尺寸

        :return: None
        """
        if self.input_dir:
            if os.path.isdir(self.input_dir):
                # 批量处理本地文件夹中的图片
                for filename in os.listdir(self.input_dir):
                    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                        image_path = os.path.join(self.input_dir, filename)
                        self.resize_image(image_path)
            elif self.input_dir.startswith('http'):
                # 批量处理远程URL中的图片
                response = requests.get(self.input_dir)
                response.raise_for_status()
                # 假设远程URL返回的是JSON格式的图片列表
                image_urls = response.json().get('images', [])
                for image_url in image_urls:
                    self.resize_image(urljoin(self.input_dir, image_url))
            else:
                print(f'输入目录无效：{self.input_dir}')
        else:
            print('未指定输入目录')

# 示例用法
if __name__ == '__main__':
    # 创建ImageResizer对象
    resizer = ImageResizer(target_width=800, target_height=600, input_dir='./images', output_dir='./resized_images')
    # 批量调整图片尺寸
    resizer.resize_images()
