# tests/test_utils.py

import unittest
import cv2
import os
import sys

# Add the `src` directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
# print(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from src.utils import read_image, get_image_size, resize_image

class TestUtils(unittest.TestCase):

    def setUp(self):
        # Set up the path to the test image and read the image
        self.image_path = os.path.join(os.path.dirname(__file__), "../images/test.jpg")
        self.image = read_image(self.image_path)

    def test_read_image(self):
        # Test if the image is read correctly
        self.assertIsNotNone(self.image, "The image should not be None")
    
    def test_get_image_size(self):
        # Test if the function returns correct image size
        height, width = get_image_size(self.image)
        self.assertTrue(height > 0 and width > 0, "Image dimensions should be greater than 0")

    def test_resize_image(self):
        # Test if the image is resized correctly
        new_width, new_height = 100, 100
        resized_image = resize_image(self.image, new_width, new_height)
        resized_height, resized_width = get_image_size(resized_image)
        self.assertEqual(resized_width, new_width, "Width should match the specified value")
        self.assertEqual(resized_height, new_height, "Height should match the specified value")

if __name__ == "__main__":
    unittest.main()
