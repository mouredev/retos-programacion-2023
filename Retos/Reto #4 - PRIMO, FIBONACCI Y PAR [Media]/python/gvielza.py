#/*
 #* Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 #* Ejemplos:
 #* - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
# * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"

import math

numero=int(input('escribe un numero: '))


def es_par(valor):
    if valor%2==0:
        return True
    else:
        return False

def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True
def es_fibonacci(num):
    if (math.sqrt(5*num**2 + 4) % 1 == 0) or (math.sqrt(5*num**2 - 4) % 1 == 0):
        return True
    else:
        return False

def resultado(numero):
    cadena="el numero "+str(numero)
    if es_par(numero):
        cadena+=" es un numero par"
    else:
        cadena+=" es un numero impar"
    if es_primo(numero):
        cadena+=", es primo"
    else:
        cadena+=", no es primo"
    if es_fibonacci(numero):
        cadena+=" y es fibonnacci"
    else:
        cadena+=" y no es fibonacci"
    return cadena

print(resultado(numero))




