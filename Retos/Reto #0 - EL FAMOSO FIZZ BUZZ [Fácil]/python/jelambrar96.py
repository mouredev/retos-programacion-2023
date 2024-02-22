#!/usr/bin/python3
"""
/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
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

def main():
    for i in range(1,101,1):
        number = i
        if number % 15 == 0:
            print(number, "fizzbuzz", sep=" - ")
        elif number % 5 == 0:
            print(number, "buzz", sep=" - ") 
        elif number % 3 == 0:
            print(number, "fizz", sep=" - ")
        else:
            print(number)

if __name__ == '__main__':
    main()
