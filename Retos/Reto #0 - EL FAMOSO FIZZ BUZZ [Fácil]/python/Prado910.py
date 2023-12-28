# -----------------------------------------------------------------
# Escribe un programa que muestre por consola (con un print) los
# números de 1 a 100 (ambos incluidos y con un salto de línea entre
# cada impresión), sustituyendo los siguientes:
# - Múltiplos de 3 por la palabra "fizz".
# - Múltiplos de 5 por la palabra "buzz".
# - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
# -----------------------------------------------------------------

for i in range(1, 101):
    if i % 15 == 0:
        i = "fizzbuzz"
    elif i % 5 == 0:
        i = "buzz"
    elif i % 3 == 0:
        i = "fizz"
    
    print("-", i)
