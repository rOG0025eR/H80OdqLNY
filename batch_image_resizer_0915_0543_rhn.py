# 代码生成时间: 2025-09-15 05:43:04
import os
import requests
from PIL import Image
from io import BytesIO

"""
Image Resizer for Batch Processing of Images
This script allows resizing multiple images in a directory by a specified factor.
It uses the requests library to download images if necessary.
"""

class ImageResizer:
    def __init__(self, image_folder, output_folder, resize_factor):
        """
        Initializes the image resizer.
        :param image_folder: Directory containing the original images.
        :param output_folder: Directory where resized images will be saved.
        :param resize_factor: Factor by which to resize the images.
        """
        self.image_folder = image_folder
        self.output_folder = output_folder
        self.resize_factor = resize_factor
        self.session = requests.Session()

    def resize_image(self, image_path):
        """
        Resizes a single image.
        :param image_path: Path to the image file.
        """
        try:
            with Image.open(image_path) as img:
                resized_img = img.resize((int(img.width * self.resize_factor), int(img.height * self.resize_factor)))
                return resized_img
        except IOError:
            print(f"Error opening image {image_path}")
            return None

    def save_resized_image(self, resized_img, filename):
        """
        Saves a resized image to the output directory.
        :param resized_img: The resized PIL Image object.
        :param filename: The filename for the resized image.
        """
        output_path = os.path.join(self.output_folder, filename)
        resized_img.save(output_path)
        print(f"Saved resized image to {output_path}")

    def process_directory(self):
        """
        Processes all images in the specified directory.
        """
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)

        for filename in os.listdir(self.image_folder):
            image_path = os.path.join(self.image_folder, filename)
            resized_img = self.resize_image(image_path)
            if resized_img:
                self.save_resized_image(resized_img, filename)

    def download_and_resize_image(self, image_url):
        """
        Downloads an image from a URL, resizes it, and saves it to the output directory.
        :param image_url: URL of the image to download.
        """
        try:
            response = self.session.get(image_url)
            response.raise_for_status()
            img = Image.open(BytesIO(response.content))
            resized_img = img.resize((int(img.width * self.resize_factor), int(img.height * self.resize_factor)))
            filename = os.path.basename(image_url)
            self.save_resized_image(resized_img, filename)
        except requests.RequestException as e:
            print(f"Error downloading image from {image_url}: {e}")

# Example usage:
if __name__ == '__main__':
    resizer = ImageResizer('path/to/images', 'path/to/output', 0.5)
    resizer.process_directory()
    # Optionally, to download and resize images from URLs:
    # resizer.download_and_resize_image('https://example.com/image.jpg')
