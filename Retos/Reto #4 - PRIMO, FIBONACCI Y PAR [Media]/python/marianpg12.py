"""
/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */
"""

# ------ Tres funciones, luego las llamo -------

def is_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**(1/2))+1):      #numero primo
        if n % i == 0:
            return False
    return True

def is_fibonacci(n):
    if n == 0 or n == 1:
        return True
    a, b = 0, 1
    while b < n:     
        a, b = b, a + b          # 1, 2, 3, 5, 8, 13, 21, 34, etc.
    return b == n

def is_par(n):
    return n % 2 == 0            # es par?

def check_number(n):
    if is_primo(n):
        print(f"{n} es primo,", end=' ')
    else:
        print(f"{n} no es primo,", end=' ')
    if is_fibonacci(n):
        print("es fibonacci,", end=' ')
    else:
        print("no es fibonacci,", end=' ')
    if is_par(n):
        print("es par.")
    else:
        print("es impar.")

check_number(2)
check_number(7)
check_number(17)
check_number(10)
check_number(55)
