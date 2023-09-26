"""
    Escribe un programa que muestre por consola (con un print) los
    números de 1 a 100 (ambos incluidos y con un salto de línea entre
    cada impresión), sustituyendo los siguientes:
     - Múltiplos de 3 por la palabra "fizz".
     - Múltiplos de 5 por la palabra "buzz".
     - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""
def fizz_buzz():
    cad = ""
    for i in range(1, 101, 1):
        if i % 3 == 0 and i % 5 == 0:
            cad += "fizzbuzz\n"
        elif i % 3 == 0:
            cad += "fizz\n"
        elif i % 5 == 0:
            cad += "buzz\n"
        else:
            cad += str(i) + "\n"
    print(cad)

fizz_buzz()