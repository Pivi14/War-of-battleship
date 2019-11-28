import os

def screen_clear():
    os.system("clear||cls")

def print_menu(menu):
    for element in range(len(menu) - 1):
        print(f"({element + 1}) {menu[element]}")
    print(f"(0) {menu[-1]}")

def get_input(question):
    results = []
    for quest in question:
        answer = input(f"{quest}: ")
        results.append(answer)
    return results

def create_matrix():
    default_value = 0
    matrix = []
    for column in range(10):
        matrix.append([])
        for row in range(10):
            matrix[column].append(default_value)
    return matrix

