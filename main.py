from function import *
import game_mode, game_rule


def main():
    while True:
        screen_clear()
        menu_functions = {1: game_mode.single_player,
                          2: game_mode.multi_player,
                          3: game_rule.game_rule}
        menu = ["Single player",
                "Multi player",
                "Game rule",
                "Exit"]
        question = ["Choose the menu's number"]
        print_menu(menu)
        menu_number = get_input(question)
        if int(menu_number[0]) != 0:
            menu_functions[int(menu_number[0])]()
        else:
            screen_clear()
            good_bye_message = "Goodbye see you soon!"
            print(good_bye_message)
            break

if __name__ == '__main__':
    main()