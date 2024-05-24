"""
Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
Ejemplos:
- Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
- Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
"""


def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def es_fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n or n == 0


def es_par(n):
    return n % 2 == 0


def verificar_numero(n):
    primo = es_primo(n)
    fibonacci = es_fibonacci(n)
    par = es_par(n)

    resultado = f"{n} "
    if primo:
        resultado += "es primo, "
    else:
        resultado += "no es primo, "

    if fibonacci:
        resultado += "es fibonacci, "
    else:
        resultado += "no es fibonacci, "

    if par:
        resultado += "y es par"
    else:
        resultado += "y es impar"

    return resultado


# Ejemplos
print(verificar_numero(2))  # "2 es primo, es fibonacci, y es par"
print(verificar_numero(7))  # "7 es primo, no es fibonacci, y es impar"
print(verificar_numero(8))  # "8 no es primo, es fibonacci, y es par"
