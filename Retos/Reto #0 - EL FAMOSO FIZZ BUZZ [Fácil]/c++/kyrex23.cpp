/*
 * # Reto #0: EL FAMOSO "FIZZ BUZZ"
 * #### Dificultad: Fácil | Publicación: 26/12/22 | Corrección: 02/01/23
 *
 * ## Enunciado
 *
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 *
 * Author: kyrex23
 * Date:   22/01/2023
 */

#include <iostream>
#include <string>

const int MIN_VALUE = 1;
const int MAX_VALUE = 100;

const int FIZZ_DIVISOR = 3;
const int BUZZ_DIVISOR = 5;


int main(int argc, char *argv[]) {
    for(int i = MIN_VALUE; i <= MAX_VALUE; ++i) {
        std::string output = "";

        if(i % FIZZ_DIVISOR == 0) output += "fizz";
        if(i % BUZZ_DIVISOR == 0) output += "buzz";
        if(output == "") output += std::to_string(i);

        std::cout << output << std::endl;
    }
}
