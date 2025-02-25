import math
def check_number(n):
    primo = 'no es primo'
    fibonacci_n = 'no es fibonacci'
    even = 'es impar'
    if prime(n):
        primo = 'es primo'
    if fibonacci(n):
        fibonacci_n = 'es fibonacci'
    if par(n):
        even = 'es par'
    return f'el numero {n},{primo},{even},{fibonacci_n}'
def prime(n):
    if n <= 1:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def fibonacci(n):
    if n < 0:
        return False
    return es_cuadrado_perfecto(5 * n**2 + 4) or es_cuadrado_perfecto(5 * n**2 - 4)

def es_cuadrado_perfecto(x):
    raiz = int(math.sqrt(x))
    return raiz * raiz == x
def par(n):
    return True if n % 2 == 0 else False


print(check_number(5))