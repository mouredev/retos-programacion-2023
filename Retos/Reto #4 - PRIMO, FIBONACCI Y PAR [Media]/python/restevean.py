"""
Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 Ejemplos:
 - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
"""


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def is_fibonacci(n):
    x, y = 0, 1
    while y < n:
        x, y = y, x + y
    return y == n


def is_even(n):
    return n % 2 == 0


def check_number(n):
    primo = "is prime" if is_prime(n) else "it is not prime"
    fibonacci = "is fibonacci" if is_fibonacci(n) else "it is not fibonacci"
    par = "is even" if is_even(n) else "it is not even"
    return f"{n} {primo}, {fibonacci} y {par}"


print(check_number(0))
print(check_number(2))
print(check_number(1))
print(check_number(3))
print(check_number(4))
print(check_number(5))
print(check_number(6))
print(check_number(7))
