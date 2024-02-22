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

using System;
using System.Globalization;
using System.Text;
using System.Web;

namespace reto_47
{
    public class Reto47
    {
        static void Main(string[] args)
        {
            string palabra, cadena;
            int puntos = 0;

            do
            {
                Console.Write("Introduce una palabra que tenga una puntuación igual o mayor a 100 puntos:");
                cadena = Console.ReadLine();
                palabra = Obtener_primera_palabra(cadena);
                puntos = Calcula_puntos(palabra);
                Console.WriteLine($"La palabra {palabra} tiene {puntos} puntos");
            } while (puntos < 100);

            Console.WriteLine("Enhorabuena! Has conseguido una palabra de 100 puntos! Hasta la próxima!");

            Console.ReadKey();
        }

        static private int Calcula_puntos(string palabra)
        {
            string palabra_mayusculas = palabra.ToUpper();
            int codigo_ascci_a = (int)'A', puntos = 0;

            palabra_mayusculas = Quitar_acentos(palabra_mayusculas);

            foreach (var letra in palabra_mayusculas)
            {
                if (Char.IsLetter(letra))
                {
                    puntos += (int)letra - codigo_ascci_a + 1;
                }
                else
                {
                    puntos += 0;
                }
            }

            return puntos;
        }

        static private string Quitar_acentos(string palabra)
        {
            string palabra_normalizada = palabra.Normalize(NormalizationForm.FormD);
            StringBuilder salida = new StringBuilder();

            foreach (char c in palabra_normalizada)
            {
                if (CharUnicodeInfo.GetUnicodeCategory(c) != UnicodeCategory.NonSpacingMark)
                {
                    salida.Append(c);
                }
            }

            return salida.ToString().Normalize(NormalizationForm.FormC);
        }

        static private string Obtener_primera_palabra(string cadena)
        {
            string[] palabras;
            string primera_palabra;

            palabras = cadena.Split(new[] { ' ' }, StringSplitOptions.RemoveEmptyEntries);

            primera_palabra = palabras.Length > 0 ? palabras[0] : String.Empty;

            return primera_palabra;
        }
    }
}