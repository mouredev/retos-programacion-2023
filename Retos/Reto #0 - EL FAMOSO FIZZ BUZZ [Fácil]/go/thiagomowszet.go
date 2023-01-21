package main

import("fmt")



/*

Reto #0: El famoso "FizzBuzz" - Thiago Mowszet

 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".

*/


func main() {

    for i := 1; i <= 100; i++ {
        if i % 3 == 0  && i % 5 == 0 {
            fmt.Printf("FizzBuzz\n")
        }else if i % 3 == 0 {
            fmt.Printf("Fizz\n")
        }else if i % 5 == 0 {
            fmt.Printf("Buzz\n")
        }else {
            fmt.Println(i)
        }
    }

}
