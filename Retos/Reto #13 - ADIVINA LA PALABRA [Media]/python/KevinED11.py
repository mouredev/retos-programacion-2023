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

from random import choice
from os import system as os_system
import math

# Palabras que se usaran para el juego elegida de manera random
palabras: list[str] = ["combate", "dinero",
                       "amenaza", "banana",
                       "manzana", "naranja",
                       "pera"]


def adivinar_palabra() -> None:
    """ Funcion principal encargada de mover el juego de adivinanza de palabra.
    """

    palabra_a_jugar: str = choice(palabras)

    palabra_sustituida_con_guiones: str = palabra_a_jugar

    longitud_de_la_palabra: int = len(palabra_a_jugar)

    NUMERO_DE_INTENTOS: int = 3

    numero_de_letras_a_ocultar = math.floor(
        len(palabra_sustituida_con_guiones) / 2)

    def mensaje_inicial() -> None:
        """Da el mensaje inicial del juego
        """
        print(
            f"La palabra tiene un total de: {longitud_de_la_palabra} caracteres")

        print(
            f"La palabra es: '{palabra_sustituida_con_guiones}'"
        )

        print(
            f"Te quedan: {NUMERO_DE_INTENTOS} intentos")

    def limpieza_de_terminal() -> None:
        """se encargara de limpiar la terminal
        """
        os_system(command="clear")

    def mensaje_al_ganador() -> None:
        """Se encargara de mostrarle al usuario que ha ganado
        """
        print(
            f"\n¡Felicidades haz ganado!, la palabra era: '{palabra_a_jugar}'")

    # Bucle en el que se remplazan letras por guiones bajos
    letras_a_sustituir: list[str] = []

    while len(letras_a_sustituir) < numero_de_letras_a_ocultar:

        letra = choice(
            palabra_sustituida_con_guiones)

        if letra != "_":
            letras_a_sustituir.append(letra)

            palabra_sustituida_con_guiones = palabra_sustituida_con_guiones.replace(
                letra, "_", 1)

    # Bucle en el que se inicia el juego pidiendole preguntas al usuario
    while NUMERO_DE_INTENTOS > 0:
        limpieza_de_terminal()
        # mensaje inicial
        mensaje_inicial()

        try:
            pregunta: str = input("Ingresa la palabra o letra: ")

        except KeyboardInterrupt:
            break

        if pregunta == "":
            print("\n")

            continue

        if len(pregunta) > longitud_de_la_palabra:
            limpieza_de_terminal()

            print(
                "Debes ingresar una palabra de la misma longitud\n")
            continue

        # verificación de la palabra enviada, si coincide el juego termina y se le informa que ha ganado
        if len(pregunta) > 1 and pregunta == palabra_a_jugar:
            mensaje_al_ganador()

            break

        # Bloque de código que se encarga de evaluar la ocación en la que se mande una letra y este o no dentro de la palabra

        if len(pregunta) == 1 and pregunta in [letra for letra in palabra_a_jugar]:
            limpieza_de_terminal()

            palabra_dividida_guiones: list[str] = [
                letra for letra in palabra_sustituida_con_guiones]

            for i, letra in enumerate(palabra_a_jugar):
                if pregunta == letra:
                    palabra_dividida_guiones[i] = letra

            palabra_sustituida_con_guiones = "".join(palabra_dividida_guiones)

            # si adivina todas las letras se le informa que ha ganado
            if palabra_sustituida_con_guiones == palabra_a_jugar:
                mensaje_al_ganador()

                break

            continue

        else:
            limpieza_de_terminal()

            NUMERO_DE_INTENTOS -= 1

            if NUMERO_DE_INTENTOS == 0:
                print(
                    f"Haz fallado, vuelve a intentarlo, la palabra era {palabra_a_jugar}")
                break

            continue


if __name__ == "__main__":
    adivinar_palabra()
