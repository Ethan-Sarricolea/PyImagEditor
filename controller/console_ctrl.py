"""
Description: Console controller module for handling user interactions and commands.
Author: Sarricolea Cortés Ethan Yahel
Date: 2025-09-06
"""

from view.console import *
from model.image_ctrl import *
from model.background_rm import *

def console_start():
    option = True

    start()

    while option:
        interface_option()
        try:

            selection = int(input("Enter your choice: "))

            if selection == 4:
                end()
                break
            elif selection == 3:
                remove_background_clipboard()
                interface_success("Background removed and image saved as output.png")

            elif selection == 2:
                image_path = interface_prompt()
                remove_background_image(image_path)
                interface_success("Background removed and image saved as output.png")

            elif selection == 1:
                if confirmation_prompt("Do you want to copy the last image to the clipboard?"):
                    copy_image("docs/output.png")
                    interface_success("Image copied to clipboard successfully.")
                else:
                    interface_message("Operation cancelled by user.")

            elif selection == 0:
                interface_message("This option is under development.")
                
        except Exception as e:
                interface_error(str(e))
                continue