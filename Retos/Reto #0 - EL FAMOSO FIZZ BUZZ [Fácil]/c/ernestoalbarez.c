#include <stdio.h>
#include <stdbool.h>

/*
Reto #0: EL FAMOSO "FIZZ BUZZ"


 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
*/

void main() {
    const char* fizz = "Fizz";
    const char* buzz = "Buzz";
    const char* fizzBuzz = "FizzBuzz";
    
    for (int i=1; i<=100; i++) {
        bool divisibleBy3 = i%3==0;
        bool divisibleBy5 = i%5==0;
        
        if (divisibleBy3 && divisibleBy5) {
            puts(fizzBuzz);
        } else if (divisibleBy3) {
            puts(fizz);
        } else if (divisibleBy5) {
            puts(buzz);
        } else {
            printf("%d\n", i);
        }
    }
}
