"""
Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
Múltiplos de 3 por la palabra "fizz".
Múltiplos de 5 por la palabra "buzz".
Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz"
"""

# Usamos el bucle for para recorrer los números desde 1 hasta 100
for i in range(1, 101):
    # Si i es múltiplo de 3 y de 5, imprimimos "fizzbuzz"
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    # Si i es múltiplo de 3, imprimimos "fizz"
    elif i % 3 == 0:
        print("fizz")
    # Si i es múltiplo de 5, imprimimos "buzz"
    elif i % 5 == 0:
        print("buzz")
    # Si i no es múltiplo de 3 ni de 5, imprimimos el número
    else:
        print(i)