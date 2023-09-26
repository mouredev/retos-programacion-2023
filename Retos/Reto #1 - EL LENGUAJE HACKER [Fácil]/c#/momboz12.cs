using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Retos
{

    /*
     * Escribe un programa que reciba un texto y transforme lenguaje natural a
     * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
     *  se caracteriza por sustituir caracteres alfanuméricos.
     * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
     *   con el alfabeto y los números en "leet".
     *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
     */

    internal class Reto_01
    {
        static readonly Dictionary<string, string> leetDictionary = new Dictionary<string, string>()
        {
            { "a", "4" },
            { "b", "I3" },
            { "c", "[" },
            { "d", ")" },
            { "e", "3" },
            { "f", "|=" },
            { "g", "&" },
            { "h", "#" },
            { "i", "1" },
            { "j", ",_|" },
            { "k", ">|" },
            { "l", "1" },
            { "m", @"/\/\" },
            { "n", "^/" },
            { "o", "0" },
            { "p", "|*" },
            { "q", "(_,)" },
            { "r", "I2" },
            { "s", "5" },
            { "t", "7" },
            { "u", "(_)" },
            { "v", @"\/" },
            { "w", @"\/\/" },
            { "x", "><" },
            { "y", "j" },
            { "z", "2" },
            { "0", "o" },
            { "1", "L" },
            { "2", "R" },
            { "3", "E" },
            { "4", "A" },
            { "5", "S" },
            { "6", "b" },
            { "7", "T" },
            { "8", "B" },
            { "9", "g" },
        };

        /// <summary>
        /// Reemplaza los caracteres originales por los del diccionario leet,
        /// en caso de no encontrar el caracter deja el original
        /// </summary>
        /// <param name="strText"></param>
        /// <returns></returns>
        static string hackerText(string strText)
        {
            string strTranslate = "";
            foreach (char inChar in strText)
                if (leetDictionary.TryGetValue(inChar.ToString(), out string newChar))
                    strTranslate += newChar;
                else
                    strTranslate += inChar;
            return strTranslate;
        }

        static void Main(string[] args)
        {
            Console.Write("Ingrese el texto que desea traducir: ");
            string strInputText = Console.ReadLine() ?? "";
            string strOutputText = hackerText(strInputText.ToLower());
            Console.WriteLine($"Texto traducido: {strOutputText}");
            Console.ReadKey();
        }

        
    }
}
