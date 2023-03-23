'''
 Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 Ejemplos:
 - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
'''
import math

def is_fibonacci(num: int) -> bool:
    a, b = 0, 1
    while b < num:
        a, b = b, a + b
    return b == num

def is_prime(num:int) -> bool:
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def is_even(num: int) -> bool:
    return num % 2 == 0

def check_even_fibonacci_prime(num: int) -> str:
    result = '{} '.format(num)
    result += f"{'es primo, ' if is_prime(num) else 'no es primo, '}"
    result += f"{'fibonacci' if is_fibonacci(num) else 'no es fibonacci'}"
    result += f"{' y es par' if is_even(num) else ' y es impar'}"
    return result


print(check_even_fibonacci_prime(2))
