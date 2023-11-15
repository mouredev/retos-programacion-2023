#!/usr/bin/env python3

import random

entry = "🚪"
exit = "🍭"
room = "⬜"
ghost = "👻"
player = "🐍"

questions_list = [
    ["Who is the most famous vampire?", "Dracula"],
    ["Is Halloween scary?", "Yes"],
    ["Who is the craziest scientist?", "Frankestein"],
]

def get_random_question():
    nq = len(questions_list)

    n = random.randint(0, nq-1)

    return questions_list[n]

def is_up_possible(player_pos):
    if player_pos[0] == 0:
        return False
    return True

def move_up(player_pos):
    if not is_up_possible(player_pos):
        return

    player_pos[0] -= 1

def is_down_possible(player_pos):
    if player_pos[0] == 3:
        return False
    return True

def move_down(player_pos):
    if not is_down_possible(player_pos):
        return

    player_pos[0] += 1

def is_left_possible(player_pos):
    if player_pos[1] == 0:
        return False
    return True

def move_left(player_pos):
    if not is_left_possible(player_pos):
        return

    player_pos[1] -= 1

def is_right_possible(player_pos):
    if player_pos[1] == 3:
        return False
    return True

def move_right(player_pos):
    if not is_right_possible(player_pos):
        return

    player_pos[1] += 1

def create_empty_house():
    house = []
    for i in range(4):
        house.append([room] * 4)
    return house

def place_ramdom_ghost(house, prob=10):
    for i in range(4):
        for j in range(4):
            if house[i][j] != room:
                continue
            p = random.randint(0, 100)
            if p <= prob:
                house[i][j] = ghost

def place_random_element(house, element):
    i = random.randint(0, 3)
    j = random.randint(0, 3)

    if house[i][j] == room:
        house[i][j] = element
    else:
        place_random_element(house, element)

def find_element(house, element):
    found = False
    pos = []

    for i in range(4):
        for j in range(4):
            if house[i][j] == element:
                found = True
                pos = [i, j]
                break
        if found:
            break
    return pos

def ask_question():
    [question, response] = get_random_question()
    print(question)

    answer = input("Answer: ")

    if answer == response:
        return True
    return False

def print_house(house, player_pos=[]):
    print("")
    for i in range(4):
        line = ""
        for j in range(4):
            if player_pos == [i,j]:
                line += player
            else:
                line += house[i][j]
        print(line)
    print("")

if __name__ == "__main__":
    house = create_empty_house()
    place_random_element(house, entry)
    place_random_element(house, exit)
    place_ramdom_ghost(house)
    player_pos =  find_element(house, entry)
    print_house(house, player_pos)

    end_game = False

    while not end_game:
        movs = []

        if is_up_possible(player_pos):
            movs += "u"
        if is_down_possible(player_pos):
            movs += "d"
        if is_left_possible(player_pos):
            movs += "l"
        if is_right_possible(player_pos):
            movs += "r"

        m = input("Allowed movements ("+ "".join(movs) +"): ")
        print("")

        if not m in movs:
            print("Bad movement, try again")
            continue

        if m == "u":
            move_up(player_pos)
        elif m == "d":
            move_down(player_pos)
        elif m == "l":
            move_left(player_pos)
        else:
            move_right(player_pos)

        print_house(house, player_pos)

        if house[player_pos[0]][player_pos[1]] == exit:
            print("Congratulations, you win!")
            end_game = True
            break

        questions = 1

        if house[player_pos[0]][player_pos[1]] == ghost:
            questions += 1

        for i in range(questions):
            ok = ask_question()
            if not ok:
                print("Game over! You lose")
                break

        if not ok:
            break
