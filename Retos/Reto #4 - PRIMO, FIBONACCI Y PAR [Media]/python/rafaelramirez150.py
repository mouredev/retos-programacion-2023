'''
/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */
 '''
def primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def fibonacci(numero):
    a, b = 0, 1
    while a < numero:
        if a == numero:
            return True
        a, b = b, a + b
    return False

def par(numero):
    return numero % 2 == 0

# Pedir al usuario que ingrese un número
numero = int(input("Ingresa un número: "))

# Verificar si el número es primo
if primo(numero):
    print(numero, "es primo.")
else:
    print(numero, "no es primo.")

# Verificar si el número pertenece a la secuencia de Fibonacci
if fibonacci(numero):
    print(numero, "pertenece a la secuencia de Fibonacci.")
else:
    print(numero, "no pertenece a la secuencia de Fibonacci.")

# Verificar si el número es par
if par(numero):
    print(numero, "es par.")
else:
    print(numero, "no es par.")


