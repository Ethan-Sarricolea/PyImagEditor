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

def interface_prompt(prompt_message):
    """
    Displays a prompt message to the console and returns user input.
    """
    return input(f"[PROMPT]: {prompt_message} ")

def interface_option():
    print("Select an option:")
    print("1.[DEV] Copy Image to Clipboard")
    print("2.[DEV] Remove Background from Image File")
    print("3. Remove Background from Clipboard Image")
    print("4. Exit")

def start():
    print("Welcome to PyImagEditor!")
    print("A simple image editor for basic tasks.")

def end():
    print("Thank you for using PyImagEditor. Goodbye!")
