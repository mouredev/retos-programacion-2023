#!/usr/bin/python3

"""
# Reto #28: Expresión matemática
/*
 * Crea una función que reciba una expresión matemática (String)
 * y compruebe si es correcta. Retornará true o false.
 * - Para que una expresión matemática sea correcta debe poseer
 *   un número, una operación y otro número separados por espacios.
 *   Tantos números y operaciones como queramos.
 * - Números positivos, negativos, enteros o decimales.
 * - Operaciones soportadas: + - * / % 
 *
 * Ejemplos:
 * "5 + 6 / 7 - 4" -> true
 * "5 a 6" -> false
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




def revisar_expresion(expresion: str):
    # no debe contener alpha
    is_alpha = sum([ 1 if c.isalpha() else 0 for c in expresion ])
    if is_alpha > 0:
        # print("is_alpha", expresion)
        return False
    # debe contener numeros y simbolos validos
    is_simbols = sum([ 1 if not c in " 1234567890+-*%/." else 0 for c in expresion ])
    if is_simbols > 0:
        # print("wrong simbol", expresion)
        return False
    operadores = {'+', '-', '*', '/', '%'}
    elementos = expresion.split()
    
    if len(elementos) % 2 == 0:
        # print("bad length", elementos)
        return False  # Número incorrecto de elementos
    
    for i, elem in enumerate(elementos):
        if i % 2 == 0:  # Elementos en posición par son números
            try:
                float(elem)
            except ValueError:
                # print("bad number", elementos)
                return False  # No es un número válido
    return True


if __name__ == '__main__':
    print('"6+5+43"', revisar_expresion("6+5+43"))
    print('"6 +5"', revisar_expresion("6 +5"))
    print('"6 + 555487"', revisar_expresion("6 + 555487"))
    print('"6 +"', revisar_expresion("6 +")) 
