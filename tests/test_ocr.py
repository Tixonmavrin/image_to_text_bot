# Import library for testing our program
import unittest

# Import our ocr api class for communication with google vision api
from image_to_text_bot.ocr_api import Ocr

# google library for communication with google vision api
from google.cloud import vision


class ClientMock:
    """Client class mock for testing"""

    def __init__(self, text: str) -> None:
        """Init function"""
        self.text = text

    def document_text_detection(self, image: vision.Image) -> str:
        """Text detection from image. Always return init text"""
        x = lambda: 0
        x.full_text_annotation = lambda: 0
        x.full_text_annotation.text = self.text
        return x


class FileMock:
    """File class mock for testing"""

    @staticmethod
    def download(file_path: str) -> None:
        """Download image. Do nothing"""
        pass


class TestOcr(unittest.TestCase):
    """Main testing class"""

    def test_ocr(self) -> None:
        """Testing ocr class. Simple test to check return"""

        # Set result text
        text = "This is result text"

        # Add field client to Ocr class
        Ocr.client = ClientMock(text)

        # Assert equal texts
        self.assertEqual(text, Ocr.get_text_from_image(FileMock))
