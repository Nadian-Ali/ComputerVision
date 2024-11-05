# src/utils.py

import cv2
import os

def read_image(image_path):
    """Reads an image from a given path."""
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"The image path '{image_path}' does not exist.")
    return cv2.imread(image_path)

def get_image_size(image):
    """Returns the dimensions (height, width) of an image."""
    return image.shape[:2]

def resize_image(image, width, height):
    """Resizes the image to the given width and height."""
    return cv2.resize(image, (width, height))
