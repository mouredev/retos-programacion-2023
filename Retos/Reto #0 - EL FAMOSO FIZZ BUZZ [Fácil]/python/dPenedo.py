"""
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""


def es_multiplo(numero, divisor):
    return numero % divisor == 0

for i in range(1, 101):
    multiplo_de_3 = es_multiplo(i, 3)
    multiplo_de_5 = es_multiplo(i, 5)
    if multiplo_de_3 and multiplo_de_5:
        print("fizzbuzz")
    elif multiplo_de_3:
        print("fizz")
    elif multiplo_de_5:
        print("buzz")
    print(i)
