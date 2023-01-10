/*
 *              Reto #0: EL FAMOSO "FIZZ BUZZ"
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
*/

#include <iostream>
#include <array>

struct intToFizzBuzz
{
    int i_{};
    std::string out{};  
};

static constexpr std::array data
{
      intToFizzBuzz{15, "FizzBuzz"}
    , intToFizzBuzz{ 3, "Fizz"}
    , intToFizzBuzz{ 5, "Buzz"}
};

void fizzBuzz(int const max)
{
    for(int i{1}; i <= max; ++i)
    {
        bool printed { false };
        for(auto const& [ num, out ] : data)
        {
            if( ( i % num ) == 0)
            {
                std::cout << out << '\n';
                printed = true;
                break;
            }
        }
        if(!printed) { std::cout << i << '\n'; }
    }
}

int main()
{
    fizzBuzz(100);

    return 0;
}