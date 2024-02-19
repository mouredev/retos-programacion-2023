'''
 * Escribe un programa que, dado un número, compruebe y muestre si es primo,
 * fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
'''

import math

def main():
    try:
        valor = int(input("Ingresa un número para verificar si es primo, fibonacci y par: "))
        verificar(valor)
    except ValueError:
        print("Ingresa valores válidos.")

def verificar(dato):
    print(f"{dato} {es_primo(dato)}, {es_fibonacci(dato)} y {par_impar(dato)}")

def par_impar(dato):
    if dato % 2 == 0:
        return "es par"
    else:
        return "es impar"

def es_primo(numero):
    if numero <= 1:
        return "no es primo"

    for i in range(2, int(math.sqrt(numero)) + 1):
        if numero % i == 0:
            return "no es primo"

    return "es primo"

def es_fibonacci(dato):
    a, b = 0, 1
    contador = 0

    while contador < 1000:
        temp = a + b
        a, b = b, temp

        if a == dato:
            return "fibonacci"
        contador += 1

    return "no es fibonacci"

if __name__ == "__main__":
    main()
