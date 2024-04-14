#!/usr/bin/python3

"""
# Reto #30: El teclado T9
/*
 * Los primeros dispositivos móviles tenían un teclado llamado T9
 * con el que se podía escribir texto utilizando únicamente su
 * teclado numérico (del 0 al 9).
 *
 * Crea una función que transforme las pulsaciones del T9 a su
 * representación con letras.
 * - Debes buscar cuál era su correspondencia original.
 * - Cada bloque de pulsaciones va separado por un guión.
 * - Si un bloque tiene más de un número, debe ser siempre el mismo.
 * - Ejemplo:
 *     Entrada: 6-666-88-777-33-3-33-888
 *     Salida: MOUREDEV
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



T9_KEYBOARD = [" ", ",.?!", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]


def traducir_t9_a_palabra(cadena:str):
    salida = None
    try:
        lista_palabras = cadena.split("-")
        lista_index = [ (int(item[0]), len(item) - 1) for item in lista_palabras ]
        lista_letras = [ T9_KEYBOARD[index1][index2] for index1, index2 in lista_index ]
        salida = "".join(lista_letras)
    except ValueError as ve:
        print(ve)
    except IndexError as ie:
        print(ie)
    return salida


if __name__ == '__main__':
     print(traducir_t9_a_palabra("6-666-88-777-33-3-33-888"))



