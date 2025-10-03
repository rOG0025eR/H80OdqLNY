# 代码生成时间: 2025-10-03 22:09:50
import os
import requests
# 添加错误处理
from PIL import Image
from io import BytesIO

"""
# FIXME: 处理边界情况
Image Resizer: A Python script that resizes images in batch using PIL and Requests.

This script allows you to resize multiple images, saving them in a specified output directory.
# 优化算法效率
It uses the PIL library for image processing and the Requests library for downloading images if needed.
"""

class ImageResizer:
    def __init__(self, target_width, target_height, output_dir):
        """
        Initialize the ImageResizer with target dimensions and output directory.

        :param target_width: The desired width for resized images.
        :param target_height: The desired height for resized images.
        :param output_dir: The directory where resized images will be saved.
# TODO: 优化性能
        """
        self.target_width = target_width
        self.target_height = target_height
        self.output_dir = output_dir

    def resize_image(self, image_path, output_path):
        """
        Resize a single image and save it to the output path.

        :param image_path: The path of the image to resize.
        :param output_path: The path where the resized image will be saved.
        """
        try:
            with Image.open(image_path) as img:
                img = img.resize((self.target_width, self.target_height), Image.ANTIALIAS)
                img.save(output_path)
        except IOError:
# NOTE: 重要实现细节
            print(f"Error resizing image at {image_path}")
# 扩展功能模块

    def resize_images_in_directory(self, input_dir):
# FIXME: 处理边界情况
        """
        Resize all images in the specified directory.

        :param input_dir: The directory containing images to resize.
        """
        for filename in os.listdir(input_dir):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                image_path = os.path.join(input_dir, filename)
                output_path = os.path.join(self.output_dir, filename)
                self.resize_image(image_path, output_path)

    def download_and_resize_image(self, url, output_path):
        """
        Download an image from a URL, resize it, and save it to the output path.

        :param url: The URL of the image to download and resize.
        :param output_path: The path where the resized image will be saved.
        """
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an HTTPError if the HTTP request returned an unsuccessful status code
            with Image.open(BytesIO(response.content)) as img:
# FIXME: 处理边界情况
                img = img.resize((self.target_width, self.target_height), Image.ANTIALIAS)
                img.save(output_path)
        except requests.exceptions.RequestException as e:
            print(f"Error downloading image from {url}: {e}")
        except IOError as e:
            print(f"Error resizing image from {url}: {e}")

    def run(self, input_dir=None, url=None):
        """
        Resize images either from a directory or a URL.
# FIXME: 处理边界情况

        :param input_dir: The directory containing images to resize.
        :param url: The URL of the image to download and resize.
        """
        if input_dir:
            self.resize_images_in_directory(input_dir)
        elif url:
            output_path = os.path.join(self.output_dir, 'downloaded_resized_image.jpg')
# NOTE: 重要实现细节
            self.download_and_resize_image(url, output_path)
# TODO: 优化性能
        else:
            print("Please provide either a directory path or a URL.")

# Example usage:
if __name__ == '__main__':
    resizer = ImageResizer(target_width=800, target_height=600, output_dir='resized_images')
# 增强安全性
    # To resize images in a directory
    resizer.run(input_dir='path_to_your_images_directory')
    # To download and resize an image from a URL
    # resizer.run(url='https://example.com/image.jpg')