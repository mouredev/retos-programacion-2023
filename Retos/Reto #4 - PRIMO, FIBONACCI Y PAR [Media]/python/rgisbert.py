"""
 Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 Ejemplos:
 - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
"""


class ZeroOrNegativeNumber(Exception):
    pass


def is_fibonacci(n):
    fibonacci = [1, 1]

    while fibonacci[-1] < n:
        one, two = fibonacci[-1], fibonacci[-2]
        fibonacci.append(one + two)

    return n in fibonacci


def is_pair(n):
    return n % 2 == 0


def is_prime(n):
    if n == 1:
        return False

    for x in range(2, n - 1):
        if (n % x == 0):
            return False

    return True


def main():
    try:
        num = int(input("Introduzca un número entero positivo: "))

        if num <= 0:
            raise ZeroOrNegativeNumber

        text_result = "es primo, " if is_prime(num) else "no es primo, "
        text_result += "es fibonacci y " if is_fibonacci(
            num) else "no es fibonacci y "
        text_result += "es par" if is_pair(num) else "es impar"

        print(f"{num} {text_result}.")

    except ValueError:
        print("Se esperaba un número entero")
    except ZeroOrNegativeNumber:
        print("Debe escribir un número mayor a 0")


if __name__ == "__main__":
    main()
