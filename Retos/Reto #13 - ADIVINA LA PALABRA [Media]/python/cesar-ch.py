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
 * - La palabra debe ocultar de forma aleatoria letras, y nunca puede comenzar
 *   ocultando más del 60%
 * - Puedes utilizar las palabras que quieras y el número de intentos que consideres
"""

import random

def GuessWord(originalWord):
    word = HiddenWord(originalWord)
    attempts = round(len(originalWord) / 2) + 1

    while attempts > 0:
        print("Número de intentos:", attempts)
        print("Palabra oculta:", word)
        response = input("Introduce una letra: ")

        found = False

        for i in range(len(originalWord)):
            if originalWord[i] == response and word[i] == "_":
                word = word[:i] + response + word[i+1:]
                found = True
                print(word)

        if word == originalWord:
            break

        if not found:
            attempts -= 1

    if word == originalWord:
        print("Has ganado")
    else:
        print("Has perdido")

def HiddenWord(word):
    length = round(len(word) * 0.6)
    arr = list("_" * len(word))
    print(range(len(word)))
    print(length)
    indices = random.sample(range(len(word)), length)
    print(indices)
    for i, index in enumerate(indices):
        if arr[index] == word[index]:
            i -= 1
        else:
            arr[index] = word[index]
    return "".join(arr)


GuessWord("mouredev")
