/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */

using System;

class estuardodev
{
    public static void Main(String[] args)
    {
        Console.Write("Ingresa el texto que deseas traducir a lenguaje hacker:");
        string Entrada;
        Entrada = Console.ReadLine();
        if (Entrada == null || Entrada.Equals(""))
        {
            Console.WriteLine("El texto es nulo o incorrecto.");
        }
        else {
            LenguajeHacker(Entrada);
        }
        
    }

    public static void LenguajeHacker(string Texto)
    {
        Dictionary<string, string> ValoresHacker = new Dictionary<string, string>
        {
            { "A", "4" },
            { "B", "I3" },
            { "C", "[" },
            { "D", ")" },
            { "E", "3" },
            { "F", "|=" },
            { "G", "&" },
            { "H", "#" },
            { "I", "1" },
            { "J", ",_|" },
            { "K", ">|" },
            { "L", "£" },
            { "M", "/\\/\\" },
            { "N", "^/" },
            { "O", "0" },
            { "P", "|*" },
            { "Q", "(_,)" },
            { "R", "I2" },
            { "S", "5" },
            { "T", "7" },
            { "U", "(_)" },
            { "V", "\\/" },
            { "W", "\\_:_/" },
            { "X", "><" },
            { "Y", "j" },
            { "Z", "2" },

            { "a", "@" },
            { "b", "!3" },
            { "c", "©" },
            { "d", "|}" },
            { "e", "ë" },
            { "f", "ph" },
            { "g", "gee" },
            { "h", ":-:" },
            { "i", "3y3" },
            { "j", "._]" },
            { "k", "|c" },
            { "l", "|" },
            { "m", "<\\/>" },
            { "n", "{\\}" },
            { "o", "oh" },
            { "p", "|°" },
            { "q", "0_" },
            { "r", "|-" },
            { "s", "ehs" },
            { "t", "']['" },
            { "u", "L|" },
            { "v", "\\|" },
            { "w", "(n)" },
            { "x", "?" },
            { "y", "`/" },
            { "z", "7_" },

            { "1", "L" },
            { "2", "R" },
            { "3", "E" },
            { "4", "A" },
            { "5", "S" },
            { "6", "G" },
            { "7", "T" },
            { "8", "B" },
            { "9", "q" },
            { "0", "o" },
        };

        foreach (string key in ValoresHacker.Keys)
        {
            Texto = Texto.Replace(key, ValoresHacker[key]);
        }

        Console.WriteLine(Texto);
    }
}
