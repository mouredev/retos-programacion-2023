'''
Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
    - Múltiplos de 3 por la palabra "fizz".
    - Múltiplos de 5 por la palabra "buzz".
    - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
'''

for e in range(1,101):
    if e % 5 == 0 and e % 3 == 0:
        print("el numero " + f"{e} es fizzbuzz")
    elif e % 5 == 0:
        print("el numero " + f"{e} es buzz")
    elif e % 3 == 0:
        print("el numero " + f"{e} es fizz")
    else:
        print(e)