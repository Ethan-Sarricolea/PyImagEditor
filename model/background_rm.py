"""
Description: Image edition background removal model
Author: Sarricolea Cortés Ethan Yahel
Date: 2025-09-05
"""

from rembg import remove
from PIL import Image
from model.image_ctrl import paste_image

def remove_background_clipboard(salida="docs/output.png"):
    """
    Removes the background from an image and saves the result.
    """
    try:
        img = paste_image()
        if img is None:
            raise ValueError("No image data in clipboard")
        img = img.convert("RGBA")
        output_image = remove(img)
        output_image.save(salida)
        return salida
    except Exception as e:
        raise RuntimeError("Failed to remove background from clipboard image") from e
    
# POR CONFIRMAR
def remove_background_image(image):
    """
    Removes the background from a PIL Image object and returns the result.
    """
    print(image)
    image = Image.open(image).convert("RGBA")
    output_image = remove(image)
    output_image.save("docs/output.png")
    return output_image