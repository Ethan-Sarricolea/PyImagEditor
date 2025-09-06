"""

"""

from view.console import *
from controller.background_rm import *
from model.image_ctrl import *

def main():
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
        except Exception as e:
                interface_error(str(e))
                continue

if __name__ == "__main__":
    main()