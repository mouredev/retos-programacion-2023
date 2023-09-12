""" 
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""


def show_numbers(limitnumber):
    for i in range(limitnumber):
        if (i + 1) % 5 == 0 and (i + 1) % 3 == 0:
            print("fizzbuzz")
        elif (i + 1) % 3 == 0:
            print("fizz")
        elif (i + 1) % 5 == 0:
            print("buzz")
        else:
            print(i + 1)
        print("\n")


def main():
    show_numbers(100)


main()
