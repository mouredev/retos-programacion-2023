'''/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */'''

def fibonacci(n):
    f = [0, 1]
    j = 0
    for i in range(n):
        j += f[-1] + f[-2]
        f.append(j)
        j = 0
    if n not in f:
        return 'no es fibonacci'
    else:
        return 'fibonacci'

def es_par(n):
    if n % 2 != 0:
        return 'no es par'
    else:
        return 'es par'

def es_primo(n):
    lista = [1, 2, 3, 5, 7, 11]
    if n not in lista or (n % 2 == 0 and n % 3 == 0 and n % 5 == 0 and n % 7 == 0 and n % 11 == 0):
        return 'no es primo'
    else:
        return 'es primo'

n = int(input('Introduce un numero: '))

print(f'{n} {es_primo(n)}, {fibonacci(n)} y {es_par(n)}')
