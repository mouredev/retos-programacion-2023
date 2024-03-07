#!/usr/bin/python3

"""
# Reto #47: La palabra de 100 puntos
/*
 * La última semana de 2021 comenzamos la actividad de retos de programación,
 * con la intención de resolver un ejercicio cada semana para mejorar
 * nuestra lógica... ¡Hemos llegado al EJERCICIO 100! Gracias 🙌
 *
 * Crea un programa que calcule los puntos de una palabra.
 * - Cada letra tiene un valor asignado. Por ejemplo, en el abecedario
 *   español de 27 letras, la A vale 1 y la Z 27.
 * - El programa muestra el valor de los puntos de cada palabra introducida.
 * - El programa finaliza si logras introducir una palabra de 100 puntos.
 * - Puedes usar la terminal para interactuar con el usuario y solicitarle
 *   cada palabra.
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



LISTA_LETRAS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q',
                'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def puntos_palabra(palabra: str):
    puntos = sum([ LISTA_LETRAS.index(item) for item in palabra ])
    puntos += len(palabra)
    return puntos


def main():
    while True:
        palabra = input("Escriba una palabra que llegue a 100 puntos: ")
        palabra = palabra.lower()
        puntos = puntos_palabra(palabra)
        if puntos == 100:
            print("Has ganado, tu palabra tiene 100 puntos")
            break
        print(f"Su palabra tiene un valor de {puntos} puntos")


if __name__ == '__main__':
    main()


