# /*
#  * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
#  * Ejemplos:
#  * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
#  * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
#  */

# Crear funcion is_primo
def is_primo(n):
    if n <= 1:
        return "no es primo"
    if n == 2:
        return "es primo"
    if n % 2 == 0:
        return "no es primo"
        
    i = 3
    while i <= n ** 0.5:
        if n % i == 0:
            return "no es primo"  # Si tiene algún divisor, no es primo
        i += 2
    
    return "es primo"

# Crear funcion is_fibonacci
def is_fibonacci(n):
    arr = []
    a, b = 0, 1
    while a <= n:
        arr.append(a)
        a, b = b, a + b
    
    if n in arr:
        return "fibonacci"
    else:
        return "no es fibonacci"


# Crear funcion is_pair
def is_pair(n):
    if n % 2 == 0:
        return "es par"
    else:
        return "es impar"

# Funcion principal
def main(num):
    print(f'{num} {is_primo(num)}, {is_fibonacci(num)} y {is_pair(num)}')


main(2)
main(7)
main(10)
main(29)
main(30)
