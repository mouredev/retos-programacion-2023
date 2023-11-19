/*
 * Crea un programa que sea capaz de solicitarte un número y se
 * encargue de imprimir su tabla de multiplicar entre el 1 y el 10.
 * - Debe visualizarse qué operación se realiza y su resultado.
 *   Ej: 1 x 1 = 1
 *       1 x 2 = 2
 *       1 x 3 = 3
 *       ... 
 */

using System;

namespace deathwing696
{
    public class Deathwing696
    {
        static void Main(string[] args)
        {
            int numero;

            Console.Write("Introduce un número para ver su tabla de multiplicar:");

            if (Int32.TryParse(Console.ReadLine(), out numero))
            {
                for (int i = 1; i <= 10; i++)
                    Console.WriteLine($"{numero} x {i} = {i * numero}");
            }
            else
            {
                Console.WriteLine("Lo que has introducido no es un número...fin del programa");
            }

            Console.ReadKey();
        }
    }
}