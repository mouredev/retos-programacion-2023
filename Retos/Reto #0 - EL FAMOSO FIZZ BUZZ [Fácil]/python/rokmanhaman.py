"""
Reto #0: EL FAMOSO "FIZZ BUZZ"
/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */
 """

for x in range(1,101,1):
    y = ""
    if x % 3 == 0:
        y = "fizz"
        if x % 5 == 0:
            y = y + "buzz"
    elif x % 5 == 0:
        y = y + "buzz"
    else:
        y = x
    print(y)
         



