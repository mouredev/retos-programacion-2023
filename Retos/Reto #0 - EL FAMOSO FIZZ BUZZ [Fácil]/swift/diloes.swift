/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */

func resolveChallenge(){
    for index in 1...100{
        if index % 3 == 0 && index % 5 == 0 {
            print("fizzbuzz")
        } else if index % 5 == 0 {
            print("buzz")
        } else if index % 3 == 0 {
            print("fizz")
        } else {
            print(index)
        }
    }
}

resolveChallenge()