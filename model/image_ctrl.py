"""
Description: Controller for image operations
Author: Sarricolea Cortés Ethan Yahel
Date: 2025-09-05
"""

from PIL import Image, ImageGrab
import win32clipboard
from io import BytesIO

# Copy

def copy_image(path):
    """
    Copies the current image to the clipboard.
    """
    try:
        img = Image.open(path)
        buffer = BytesIO()
        img.save(buffer, format='BMP')
        data = buffer.getvalue()[14:]  # BMP file header is 14 bytes
        buffer.close()

        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
        win32clipboard.CloseClipboard()
    except Exception as e:
        raise RuntimeError("Failed to copy image to clipboard") from e

# Paste - va a requerir try

def paste_image():
    """
    Pastes an image from the clipboard.
    """
    try:
        data = ImageGrab.grabclipboard()
        if data is None:
            raise ValueError("No image data in clipboard")
        
        if isinstance(data, Image.Image):
            return data
        if isinstance(data, list) and len(data) > 0:
            try:
                img = Image.open(data[0])
            except Exception as e:
                raise ValueError("Clipboard data is not an image") from e
        print("Clipboard data is not an image")
        return None
    except Exception as e:
        raise RuntimeError("Failed to paste image from clipboard") from e