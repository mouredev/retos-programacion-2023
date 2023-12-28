""" Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
* Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
"""

"""Método para comprobar si un número es par"""
def is_par(number):
    return number % 2 == 0

"""Método para comprobar si un número es fibonacci"""
def is_fibonacci(number):
    a = 0
    b = 1

    if number == 0:
        return True

    while b < number:
        a, b = b, a + b
    return b == number

"""Método para comprobar si un número es primo"""
def is_prime(number):
    if number < 2:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False
    return True

"""Método para imprimir por pantalla si un número es primo, fibonacci y par"""
def is_prime_fibonacci_par(number):
    return f"{number} es {'primo, ' if is_prime(number) else ''}{'fibonacci, ' if is_fibonacci(number) else ''}{'par' if is_par(number) else 'impar'}"


""" Casos de prueba """

if __name__ == "__main__":

    print(is_prime_fibonacci_par(2))
    print(is_prime_fibonacci_par(7))
    print(is_prime_fibonacci_par(13))
    print(is_prime_fibonacci_par(14))
    print(is_prime_fibonacci_par(15))
    print(is_prime_fibonacci_par(16))
    print(is_prime_fibonacci_par(-20))
    print(is_prime_fibonacci_par(0))



