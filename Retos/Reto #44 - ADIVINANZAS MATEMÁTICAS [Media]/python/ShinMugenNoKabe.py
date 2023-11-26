# Crea un juego interactivo por terminal en el que tendrás que adivinar 
# el resultado de diferentes
# operaciones matemáticas aleatorias (suma, resta, multiplicación 
# o división de dos números enteros).
# - Tendrás 3 segundos para responder correctamente.
# - El juego finaliza si no se logra responder en ese tiempo.
# - Al finalizar el juego debes mostrar cuántos cálculos has acertado.
# - Cada 5 aciertos debes aumentar en uno el posible número de cifras 
#   de la operación (cada vez en un operando):
#   - Preguntas 1 a 5: X (entre 0 y 9) operación Y (entre 0 y 9)
#   - Preguntas 6 a 10: XX (entre 0 y 99) operación Y (entre 0 y 9)
#   - Preguntas 11 a 15: XX operación YY
#   - Preguntas 16 a 20: XXX (entre 0 y 999) operación YY
#   ...

from random import choice, randint
from threading import Timer
from os import _exit
from functools import cache

ARITHMETIC_OPERATORS: list[str] = ["+", "-", "*", "/"]
TIMER_SECONDS = 3


@cache
def find_maximum_number(digits: int) -> int:
    if digits <= 0:
        raise ValueError("Invalid number of digits")

    one_plus_max_num: int = "1" + ("0" * digits)
    return int(f"{one_plus_max_num}") - 1


def resolve_arithmetic_expression(expression: str) -> int | float:
    return round(eval(expression), 2)


def generate_arithmetic_expression(digits_operator_1: int, digits_operator_2: int) -> str:
    maximum_number_1 = find_maximum_number(digits_operator_1)
    maximum_number_2 = find_maximum_number(digits_operator_2)

    operator_1: int = randint(1, maximum_number_1)
    operator_2: int = randint(1, maximum_number_2)
    arithmetic_operator: str = choice(ARITHMETIC_OPERATORS)

    return f"{operator_1} {arithmetic_operator} {operator_2}"


def check_user_solution(arithmetic_expression: str, current_score: int) -> None:
    t = Timer(TIMER_SECONDS, finish_game, args=[current_score])
    t.start()

    while True:
        try:
            answer: float = float(input(f"{arithmetic_expression} = "))
            solution: int | float = resolve_arithmetic_expression(arithmetic_expression)

            if answer != solution:
                print("Wrong answer!")
            else:
                t.cancel()
                break
        except ValueError:
            print("Invalid input!")
    

def finish_game(score: int):
    print(f"\nTime's up! Total score: {score}")
    _exit(0)


def play_game():
    current_score: int = 0
    digits_operator_1: int = 1
    digits_operator_2: int = 1

    while True:
        arithmetic_expression: str = generate_arithmetic_expression( digits_operator_1, digits_operator_2)
        check_user_solution(arithmetic_expression, current_score)
        current_score += 1

        if current_score % 5 == 0:
            if digits_operator_2 < digits_operator_1:
                digits_operator_2 += 1
            else:
                digits_operator_1 += 1


if __name__ == "__main__":
    play_game()