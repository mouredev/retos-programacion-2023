/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".

    .NET SDK 6 - dotnet run
 */

string FizzBuzz(int number)
{
    return number % 3 == 0 && number % 5 == 0 ? "fizzbuzz" : number % 3 == 0 ? "fizz" : number % 5 == 0 ? "buzz" : number.ToString();
}

for (int number = 1; number <= 100; number++)
{
    Console.WriteLine(FizzBuzz(number));
}

