'''/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */'''


def primo_fibonacci_par(numero):
    # Comprobamos si es primo
    if numero > 1:
        for i in range(2, numero):
            if numero % i == 0:
                print(f'{numero} no es primo')
                break
        else:
            print(f'{numero} es primo')
    else:
        print(f'{numero} no es primo')

    # Comprobamos si es fibonacci
    a = 0
    b = 1
    while b < numero:
        a, b = b, a + b  # a = b, b = a + b
    if b == numero:
        print(f'{numero} es fibonacci')
    else:
        print(f'{numero} no es fibonacci')

    # Comprobamos si es par
    if numero % 2 == 0:
        print(f'{numero} es par')
    else:
        print(f'{numero} es impar')


numero = int(input('Introduce un número: '))
primo_fibonacci_par(numero)
