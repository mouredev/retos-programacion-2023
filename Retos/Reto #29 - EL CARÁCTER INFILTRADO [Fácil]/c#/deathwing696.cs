/*
 * Crea una función que reciba dos cadenas de texto casi iguales,
 * a excepción de uno o varios caracteres. 
 * La función debe encontrarlos y retornarlos en formato lista/array.
 * - Ambas cadenas de texto deben ser iguales en longitud.
 * - Las cadenas de texto son iguales elemento a elemento.
 * - No se pueden utilizar operaciones propias del lenguaje
 *   que lo resuelvan directamente.
 * 
 * Ejemplos:
 * - Me llamo mouredev / Me llemo mouredov -> ["e", "o"]
 * - Me llamo.Brais Moure / Me llamo brais moure -> [" ", "b", "m"]
 */

using System;
using System.Collections.Generic;

namespace reto29
{
    public class Reto29
    {
        static void Main(string[] args)
        {
            string cadena1 = "Me llamo mouredev", cadena2 = "Me llemo mouredov";
            string cadena3 = "Me llamo.Brais Moure", cadena4 = "Me llamo brais moure";
            List<char> diferencias = new List<char>();

            diferencias = Encuentra_diferencias(cadena1, cadena2);

            if (diferencias.Count > 0)
            {
                Console.Write($"{cadena1} / {cadena2} -> ");
                Dibuja_por_pantalla(diferencias);
                Console.WriteLine();
            }

            diferencias.Clear();
            diferencias = Encuentra_diferencias(cadena3, cadena4);

            if (diferencias.Count > 0)
            {
                Console.Write($"{cadena3} / {cadena4} -> ");
                Dibuja_por_pantalla(diferencias);
                Console.WriteLine();
            }

            Console.ReadKey();
        }

        private static List<char> Encuentra_diferencias(string cadena1, string cadena2)
        {
            List<char> diferencias = new List<char>();

            if (cadena1.Length == cadena2.Length)
            {
                for (int i = 0; i < cadena1.Length; i++)
                {
                    if (cadena1[i] != cadena2[i])
                        diferencias.Add(cadena2[i]);
                }
            }

            return diferencias;
        }

        private static void Dibuja_por_pantalla(List<char> diferencias) 
        {
            Console.Write("[");

            for (int i = 0; i < diferencias.Count; i++)
            {
                Console.Write($"\"{diferencias[i]}\"");

                if (i < diferencias.Count - 1)
                    Console.Write(", "); 
            }

            Console.Write("]");
        }
    }
}