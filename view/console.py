"""
Description: Console view for displaying messages and errors
Author: Sarricolea Cortés Ethan Yahel
Date: 2025-09-05
"""

def interface_message(message):
    """
    Displays a message to the console.
    """
    print(f"[INFO]: {message}")

def interface_error(error_message):
    """
    Displays an error message to the console.
    """
    print(f"[ERROR]: {error_message}")

def interface_success(success_message):
    """
    Displays a success message to the console.
    """
    print(f"[SUCCESS]: {success_message}")

def interface_warning(warning_message):
    """
    Displays a warning message to the console.
    """
    print(f"[WARNING]: {warning_message}")

def interface_prompt(prompt_message = None):
    """
    Displays a prompt message to the console and returns user input.
    """
    if prompt_message:
        return input(f"[PROMPT]: {prompt_message}")
    else: 
        return input(r"[PROMPT]: ")

def interface_dev(dev_message):
    """
    Displays a development message to the console.
    """
    return(f"[DEV]: {dev_message}")

def interface_option(options):
    return (f"[OPTION]: {options}")

def interface_options_list():
    print("Select an option:")
    print(f"1. {interface_option('Copy Image to Clipboard')}")
    print(f"2. {interface_option('Remove Background from Image File')}")
    print(f"3. {interface_option('Remove Background from Clipboard Image')}")
    print("4. Exit")

def confirmation_prompt(prompt_message):
    """
    Displays a confirmation prompt to the user and returns True for 'y' and False for 'n'.
    """
    while True:
        response = input(f"{prompt_message} (y/n): ").strip().lower()
        if response == 'y':
            return True
        elif response == 'n':
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

def start():
    print("Welcome to PyImagEditor!")
    print("A simple image editor for basic tasks.")

def end():
    print("Thank you for using PyImagEditor. Goodbye!")
