/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace reto0
{
    internal class Program
    {
        static void Main(string[] args)
        {
            for (int num = 1; num < 101; num++)
            {
                 if (num % 3 == 0 && num % 5 == 0)
                {
                    Console.WriteLine("fizzbuzz\n");
                }
                else if (num % 5 == 0)
                {
                    Console.WriteLine("buzz\n");
                }              
                 else if(num % 3 == 0) 
                {
                    Console.WriteLine("fizz\n");
                }
                 else
                {
                    Console.WriteLine(num + "\n");
                }
            }
        }
    }
}
