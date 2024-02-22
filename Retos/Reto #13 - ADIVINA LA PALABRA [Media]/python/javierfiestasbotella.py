'''/*
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
 */'''

import random

intentos = 3
palabras = ["perro", "gato", "casa", "árbol", "coche", "libro", "computadora", "mesa", "silla", "teléfono"]

def show_original():
    return random.choice(palabras)

def show(word):
    letras_a_reemplazar = int(len(word) * 0.6)
    lista_palabra = list(word)
    indices_reemplazo = random.sample(range(len(word)), letras_a_reemplazar)
    for indice in indices_reemplazo:
        lista_palabra[indice] = '_'
    return ''.join(lista_palabra)

def check_letter(letter, word):
    global intentos
    aciertos = {}
    for idx, char in enumerate(word):
        if char == letter:
            aciertos[idx] = letter
    if not aciertos:
        intentos -= 1
    return aciertos

def check_live(intentos):
    if intentos == 0:
        print('GAME OVER!!!')
        return False
    else:
        print(f'Te quedan {intentos} intentos!!')
        return True

def autocompleta(d, incompleta):
    for indice, letra in d.items():
        incompleta = incompleta[:indice] + letra + incompleta[indice+1:]
    return incompleta

if __name__ == "__main__":
    level = show_original()
    incompleta = show(level)
    while True:
        print(incompleta)
        player = input('Introduce una letra o una palabra: ')
        if len(player) > 1:
            if player == level:
                print('¡CORRECTO! ¡Has adivinado la palabra!')
                break
            else:
                intentos -= 1
                print('Lo siento, esa no es la palabra correcta.')
                if not check_live(intentos):
                    break
        else:
            d = check_letter(player, level)
            incompleta = autocompleta(d, incompleta)
            if '_' not in incompleta:
                print('¡CORRECTO! ¡Has adivinado la palabra!')
                break
            else:
                if not check_live(intentos):
                    break
