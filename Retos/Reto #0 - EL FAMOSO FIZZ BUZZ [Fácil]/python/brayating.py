##  Pregunta  problema##
# Escribe  un programa que imprima por consola los numeros del 1 hasta 100 con un salto de linea entre cada impresion y ademas con las  sigientes derivaciones
# Múltiplos de  3 por la  palabra " fizz"
# Múltiplos de 5 por la palabra "buzz"
# Múltiplos de 3 y 5 ala vez con la palabra "fizzbuzz".


def fizzbuzz():
    for i in range(1, 101):
        # Definimos el rango de  1 hasta  100 por medioo de  este ciiclo for
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
            # definimos  lso multiplos 3
        elif i % 3 == 0:
            print("fizz")
            # definimos  los  multiplos de  5
        elif i % 5 == 0:
            print("buzz")

        else:
            print(i)


fizzbuzz()
