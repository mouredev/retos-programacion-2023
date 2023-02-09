from math import sqrt

def es_primo(num: int) -> bool:
    if num <= 1:
        return False
    for i in range(1, num + 1):
        if i != 1 and i != num:
            if num % i == 0:
                return False
    return True

def es_fibonacci(num: int) -> bool:
    if num == 0 or num == 1:
        return True
    n1 = 5*num*num + 4
    n2 = 5*num*num - 4
    s1 = int(sqrt(n1))
    s2 = int(sqrt(n2))
    return s1*s1 == n1 or s2*s2 == n2

def es_par(num: int) -> bool:
    return num % 2 == 0

def mostrar_categorias(num: int) -> None:
    primo = "es primo"
    fib = "fibonacci"
    par = "par"
    if not es_primo(num):
        primo = "no es primo"
    if not es_fibonacci(num):
        fib = "no es fibonacci"
    if not es_par(num):
        par = "es impar"
    print(f'{num} {primo}, {fib} y {par}')

mostrar_categorias(2)
mostrar_categorias(7)
