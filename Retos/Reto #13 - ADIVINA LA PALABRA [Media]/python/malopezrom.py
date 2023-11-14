# /*
# * Crea un pequeño juego que consista en adivinar palabras en un número máximo de intentos:
#  * - El juego comienza proponiendo una palabra aleatoria incompleta
#  * - Por ejemplo "m_ur_d_v", y el número de intentos que le quedan
#  * - El usuario puede introducir únicamente una letra o una palabra(de la misma longitud que
#                                                                     * la palabra a adivinar)
#  * - Si escribe una letra y acierta, se muestra esa letra en la palabra. Si falla, se resta
#  *     uno al número de intentos
#  * - Si escribe una resolución y acierta, finaliza el juego, en caso contrario, se resta uno
#  *     al número de intentos
#  * - Si el contador de intentos llega a 0, el jugador pierde
#  * - La palabra debe ocultar de forma aleatoria letras, y nunca puede comenzar ocultando más del 60%
#  * - Puedes utilizar las palabras que quieras y el número de intentos que consideres
#  */

import random
import requests


# Estados del ahorcado

hangStates = ["""
                  +---+
                  |   |
                  O   |
                  |   |
                      |
                      |
              =========""",
              """
                  +---+
                  |   |
                  O   |
                 /|   |
                      |
                      |
              =========""",
              """
                  +---+
                  |   |
                  O   |
                 /|\\  |
                      |
                      |
              =========""",
              """
                  +---+
                  |   |
                  O   |
                 /|\\  |
                 /    |
                      |
              =========""",
              """
                  +---+
                  |   |
                  O   |
                 /|\\  |
                 / \\  |
                      |
              ========="""]



## Funcion que obtiene una palabra aleatoria de la API
def get_random_word():
    url = "https://clientes.api.greenborn.com.ar/public-random-word?c=1&l=8"
    response = requests.get(url=url)
    text_results = response.json()
    return text_results[0]

## Funcion que oculta las letras de la palabra
def offuscate_word(positions, word):

    offuscated_word = ''
    for index, letter in enumerate(word):
        offuscated_word += '_' if index in positions else letter

    return offuscated_word


## Funcion que obtiene las posiciones de las letras a ocultar
def hidden_positions(word):
    return random.sample(range(len(word)), int(len(word) * 0.6))


## Funcion que remueve las posiciones de las letras acertadas
def remove_position_letter(positions:list[int],letter:str,word:str):
    if(letter in word):
        positions.sort()
        aux = positions.copy()
        for i in aux:
            if(word[i] == letter):
                positions.remove(i)

## Funcion que verifica si la letra ingresada es correcta
def check_letter(letters:str,letter,word):
    for index in range(len(letters)):
        if letter == word[index]:
            return True



## Funcion que ejecuta el juego
def game():

    maxAttemps = 5
    attemps=0
    letters_used = []
    word = get_random_word()
    positions_letters = hidden_positions(word)
    word_offuscated = offuscate_word(positions_letters,word)
    isFinished = False
    isWinner = False


    while attemps < 5 and not isFinished:
        print(hangStates[attemps])
        print('Palabra a adivinar: ' + word_offuscated)
        print('Intentos restantes:'  + str(maxAttemps-attemps) + ' intentos')
        print('Letras usadas: ' + str(letters_used))
        letter = input('Ingresa una letra o la palabra completa: ')
        if letter == word:
            print('Has acertado la palabra !' + word)
            isFinished = True
            isWinner = True
            break
        elif check_letter(word_offuscated,letter,word):
            remove_position_letter(positions_letters,letter,word)
            word_offuscated = offuscate_word(positions_letters, word)
            print('Has acertado la letra '+ letter + '!')
            if (word_offuscated == word):
                print('Has acertado la palabra ' + word)
                isFinished = True
                isWinner = True
        else:
            print('Has fallado la letra '+ letter + '!')
            attemps += 1
            if(letters_used.count(letter) == 0):
                letters_used.append(letter)



    if(not isWinner):
        print('Has perdido, la palabra era ' + word)





game()




