import os
import random
import sys
import select
from time import sleep
from typing import Callable

operations: list[tuple[str, Callable[[int, int], int]]] = [
    ("+", lambda x, y: x + y),
    ("-", lambda x, y: x - y),
    ("⨉", lambda x, y: x * y),
    ("÷", lambda x, y: x // y),
]


def timed_input(prompt: str, timeout: float = 3.0):
    print(prompt, end="", flush=True)

    rlist, _, _ = select.select([sys.stdin], [], [], timeout)
    if not rlist:
        return None
    return sys.stdin.readline().rstrip("\n")


def generate_question(x_digits: int, y_digits: int) -> tuple[str, int]:
    op_sign, op_func = random.choice(operations)
    x = random.randint(0, int("9" * x_digits))
    y = random.randint(0, int("9" * y_digits))

    if op_sign == "÷" and y == 0:
        while y == 0:
            y = random.randint(0, int("9" * y_digits))
            
    if x < y and x != 0:
        x, y = y, x

    return f"[?] {x} {op_sign} {y} = ", op_func(x, y)


def handle_player_loses(points):
    print(f"[*] You scored {points}!")


def handle_difficulty(points: int = 0, x_digits: int = 0, y_digits: int = 0):
    if points == 0:
        return x_digits, y_digits
    if points % 5 == 0:
        if points % 2 == 0:
            return x_digits, y_digits + 1
        else:
            return x_digits + 1, y_digits
    return x_digits, y_digits


def main():
    print("➕🟰 Welcome to the Ultimate Math Quest! ➖➗")
    for i in range(3,0,-1):
        print(f"[!] Starting in {i}...")
        sleep(1)
        print ("\033[A                             \033[A")
    points, x_digits , y_digits = 0, 1, 1
    while True:
        # handle digits
        x_digits, y_digits = handle_difficulty(points, x_digits, y_digits)

        # question and answer
        question, result = generate_question(x_digits, y_digits)
        user_input = timed_input(question, 3)

        # if timeout
        if not user_input:
            print("\n[!] Too Slow! You have been disqualified!")
            handle_player_loses(points)
            return

        # getting the answer
        try:
            answer = int(user_input.strip())
        except:
            print("[!] Incorret format! You have been disqualified!")
            handle_player_loses(points)
            return

        # * wrong answer
        if answer != result:
            print("[!] Game over! Incorrect answer!")
            print(f"{question}{result}")
            handle_player_loses(points)
            return

        # * correct answer
        points += 1


if __name__ == "__main__":
    os.system("clear")
    main()
