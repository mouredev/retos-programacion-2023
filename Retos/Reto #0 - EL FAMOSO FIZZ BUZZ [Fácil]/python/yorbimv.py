"""
/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */
"""
# Funcion fizbuzz
def fizz_buzz():
    for num in range(1,101):      # Imprime del 1 al 100
        if num !=0 and num % 3 == 0 and num % 5 == 0: 
            print("fizzbuzz")
        elif num % 3 == 0:  # Si el resto de num/3 =0
            print("fizz")
        elif num % 5 == 0:  # Si el resto de num/5 =0
            print("buzz")
        else:
            print(num)

# LLama a la función fizz_buzz
fizz_buzz()
