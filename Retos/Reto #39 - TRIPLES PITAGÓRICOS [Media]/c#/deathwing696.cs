/*
 * Crea una función que encuentre todos los triples pitagóricos
 * (ternas) menores o iguales a un número dado.
 * - Debes buscar información sobre qué es un triple pitagórico.
 * - La función únicamente recibe el número máximo que puede
 *   aparecer en el triple.
 * - Ejemplo: Los triples menores o iguales a 10 están
 *   formados por (3, 4, 5) y (6, 8, 10).
 */

using System;
using System.Collections.Generic;

namespace deathwing696
{
    public class Deathwing696
    {
        private static bool Es_triple(int a, int b, int c)
        {
            return (Math.Pow(a, 2) + Math.Pow(b, 2) == Math.Pow(c, 2));                
        }

        private static void Calcula_triple_pitagorico(int maximo, List<List<int>> triples)
        {            
            for (int a = 1; a <= maximo; a++)
            {
                for (int b = a + 1; b <= maximo; b++)
                {
                    int c = (int)Math.Sqrt(Math.Pow(a, 2) + Math.Pow(b, 2));

                    if (c <= maximo && Es_triple(a, b, c))
                    {
                        List<int> combinacion = new List<int>() {a, b, c};

                        triples.Add(combinacion);
                    }
                }
            }
        }

        public static void Main(string[] args)
        {
            int maximo;

            Console.Write("Introduce el número máximo del triple pitagórico:");

            if (Int32.TryParse(Console.ReadLine(), out maximo))
            {
                List<List<int>> triples;

                triples = new List<List<int>>();
                Calcula_triple_pitagorico(maximo, triples);

                Console.WriteLine($"Los triples menores o iguales a {maximo} están formados por:");

                foreach (var combinacion in triples)
                    Console.WriteLine($"({String.Join(", ", combinacion)})");
            }
            else
            {
                Console.WriteLine("Lo que has introducido por teclado no es un número...Fin del programa");
            }

            Console.ReadKey();
        }
    }
}