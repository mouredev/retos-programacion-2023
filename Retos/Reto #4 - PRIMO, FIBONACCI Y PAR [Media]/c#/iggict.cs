/* Reto #4: PRIMO, FIBONACCI Y PAR
 * 
 * Enunciado:
 * 
 *  Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 *      Ejemplos:
 *          - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 *          - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */

using System;

Console.Write("\nReto #4: PRIMO, FIBONACCI Y PAR");
Console.Write("\n-------------------------------\n");

do
{
    Console.Write("\nIntroduce un número: ");

    int userInt = 0;

    try
    {
        userInt = Int32.Parse(Console.ReadLine() ?? "0");
    }
    catch (Exception)
    {
        Console.WriteLine($"\nERROR: Los parámetros de entrada no son válidos");
        continue;
    }

    Console.WriteLine($"{userInt} " +
        $"{(IsPrime(userInt) ? "es" : "no es")} primo, " +
        $"{(IsFibo(userInt) ? "" : "no es")} fibonacci y " +
        $"{(IsEven(userInt) ? "es par" : "es impar")}");

} while (true);

bool IsEven(int value) => value % 2 == 0;

//bool IsPrime(int value) => !Enumerable.Range(2,value-1).Any(i => value % i == 0 );

static bool IsPrime(int value)
{
    if (value <= 0)
        return false;

    for (int i = 2; i<value; i++)
    {
        if (value % i == 0)
            return false;
    }

    return true;
}

/// <remarks>Un número n es Fibonacci si (5*n 2 + 4) o (5*n 2 – 4) es un cuadrado perfecto</remarks>
/// <see cref="http://en.wikipedia.org/wiki/Fibonacci_number#Recognizing_Fibonacci_numbers"/>
bool IsFibo(int n)
{
    bool isPerfectSquare(int x) => (int)Math.Sqrt(x) * (int)Math.Sqrt(x) == x;

    return isPerfectSquare(5 * n * n + 4) || isPerfectSquare(5 * n * n - 4);
}