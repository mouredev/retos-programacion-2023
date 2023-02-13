
# Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
# Ejemplos:
# - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
# - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"


def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def es_fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n

def es_par(n):
    return n % 2 == 0

def resultado(n):
    resultado = []
    if es_primo(n):
        resultado.append("primo")
    if es_fibonacci(n):
        resultado.append("fibonacci")
    if es_par(n):
        resultado.append("par")
    else:
        resultado.append("impar")
    return resultado

numero = int(input("Introduce un número: "))
resultado = resultado(numero)

if "primo" in resultado:
    print("{} es primo".format(numero), end=", ")
else:
    print("{} no es primo".format(numero), end=", ")

if "fibonacci" in resultado:
    print("es fibonacci", end=", ")
else:
    print("no es fibonacci", end=", ")

if "par" in resultado:
    print("es par.")
else:
    print("es impar.")
