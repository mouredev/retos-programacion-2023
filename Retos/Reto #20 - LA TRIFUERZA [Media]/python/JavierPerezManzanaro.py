"""
/*
 *	¡El nuevo "The Legend of Zelda: Tears of the Kingdom" ya está disponible!
 *
 * Crea un programa que dibuje una Trifuerza de "Zelda"
 * formada por asteriscos.
 * - Debes indicarle el número de filas de los triángulos con un entero positivo (n).
 * - Cada triángulo calculará su fila mayor utilizando la fórmula 2n-1.
 *
 * Ejemplo: Trifuerza 2
 *
 *    *
 *   ***
 *  *   *
 * *** ***
"""

import os


def triforce(filas: int)->None:
    base = (2*filas)-1
    # * Primer triangulo, esta desplazado a la derecha
    for i in range(1, filas+1):
        huecos = filas - i
        asteriscos = base - huecos *2
        cadena_que_pinta = ' ' * huecos + '*' * asteriscos + ' ' * huecos
        print(' '* filas + cadena_que_pinta)
    # * Segundo y tercer triangulos que son paralelos
    for i in range(1, filas+1):
        huecos = filas - i
        asteriscos = base - huecos *2
        cadena_que_pinta = ' ' * huecos + '*' * asteriscos + ' ' * huecos
        print(cadena_que_pinta * 2)

if __name__ == '__main__':
    os.system('clear')


    filas = int(input('¿Número de filas de alto para cada estrella? '))
    print()
    triforce(filas)
