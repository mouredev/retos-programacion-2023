#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
### Reto #0: EL FAMOSO "FIZZ BUZZ” ###

https://retosdeprogramacion.com/

Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""

def fizz_buzz():
    for num in range(1, 101):
        output = ""
        if not num % 3:
            output = "fizz"
        if not num % 5:
            output += "buzz"
        if not len(output):
            output = num
        print(output)

fizz_buzz()