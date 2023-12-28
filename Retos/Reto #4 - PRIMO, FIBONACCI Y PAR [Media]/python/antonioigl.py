""""
/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */
"""


def prime_number_checker(candidate: int) -> bool:
    count: int = 0
    for i in range(1, candidate + 1):
        if candidate % i == 0:
            count += 1
        if count > 2:
            return False

    return True


def fibonacci_checker(candidate: int) -> bool:
    fibonacci_numbers: list = [0, 1]
    last_fibonacci_number: int = fibonacci_numbers[-2] + fibonacci_numbers[-1]

    while last_fibonacci_number < candidate:
        last_fibonacci_number = fibonacci_numbers[-2] + fibonacci_numbers[-1]
        fibonacci_numbers.append(last_fibonacci_number)

    if last_fibonacci_number == candidate:
        return True

    return False


def even_number_checker(candidate: int) -> bool:
    return candidate % 2 == 0


if __name__ == "__main__":
    number = 10
    prime_number: str = "es primo" if prime_number_checker(number) else "no es primo"
    fibonacci: str = "fibonacci" if fibonacci_checker(number) else "no es fibonacci"
    even_number: str = "par" if even_number_checker(number) else "impar"

    print(f"{number} {prime_number}, {fibonacci} y es {even_number}")
