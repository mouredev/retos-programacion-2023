/*
 * Crea una función que calcule el número de la columna de una hoja de Excel
 * teniendo en cuenta su nombre.
 * - Las columnas se designan por letras de la "A" a la "Z" de forma infinita.
 * - Ejemplos: A = 1, Z = 26, AA = 27, CA = 79.
 */

using System;
using System.Linq;
using System.Text.RegularExpressions;

namespace reto32
{
    public class Reto32
    {
        static void Main(string[] args)
        {
            string columna1 = "A", columna2 = "Z", columna3 = "AA", columna4 = "CA", columna5 = "ABC";

            Console.WriteLine($"{columna1} = {Calcula_columna_excel(columna1)}");
            Console.WriteLine($"{columna2} = {Calcula_columna_excel(columna2)}");
            Console.WriteLine($"{columna3} = {Calcula_columna_excel(columna3)}");
            Console.WriteLine($"{columna4} = {Calcula_columna_excel(columna4)}");
            Console.WriteLine($"{columna5} = {Calcula_columna_excel(columna5)}");

            Console.ReadKey();
        }

        private static int Calcula_columna_excel(string columna)
        {
            int retorno = 0, posicion = 0, i = 0;
            string pattern = @"[A-Z]+";
            Regex regex = new Regex(pattern);
            string reverse_columna = new string(columna.Reverse().ToArray());

            if (regex.IsMatch(columna))
            {
                foreach (var letra in reverse_columna)
                {
                    posicion = (((int)letra - (int)'A') % 26) + 1;
                    retorno += posicion * Convert.ToInt32(Math.Pow(26, i));
                    i++;
                }
            }

            return retorno;
        }
    }
}