"""
 * Crea un pequeño juego que consista en adivinar palabras en un número máximo de intentos:
 * - El juego comienza proponiendo una palabra aleatoria incompleta
 *   - Por ejemplo "m_ur_d_v", y el número de intentos que le quedan
 * - El usuario puede introducir únicamente una letra o una palabra (de la misma longitud que
 *   la palabra a adivinar)
 *   - Si escribe una letra y acierta, se muestra esa letra en la palabra. Si falla, se resta
 *     uno al número de intentos
 *   - Si escribe una resolución y acierta, finaliza el juego, en caso contrario, se resta uno
 *     al número de intentos
 *   - Si el contador de intentos llega a 0, el jugador pierde
 * - La palabra debe ocultar de forma aleatoria letras, y nunca puede comenzar ocultando más del 60%
 * - Puedes utilizar las palabras que quieras y el número de intentos que consideres
"""

import math
import random

RAND_WORDS_LIST = [
    "ordenador",
    "monitor",
    "teclado",
    "archivador",
    "libreta",
    "escritorio",
    "sujetapapeles",
    "carpeta",
    "calculadora",
    "calendario"
]


def get_random(length: int):
    return random.randint(0, length - 1)


def sixty_percent(word: str):
    return math.floor(60 * len(word) / 100)


def get_index_lists(word: str, nchars: int):
    index_set = set()

    while len(index_set) < nchars:
        index_set.add(get_random(len(word)))

    not_shown_index = []
    for i in range(len(word)):
        if i not in index_set: not_shown_index.append(i)
        i += 1

    return [list(index_set), not_shown_index]


def show_word(word: str, index_list: list):
    result = ""

    for (idx, char) in enumerate(word):
        if idx in index_list: result += char
        else: result += "_"

    print(result)


def playGame():
    RAND_WORD = random.choice(RAND_WORDS_LIST)

    [show_index_list, not_shown_index] = get_index_lists(RAND_WORD, sixty_percent(RAND_WORD))
    
    attempts = 4           # number of attempts to guess the word
    user_wins = False
    
    print("Try to guess the word:")
    while attempts and not(user_wins):
        show_word(RAND_WORD, show_index_list)

        user_input = input("Enter a letter or a word: ")
        user_input = user_input.lower()
        
        if len(user_input) != 1 and len(user_input) != len(RAND_WORD):
            attempts -= 1
            print("\nYou can only enter one letter or the whole word!")
            print(f"number of attempts left: {attempts}")
            continue
        
        if len(user_input) == 1:
            includes_char = False

            not_shown_copy = not_shown_index.copy()
            for idx in not_shown_copy:
                if user_input == RAND_WORD[idx]:
                    show_index_list.append(idx)
                    not_shown_index.remove(idx)
                    includes_char = True

            if not(includes_char):
                attempts -= 1
                print(f"number of attempts left: {attempts}")

        else:
            if user_input != RAND_WORD:
                attempts -= 1
                print(f"number of attempts left: {attempts}")
            else:
                user_wins = True
                break

        # condition for winning
        if len(show_index_list) == len(RAND_WORD):
            user_wins = True

    print(f"\nThe word is: {RAND_WORD.upper()}")

    if user_wins:
        print("You Win!")
    else:
        print("You lose...")


playGame()