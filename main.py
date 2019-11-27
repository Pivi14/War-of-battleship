import function
import os

def screen_clear():
    os.system("clear||cls")

def main():
    while True:
        screen_clear()
        # main menu print
        menu_functions = {1: single_player,
                          2: multi_player,
                          3: options}
        menu = ["Single player",
                "Multi player",
                "Options",
                "Exit"]
        question = ["Choose the menu's number"]
        function.print_menu(menu)
        menu_number = function.get_input(question)
        if int(menu_number[0]) != 0:
            menu_functions[int(menu_number[0])]()
        else:
            screen_clear()
            good_bye_message = "Goodbye see you soon!"
            print(good_bye_message)
            break

def single_player():
    pass

def multi_player():
    pass

def options():
    pass


if __name__ == '__main__':
    main()