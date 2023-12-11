using System;
using System.Collections.Generic;
/*
 * La última semana de 2021 comenzamos la actividad de retos de programación,
 * con la intención de resolver un ejercicio cada semana para mejorar
 * nuestra lógica... ¡Hemos llegado al EJERCICIO 100! Gracias 🙌
 *
 * Crea un programa que calcule los puntos de una palabra.
 * - Cada letra tiene un valor asignado. Por ejemplo, en el abecedario
 *   español de 27 letras, la A vale 1 y la Z 27.
 * - El programa muestra el valor de los puntos de cada palabra introducida.
 * - El programa finaliza si logras introducir una palabra de 100 puntos.
 * - Puedes usar la terminal para interactuar con el usuario y solicitarle
 *   cada palabra.
 */
namespace ConsoleApp1
{
    internal class Program
    {
        static void Main(string[] args)
        {
            char[] abecedario = {
                    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                    'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
                };
            int puntos, intentos = 0;
            Console.WriteLine("¡Bienvenido al programa de la palabra de los 100 puntos!");
            do
            {
                puntos = 0;
                intentos++;
                Console.Write("Introduce una palabra para calcular sus puntos: ");
                string palabra = Console.ReadLine();
                char[] letras = (palabra).ToLower().ToCharArray();
                List<char> resultado = new List<char>(letras);

                foreach (var letra in resultado)
                {
                    int index = Array.IndexOf(abecedario, letra);
                    if(index == -1) Console.WriteLine($"La letra {letra} no está en el abecedario.");
                    else
                    puntos += index + 1;
                }

                if (puntos < 100 | puntos > 100)
                {
                    Console.WriteLine($"La palabra {palabra} tiene {puntos} puntos.");
                    Console.WriteLine($"Llevas {intentos} intentos.");
                    Console.WriteLine("Pulsa cualquier tecla para continuar...");
                    Console.ReadKey();
                    Console.Clear();
                }
                else
                {
                    Console.WriteLine($"¡Has ganado! ¡Felicidades! ¡La palabra {palabra} tiene {puntos} puntos! ");
                    Console.WriteLine($"Has acabado con {intentos} intentos.");
                    Console.WriteLine("¡Gracias por jugar!");
                    Console.WriteLine("Pulsa cualquier tecla para salir...");
                    Console.ReadKey();
                    Console.Clear();
                }




            } while (puntos != 100);

        }
    }
}
