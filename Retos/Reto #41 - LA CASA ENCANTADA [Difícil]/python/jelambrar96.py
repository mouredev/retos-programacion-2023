#!/usr/bin/python3

"""
# Reto #41: La casa encantada
/*
 * Este es un reto especial por Halloween.
 * Te encuentras explorando una mansión abandonada llena de habitaciones.
 * En cada habitación tendrás que resolver un acertijo para poder avanzar a la siguiente.
 * Tu misión es encontrar la habitación de los dulces.
 *
 * Se trata de implementar un juego interactivo de preguntas y respuestas por terminal.
 * (Tienes total libertad para ser creativo con los textos)
 *
 * - 🏰 Casa: La mansión se corresponde con una estructura cuadrada 4 x 4
 *   que deberás modelar. Las habitaciones de puerta y dulces no tienen enigma.
 *   (16 habitaciones, siendo una de entrada y otra donde están los dulces)
 *   Esta podría ser una representación:
 *   🚪⬜️⬜️⬜️
 *   ⬜️👻⬜️⬜️
 *   ⬜️⬜️⬜️👻
 *   ⬜️⬜️🍭⬜️
 * - ❓ Enigmas: Cada habitación propone un enigma aleatorio que deberás responder con texto.
 *   Si no lo aciertas no podrás desplazarte.
 * - 🧭 Movimiento: Si resuelves el enigma se te preguntará a donde quieres desplazarte.
 *   (Ejemplo: norte/sur/este/oeste. Sólo deben proporcionarse las opciones posibles)
 * - 🍭 Salida: Sales de la casa si encuentras la habitación de los dulces.
 * - 👻 (Bonus) Fantasmas: Existe un 10% de que en una habitación aparezca un fantasma y
 *   tengas que responder dos preguntas para salir de ella.
 */
"""

__author__ = "Jorge Lambraño - jelambrar96"
__copyright__ = "Copyright 2024, retos-programacion-2023"
__credits__ = ["Brais Moure - mouredev"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Jorge Lambraño"
__email__ = "jelambrar@gmail.com"
__status__ = "Production"


import json
import random
import time

import requests

# Configuración inicial
DIMENSION = 4


def generarEnigma():
    reqUrl = "https://opentdb.com/api.php?amount=1&difficulty=easy&type=multiple"
    """
    {
        "response_code":0,
        "results":[
            {
                "type":"multiple",
                "difficulty":"easy",
                "category":"Science &amp; Nature",
                "question":"The element involved in making human blood red is which of the following?",
                "correct_answer":"Iron",
                "incorrect_answers":[
                    "Copper",
                    "Iridium",
                    "Cobalt"
                ]
            }
        ]
    }
    """
    response = {}
    while True: 
        try:
            # print("code")
            response_json = requests.get(reqUrl, timeout=5).json()
            response = response_json.get("results", [])[0]
        except IndexError:
            time.sleep(20)
        # print(response)
        if response:
            break

    answers = response["incorrect_answers"]
    correct = response["correct_answer"]
    answers.append(correct)
    str_answers = '\n'.join(answers)
    question = response['question'] + "\n" + str_answers
    return question, correct


# Funciones de utilidad
def print_grid(grid, me=None):
    temp_grid = [ row[:] for row in grid ]
    if me is not None:
        temp_grid[me[0]][me[1]] = '🔲'
    for row in temp_grid:
        print(''.join(row))
    print()

def get_possible_moves(x, y):
    moves = []
    if x > 0: moves.append('norte')
    if x < DIMENSION - 1: moves.append('sur')
    if y > 0: moves.append('oeste')
    if y < DIMENSION - 1: moves.append('este')
    return moves

def move_player(x, y, direction):
    if direction == 'norte': return (x-1, y)
    if direction == 'sur': return (x+1, y)
    if direction == 'este': return (x, y+1)
    if direction == 'oeste': return (x, y-1)

def check_ghost():
    return random.random() < 0.1  # 10% de probabilidades


def main():

    entrance = (0, 0)
    candy_room = (0, 0)

    while candy_room[0] == entrance[0] and candy_room[1] == entrance[1]:
        candy_room = (random.randint(0,3), random.randint(0,3))

    # riddles = [
    # "¿Cuál es el animal que después de muerto da muchas vueltas? (R: El pollo)",
    # "¿Qué tiene dientes pero no puede comer? (R: El peine)",
    # "¿Qué es algo y nada a la vez? (R: El pez)"
    # ]
    grid = [['⬜️' for _ in range(DIMENSION)] for _ in range(DIMENSION)]
    grid[entrance[0]][entrance[1]] = '🚪'
    grid[candy_room[0]][candy_room[1]] = '🍭'

    print_grid(grid)

    # Juego principal
    player_position = entrance
    while player_position != candy_room:

        x, y = player_position
        if check_ghost():
            print("¡Un fantasma aparece! Debes resolver dos enigmas para continuar.")
            additional_riddles = [generarEnigma(), generarEnigma()]
        else:
            additional_riddles = [generarEnigma()]

        # print(additional_riddles)
        for riddle, correct in additional_riddles:
            # print("Enigma:", riddle, f"\nrespuesta: {correct}")
            print("Enigma:", riddle) # , f"\nrespuesta: {correct}")
            answer = input("Tu respuesta: ").strip()
            if answer.lower() != correct.lower():
                print("Respuesta incorrecta. ¡Inténtalo de nuevo!")
                continue

        moves = get_possible_moves(x, y)
        print("Puedes moverte a:", ", ".join(moves))
        move = input("¿A dónde quieres ir? ")
        if move in moves:
            player_position = move_player(x, y, move)

        print_grid(grid, player_position)

    print("¡Felicidades! Has encontrado la habitación de los dulces.")


if __name__  == '__main__':
    main()