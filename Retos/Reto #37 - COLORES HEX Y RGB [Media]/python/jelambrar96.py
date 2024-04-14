#!/usr/bin/python3

"""
# Reto #37: Colores HEX y RGB
/*
 * Crea las funciones capaces de transformar colores HEX
 * a RGB y viceversa.
 * Ejemplos:
 * RGB a HEX: r: 0, g: 0, b: 0 -> #000000
 * HEX a RGB: hex: #000000 -> (r: 0, g: 0, b: 0)
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


def RGB_a_HEX(r: int, g: int, b: int):
    assert r >= 0 and r < 256, "r >= 0 and r < 256"
    assert g >= 0 and g < 256, "g >= 0 and g < 256"
    assert b >= 0 and b < 256, "b >= 0 and b < 256"
    number = r * 256 * 256 + g * 256 + b
    hex_number =  hex(number)[2:].upper()
    hex_number = '#' + '0' * (6 - len(hex_number)) + hex_number
    return hex_number


def HEX_a_RGB(cadena: str):
    cadena = cadena.replace("#", "")
    assert len(cadena) == 6, "Error, Invalid input"
    cadena_r = cadena[0:2]
    cadena_g = cadena[2:4]
    cadena_b = cadena[4:6]
    return int(cadena_r, 16), int(cadena_g, 16), int(cadena_b, 16)

if __name__ == '__main__':
    r = 12
    b = 192
    g = 212
    print("original:", r, g, b)
    hex_color = RGB_a_HEX(r, g, b)
    print("hexadecimal:", hex_color)
    rgb_color = HEX_a_RGB(hex_color)
    print("rgb", rgb_color)


