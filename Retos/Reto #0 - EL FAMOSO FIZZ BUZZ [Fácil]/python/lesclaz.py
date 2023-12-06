#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Ejercicio:
# Escribe un programa que muestre por consola (con un print) los
# números de 1 a 100 (ambos incluidos y con un salto de línea entre
# cada impresión), sustituyendo los siguientes:
# - Múltiplos de 3 por la palabra "fizz".
# - Múltiplos de 5 por la palabra "buzz".
# - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".

def main():
    for _ in range(1, 101):
        if _ % 3 == 0 and _ % 5 == 0:
            print('fizzbuzz')
        elif _ % 3 == 0:
            print('fizz')
        else:
            print('buzz' if _ % 5 == 0 else _)


if __name__ == '__main__':
    main()
