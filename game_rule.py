from function import screen_clear

def game_rule():
    press_message = "Press the Enter"
    with open("rule.txt", "r") as file:
        screen_clear()
        for line in file:
            print(line.rstrip())
        input(press_message)