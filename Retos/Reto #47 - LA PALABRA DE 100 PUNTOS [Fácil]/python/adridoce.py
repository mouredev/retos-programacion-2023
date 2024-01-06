"""
/*
 * Crea un programa que calcule los puntos de una palabra.
 * - Cada letra tiene un valor asignado. Por ejemplo, en el abecedario
 *   español de 27 letras, la A vale 1 y la Z 27.
 * - El programa muestra el valor de los puntos de cada palabra introducida.
 * - El programa finaliza si logras introducir una palabra de 100 puntos.
 * - Puedes usar la terminal para interactuar con el usuario y solicitarle
 *   cada palabra.
 */
"""

import string

def calcula_puntos():
    alfabeto = list(string.ascii_lowercase)
    alfabeto.insert(alfabeto.index('n') + 1, 'ñ')

    while True:
        palabra = input("Introduce una palabra:").lower()
        puntos = 0

        for posicion in palabra:
            for letra in alfabeto:
                if posicion == letra:
                    puntos += alfabeto.index(letra) + 1
        
        print(f"Palabra introducida: {palabra} Puntos: {puntos}")

        if puntos == 100:
            print("Has ganado, enhorabuena!!")
            return True       

calcula_puntos() 