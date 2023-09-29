/*
 * Dada una URL con parámetros, crea una función que obtenga sus valores.
 * No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
 *
 * Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
 * los parámetros serían ["2023", "0"]
 */

using System;
using System.Collections.Generic;
using System.Text.RegularExpressions;

namespace deathwing696
{
    public class Deathwing696
    {
        private static void Extrae_parametros(string url, List<string> parametros)
        {
            string[] partes;

            partes = url.Split('?');

            if (partes.Length > 1)
            {
                partes = partes[1].Split('&');

                foreach (var item in partes)
                {
                    string[] pares = item.Split('=');

                    parametros.Add(pares[1]);
                }
            }
        }

        private static void Comprueba_url_correcta_y_ejecuta(string url)
        {
            string pattern = @"http[s]*:\/\/.*\?.*";

            if (Regex.IsMatch(url, pattern))
            {
                List<string> parametros = new List<string>();

                Extrae_parametros(url, parametros);

                Imprimir_por_pantalla(parametros);
            }
        }

        private static void Imprimir_por_pantalla(List<string> lista)
        {
            Console.Write("[");

            foreach (var param in lista)
            {
                Console.Write("\"{0}\"", param);

                if (!param.Equals(lista[lista.Count - 1]))
                {
                    Console.Write(", ");
                }
            }

            Console.WriteLine("]");
        }

        public static void Main(string[] args)
        {
            string url = "https://retosdeprogramacion.com?year=2023&challenge=0", url2 = "http://example.com? product=1234 &utm_source=google";

            Comprueba_url_correcta_y_ejecuta(url);

            Comprueba_url_correcta_y_ejecuta(url2);

            Console.ReadLine();
        }
    }
}
