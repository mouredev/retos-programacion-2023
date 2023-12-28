using System;

/*
Reto #0: EL FAMOSO "FIZZ BUZZ"


 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
*/


class Program
{
    static void Main()
    {
        string fizz = "Fizz";
        string buzz = "Buzz";
        string fizzBuzz = "FizzBuzz";

        for (int i=1; i<=100; i++)
        {
            bool divisibleBy3 = i%3==0;
            bool divisibleBy5 = i%5==0;

            if (divisibleBy3 && divisibleBy5) {
                Console.WriteLine(fizzBuzz);
            }
            else if (divisibleBy3) {
                Console.WriteLine(fizz);
            }
            else if (divisibleBy5) {
                Console.WriteLine(buzz);
            }
            else {
                Console.WriteLine(i);
            }
        }
    }
}
