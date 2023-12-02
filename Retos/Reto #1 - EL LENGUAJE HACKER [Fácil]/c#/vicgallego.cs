/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace reto1
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Escribe un texto\n");
            string text = Console.ReadLine();
            string mayus = text.ToUpper();

            Console.WriteLine("Tu texto en lenguaje leet seria:\n");
            string textremplace = mayus.Replace("A", "4").Replace("B", "I3").Replace("C", "[").Replace("D", ")").Replace("E", "3").Replace("F", "|=").Replace("G", "&").Replace("H", "#")
                .Replace("I", "|").Replace("J", ",_|").Replace("K", ">|").Replace("L", "1").Replace("M", "|Y|").Replace("N", "/\\/").Replace("O", "0").Replace("P", "|>").Replace("Q", "0,").Replace("R", "|2")
                .Replace("S", "5").Replace("T", "7").Replace("U", "[_]").Replace("V", "\\/").Replace("W", "\v/").Replace("X", "}{").Replace("Y", "´/").Replace("Z", "2").Replace("1", "L").Replace("2", "R")
                .Replace("3", "3").Replace("4", "A").Replace("5", "S").Replace("6", "b").Replace("7", "T").Replace("8", "B").Replace("9", "g").Replace("0", "()");
            Console.WriteLine(textremplace);
        }
    }
}
