"""
 Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 Ejemplos:
 - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
"""

import math
import os


def esprimo(num):
    CONTADOR = 0
    for i in range(1, num+1):
        for n in {num % i}:
            if n == 0:
                CONTADOR += 1
    if CONTADOR == 2:
        return True
    else:
        return False


def esfibonacci(num):
    a = (5*(num*num))+4
    b = (5*(num*num))-4
    c = int(math.sqrt(a))
    d = int(math.sqrt(b))
    if c**2 == a or d**2 == b:
        return True
    else:
        return False


def espar(num):
    if num % 2 == 0:
        return True
    else:
        return False


def main():
    SALIR = False
    while SALIR == False:
        os.system('cls')
        print("¿TÚ NÚMERO ES PRIMO, FIBONACCI O PAR?")
        num = input('Escribe un número: ')
        print('*'*40)
        if num.isnumeric():
            num = int(num)
            # /
            if esprimo(num):
                p = "es primo"
            else:
                p = "no es primo"
            if esfibonacci(num):
                f = "es fibonacci"
            else:
                f = "no es fibonacci"
            if espar(num):
                par = "es par"
            else:
                par = "no es par"
            # /
            print(f"{num} {p}, {f} y {par}")
            # /
            r = input("¿Quieres salir? si/no: ")
            if r.upper() == "SI":
                SALIR = True
            else:
                SALIR = False
        else:
            SALIR = False


if __name__ == '__main__':
    main()
