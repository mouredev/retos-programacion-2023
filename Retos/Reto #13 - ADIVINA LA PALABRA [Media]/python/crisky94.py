# /*
#  * Crea un pequeño juego que consista en adivinar palabras en un número máximo de intentos:
#  * - El juego comienza proponiendo una palabra aleatoria incompleta
#  *   - Por ejemplo "m_ur_d_v", y el número de intentos que le quedan
#  * - El usuario puede introducir únicamente una letra o una palabra (de la misma longitud que
#  *   la palabra a adivinar)
#  *   - Si escribe una letra y acierta, se muestra esa letra en la palabra. Si falla, se resta
#  *     uno al número de intentos
#  *   - Si escribe una resolución y acierta, finaliza el juego, en caso contrario, se resta uno
#  *     al número de intentos
#  *   - Si el contador de intentos llega a 0, el jugador pierde
#  * - La palabra debe ocultar de forma aleatoria letras, y nunca puede comenzar ocultando más del 60%
#  * - Puedes utilizar las palabras que quieras y el número de intentos que consideres
#  */

import random

def adivina_palabra():
    palabras = ["murcielago", "perro", "gato", "elefante", "caballo", "tigre", "leon", "jirafa", "mono", "oso"]
    palabra = random.choice(palabras)
    palabra_oculta = palabra[0] 
    num_letras_ocultas = random.randint(int(len(palabra) * 0.4), int(len(palabra) * 0.6))
    indices_ocultos = random.sample(range(len(palabra)), num_letras_ocultas) 
    palabra_oculta = "".join("_" if i in indices_ocultos else palabra[i] for i in range(len(palabra)))
    intentos = 5
    while intentos > 0:
        print(f"Palabra: {palabra_oculta} - Intentos restantes: {intentos}")
        respuesta = input("Introduce una letra o una palabra: ")
        if len(respuesta) == 1:
            if respuesta in palabra:
                letras = list(palabra_oculta)
                for i in range(len(palabra)):
                    if palabra[i] == respuesta:
                        letras[i] = respuesta
                palabra_oculta = "".join(letras)
            else:
                intentos -= 1
        elif len(respuesta) == len(palabra):
            print("¡Has acertado!")
            break
        else:
            intentos -= 1
        if palabra_oculta == palabra:
            print(f"¡Has acertado! La palabra era {palabra}")
            break
    if intentos == 0:
        print(f"¡Has perdido! La palabra era {palabra}")

adivina_palabra()


