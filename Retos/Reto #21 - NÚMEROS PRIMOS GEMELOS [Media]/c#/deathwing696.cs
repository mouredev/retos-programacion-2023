/*
 * Crea un programa que encuentre y muestre todos los pares de números primos
 * gemelos en un rango concreto.
 * El programa recibirá el rango máximo como número entero positivo.
 * 
 * - Un par de números primos se considera gemelo si la diferencia entre
 *   ellos es exactamente 2. Por ejemplo (3, 5), (11, 13)
 *
 * - Ejemplo: Rango 14
 *   (3, 5), (5, 7), (11, 13)
 */

using System;
using System.Collections.Generic;


namespace reto21
{
    public class Reto21
    {
        static void Main(string[] args)
        {
            int rango = 14;
            List<int> list = new List<int>();
            List<List<int>> gemelos = new List<List<int>>();

            list = Get_primos_menores_rango(rango);

            for (int i = 0; i < list.Count - 1; i++)
            {
                if (list[i + 1] - list[i] == 2)
                {
                    var par = new List<int>() { list[i], list[i + 1] };
                    gemelos.Add(par);
                }
            }

            Console.WriteLine($"Rango {rango}");

            for (int i = 0; i < gemelos.Count; i++)
            {
                Console.Write($"({gemelos[i][0]}, {gemelos[i][1]})");

                if (i < gemelos.Count - 1)
                    Console.Write(", ");
            }

            Console.ReadKey();
        }

        private static List<int> Get_primos_menores_rango(int rango)
        {
            var primos = new List<int>();

            for (int i = 1; i <= rango; i++)
            {
                bool primo = false;

                for (int j = i - 1; j >= 2; j--)
                {
                    if (i % j == 0)
                    {
                        primo = true;
                        break;
                    }
                }

                if (!primo)
                    primos.Add(i);
            }

            return primos;
        }
    }
}