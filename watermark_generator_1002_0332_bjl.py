# 代码生成时间: 2025-10-02 03:32:25
import requests
import numpy as np
from PIL import Image
from io import BytesIO
from datetime import datetime

class WatermarkGenerator:
    """A class to embed watermarks into images."""

    def __init__(self, watermark_text):
        """Initialize the watermark generator."""
        self.watermark_text = watermark_text

    def embed_watermark(self, image_url):
        """Embed a watermark into an image."""
        try:
            # Fetch the image from the provided URL
            response = requests.get(image_url)
            response.raise_for_status()  # Raise an error for bad status codes
            image = Image.open(BytesIO(response.content))
            
            # Create a watermark image with the provided text
            watermark = Image.new('RGBA', image.size, (0,0,0,0))
            draw = watermark.Draw()
            font = Image.Font.load_default()
            draw.text((10,10), self.watermark_text, font=font, fill=(255,255,255,128))
            
            # Embed the watermark onto the original image
            image.paste(watermark, (0,0), watermark)
            
            # Save the watermarked image
            watermarked_image = BytesIO()
            image.save(watermarked_image, format='PNG')
            watermarked_image.seek(0)
            return watermarked_image
        except requests.RequestException as e:
            # Handle potential request exceptions
            print(f"Error fetching image: {e}")
            return None

    def save_watermarked_image(self, image_stream, filename):
        """Save the watermarked image to a file."""
        try:
            image_stream.seek(0)
            with open(filename, 'wb') as file:
                file.write(image_stream.read())
            print(f"Watermarked image saved as {filename}")
        except IOError as e:
            # Handle file I/O errors
            print(f"Error saving image: {e}")

# Example usage of the WatermarkGenerator class
if __name__ == '__main__':
    watermark_text = "Watermark - {}".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    generator = WatermarkGenerator(watermark_text)
    image_url = "https://example.com/image.jpg"  # Replace with your image URL
    watermarked_image = generator.embed_watermark(image_url)
    if watermarked_image:
        filename = "watermarked_image.png"
        generator.save_watermarked_image(watermarked_image, filename)