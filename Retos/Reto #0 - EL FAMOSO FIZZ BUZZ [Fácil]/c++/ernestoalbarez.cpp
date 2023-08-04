#include <iostream>
#include <string>

/*
Reto #0: EL FAMOSO "FIZZ BUZZ"


 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
*/

int main()
{
    std::string fizz = "Fizz";
    std::string buzz = "Buzz";
    std::string fizzBuzz = "FizzBuzz";

    for (int i = 1; i <= 100; i++) {
        bool divisibleBy3 = i % 3 == 0;
        bool divisibleBy5 = i % 5 == 0;

        if (divisibleBy3 && divisibleBy5) {
            std::cout << fizzBuzz << std::endl;
        }
        else if (divisibleBy3) {
            std::cout << fizz << std::endl;
        }
        else if (divisibleBy5) {
            std::cout << buzz << std::endl;
        }
        else {
            std::cout << i << std::endl;
        }
    }

    return 0;
}
