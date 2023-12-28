# ```
# /*
# * Escribe un programa que muestre por consola(con un print) los
# * números de 1 a 100 (ambos incluidos y con un salto de línea entre
#                       * cada impresión), sustituyendo los siguientes:
#  * - Múltiplos de 3 por la palabra "fizz".
#  * - Múltiplos de 5 por la palabra "buzz".
#  * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
#  */
# ```

def bizz_buzz(range_value: int, reference_one: int, reference_two: int):
    for i in range(0, range_value + 1):
        if i % reference_one == 0 and i % reference_two == 0:
            print("fizzbuzz")
        elif i % reference_one == 0:
            print("fizz")
        elif i % reference_two == 0:
            print("buzz")
        else:
            print(i)


bizz_buzz(100, 3, 5)
