# google library for communication with google vision api
from google.cloud import vision

# python-telegram-bot library
from telegram import Update, File

# Get temp folder and temp file names
import tempfile

# System communication
import os

class Ocr:
    """Class for communication with google vision api"""
    @staticmethod
    def get_text_from_image(image_file: File) -> str:
        """Get text from image with google vision api"""

        # Get temp file path with tempfile library
        fd, temp_file_path = tempfile.mkstemp()

        # Download image 
        image_file.download(temp_file_path)

        # Read image file as binary
        with open(temp_file_path, 'rb') as image_file:
            content = image_file.read()

        # Create vision.Image object to use it in document_text_detection function
        image = vision.Image(content = content)

        # Get response from google vision api
        # client field will be add to function in telegram_bot.py script
        response = Ocr.client.document_text_detection(image = image)

        # Get text from response
        text = response.full_text_annotation.text

        # Close file, automatic deletion will occur
        os.close(fd)
        
        # Return text
        return text
