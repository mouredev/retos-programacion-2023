# ```

#  * Escribe un programa que muestre por consola (con un print) los
#  * números de 1 a 100 (ambos incluidos y con un salto de línea entre
#  * cada impresión), sustituyendo los siguientes:
#  * - Múltiplos de 3 por la palabra "fizz".
#  * - Múltiplos de 5 por la palabra "buzz".
#  * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
#  */
# ```

# Solucion:

# for numero in range(101):
#     if numero % 3 == 0 and numero % 5 == 0:
#         print("fizzbuzz \n")
#     elif numero % 3 == 0:
#         print("fizz \n")
#     elif numero % 5 == 0:
#         print("buzz \n")

import numpy as np

def print_numero(numero: int) -> None:
    if numero % 3 == 0 and numero % 5 == 0:
        print("fizzbuzz \n")
    elif numero % 3 == 0:
        print("fizz \n")
    elif numero % 5 == 0:
        print("buzz \n")
    else:
        print(f"{numero} \n")

np.vectorize(print_numero)(np.arange(101))