'''
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 '''

def fizzbuzz(num):
  for i in range(1, num+1):
    threeMultiple = i % 3 == 0
    fiveMultiple = i % 5 == 0

    if (threeMultiple and fiveMultiple): message = "fizzbuzz"
    elif (threeMultiple): message = "fizz"
    elif (fiveMultiple): message = "buzz"
    else: message = i

    print(message)


fizzbuzz(100)
  