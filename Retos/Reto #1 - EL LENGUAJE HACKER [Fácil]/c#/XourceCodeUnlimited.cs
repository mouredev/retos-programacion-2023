using System;
using System.Collections.Generic;

namespace RetrosProgramacionSemanales
{
    internal class TecAlvarez
    {
        /*
         * Escribe un programa que reciba un texto y transforme lenguaje natural a
         * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
         *  se caracteriza por sustituir caracteres alfanuméricos.
         * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
         *   con el alfabeto y los números en "leet".
         *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
         */

        static void Main(string[] args)
        {
            Dictionary<char, string> dctTraduccion = new Dictionary<char, string>();
            dctTraduccion.Add('A', "4");
            dctTraduccion.Add('B', "I3");
            dctTraduccion.Add('C', "[");
            dctTraduccion.Add('D', ")");
            dctTraduccion.Add('E', "3");
            dctTraduccion.Add('F', "|=");
            dctTraduccion.Add('G', "&");
            dctTraduccion.Add('H', "#");
            dctTraduccion.Add('I', "1");
            dctTraduccion.Add('J', ",_|");
            dctTraduccion.Add('K', ">|");
            dctTraduccion.Add('L', "1");
            dctTraduccion.Add('M', "/\\/\\");
            dctTraduccion.Add('N', "^/");
            dctTraduccion.Add('O', "0");
            dctTraduccion.Add('P', "|*");
            dctTraduccion.Add('Q', "(_,)");
            dctTraduccion.Add('R', "I2");
            dctTraduccion.Add('S', "5");
            dctTraduccion.Add('T', "7");
            dctTraduccion.Add('U', "(_)");
            dctTraduccion.Add('V', "\\/");
            dctTraduccion.Add('W', "\\/\\/");
            dctTraduccion.Add('X', "><");
            dctTraduccion.Add('Y', "j");
            dctTraduccion.Add('Z', "2");

            var strText = Console.ReadLine();
            if (strText != null && strText != "")
            {
                strText = strText.ToUpper();
                foreach (var item in strText.ToCharArray())
                {
                    if (dctTraduccion.ContainsKey(item))
                    {
                        strText = strText.Replace(item.ToString(), dctTraduccion[item]);
                    }
                }
                Console.WriteLine(strText);
            }
        }
    }
}
