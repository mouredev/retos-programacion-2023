/*
 *	¡El nuevo "The Legend of Zelda: Tears of the Kingdom" ya está disponible! 
 *
 * Crea un programa que dibuje una Trifuerza de "Zelda"
 * formada por asteriscos.
 * - Debes indicarle el número de filas de los triángulos con un entero positivo (n).
 * - Cada triángulo calculará su fila mayor utilizando la fórmula 2n-1.
 *
 * Ejemplo: Trifuerza 2
 * 
 *    *
 *   ***
 *  *   *
 * *** ***
 *
 */

using System;

namespace deathwing696
{
    public class Deathwing696
    {
        static void Main(string[] args)
        {
            Console.Write("Introduce el número de pisos que tendrán los triángulos de la trifuerza:");

            int pisos;

            if (Int32.TryParse(Console.ReadLine(), out pisos))
            {
                DibujarTrifuerza(pisos);
            }
            else
            {
                Console.WriteLine("Lo introducido no es un número...fin del programa");
            }

            Console.ReadKey();
        }

        private static void DibujarTrifuerza(int pisos)
        {
            Dibuja_triangulo_arriba(pisos);
            Dibuja_triangulos_abajo(pisos);
            
        }        

        private static void Dibuja_triangulo_arriba(int pisos)
        {
            for (int i = 0; i < pisos; i++)
            {
                for (int j = 0; j < (2 * pisos - 1) - i; j++)
                {
                    Console.Write(' ');
                }

                for (int j = 0; j < (2 * i) + 1; j++)
                {
                    Console.Write('*');
                }

                Console.WriteLine();
            }
        }

        private static void Dibuja_triangulos_abajo(int pisos)
        {
            for (int i = 0; i < pisos; i++)
            {
                for (int j = 0; j < pisos - 1 - i; j++)
                {
                    Console.Write(' ');
                }

                for (int j = 0; j < (2 * i) + 1; j++)
                {
                    Console.Write('*');
                }

                for (int j = 0; j < 2 * pisos - 1 - 2 * i; j++)
                {
                    Console.Write(' ');
                }

                for (int j = 0; j < (2 * i) + 1; j++)
                {
                    Console.Write('*');
                }

                Console.WriteLine();
            }
        }
    }
}