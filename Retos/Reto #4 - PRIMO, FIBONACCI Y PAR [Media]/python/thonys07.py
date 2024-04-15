"""
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"

"""
from math import sqrt


def primos (n):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                return False
            return True
        
    else: return False    

def cuadrado_perfecto(n):
    raiz = int(n**0.5)
    return n == raiz**2
def fibonacci(n):
    if cuadrado_perfecto(5*n**2+4) or cuadrado_perfecto(5*n**2-4) :
        return True
    else:
        return False
def par(n):
    if n % 2 == 0:
        return True
    else:
        return False

def prim_fibo_par():
    n=int(input("Ingresa un numero: "))
    resultado=f"el numero {n} "
    if primos(n):
        resultado+="es primo, "
    else:
        resultado+="no es primo, "
    if fibonacci(n):
        resultado+="es fibonacci "
    else:
        resultado+="no es fibonacci "
    if par(n):
        resultado+="y es par"
    else:
        resultado+="y es impar"

    print(resultado)


prim_fibo_par()

   