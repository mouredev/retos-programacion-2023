#!/usr/bin/python3

"""
# Reto #20: La Trifuerza
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
 *
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


def simple_triangle(n):
    out_string = []
    for i in range(n):
        temp_string = "*" * i + " " * (n - i - 1)
        temp_string = temp_string[::-1] + "*" + temp_string
        out_string.append(temp_string)
    return out_string


def triforce_triangle(n):
    s_triangle = simple_triangle(n)
    out = []
    for item in s_triangle:
        out.append(" " * n + item + " " * n)
    for item in s_triangle:
        out.append(item + " " + item)
    return out


def show_triangle(list_in):
    for item in list_in:
        print(item)


if __name__ == '__main__':
    
    n = 5
    print(f"para n = {n}")
    triforce = triforce_triangle(n)
    show_triangle(triforce)
    print()
    
    n = 4
    print(f"para n = {n}")
    triforce = triforce_triangle(n)
    show_triangle(triforce)
    print()
    


