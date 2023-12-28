"""
 *
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 *
"""
import sys


def check(number: int):
    print(number, end="")
    print(" es primo" if is_prime(number) else " no es primo", end="")
    print(", fibonacci" if is_fibo(number) else ", no es fibonacci", end="")
    print(" y es par" if is_pair(number) else " y es impar")


def is_pair(number: int):
    return number % 2 == 0


def is_prime(number: int):
    if number == 0 or number == 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def is_fibo(number: int):
    a = 0
    b = 1
    while a < number:
        c = a + b
        a = b
        b = c
    return a == number


if __name__ == "__main__":
    number = sys.argv[1] if len(sys.argv) == 2 else input("Introduce un número: ")
    try:
        number = int(number)
    except:
        print("Error: Debes introducir un número")
        sys.exit(1)

    check(number)
