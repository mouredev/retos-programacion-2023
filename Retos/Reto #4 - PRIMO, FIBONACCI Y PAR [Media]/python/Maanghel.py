"""
Escribe un programa que, dado un número, compruebe y muestre si es primo,
    fibonacci y par.
Ejemplos:
- Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
- Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
"""

import math

def is_prime_fibonacci_even(number: int) -> str:
    """
    Given an integer `number`, returns a sentence stating whether the number
    is prime, whether it belongs to the Fibonacci sequence, and whether it is even or odd.

    Returns format:
        "{n} es/no es primo, es/no es fibonacci y es par/impar"

    Args:
        number (int): the integer to analyze.

    Raises:
        TypeError: if `number` is not an int.
    """
    if not isinstance(number, int):
        raise TypeError("El numero debe ser un entero.")

    even = number % 2 == 0

    if number < 2:
        prime = False
    elif number == 2:
        prime = True
    elif number % 2 == 0:
        prime = False
    else:
        prime = True
        limit = math.isqrt(number)
        for i in range(3, limit + 1, 2):
            if number % i == 0:
                prime = False
                break

    def _is_perfect_square(x: int) -> bool:
        if x < 0:
            return False
        square = math.isqrt(x)
        return square * square == x

    fibonacci = _is_perfect_square(5 * number * number + 4) or _is_perfect_square(5 * number * number - 4)

    prime_str = "es primo" if prime else "no es primo"
    fib_str = "es fibonacci" if fibonacci else "no es fibonacci"
    parity_str = "es par" if even else "es impar"

    return f"{number} {prime_str}, {fib_str} y {parity_str}"


if __name__ == "__main__":
    print(is_prime_fibonacci_even(5))
