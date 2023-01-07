/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */

using System;

namespace MoureReto1
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine($"Please, write a text:");
            string text =Console.ReadLine();
            TransformText(text.ToLower());

            Console.WriteLine($"End program!");
            Console.ReadLine();
        }

        /// <summary>
        /// foreach every char and try to transform it!
        /// </summary>
        /// <param name="originalText"></param>
        public static void TransformText(string originalText)
        {
            string returnValue = string.Empty;
            foreach (var chart in originalText)
            {
                returnValue += Change(chart);
            }
            Console.WriteLine($"The new text is: {returnValue}");
        }

        /// <summary>
        /// Conversor
        /// </summary>
        /// <param name="ch"></param>
        /// <returns></returns>
        public static string Change(Char ch)
        {
            if (ch == 'a')
                return "4";
            if (ch == 'b')
                return "|3";
            if (ch == 'c')
                return "[";
            if (ch == 'd')
                return ")";
            if (ch == 'e')
                return "3";
            if (ch == 'f')
                return "|=";
            if (ch == 'g')
                return "&";
            if (ch == 'h')
                return "#";
            if (ch == 'i')
                return "1";
            if (ch == 'j')
                return "_|";
            if (ch == 'k')
                return ">|";
            if (ch == 'l')
                return "1";
            if (ch == 'm')
                return @"/\/\";
            if (ch == 'n')
                return "^/";
            if (ch == 'o')
                return "0";
            if (ch == 'p')
                return "|*";
            if (ch == 'q')
                return "(_,)";
            if (ch == 'r')
                return "|2";
            if (ch == 's')
                return "5";
            if (ch == 't')
                return "7";
            if (ch == 'u')
                return "(_)";
            if (ch == 'v')
                return @"\/";
            if (ch == 'w')
                return @"\/\/";
            if (ch == 'x')
                return "><";
            if (ch == 'y')
                return "j";
            if (ch == 'z')
                return "2";
            return ch.ToString();
        }      
    }
}
