/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */

public class Leet
{
    public static void Main(string[] args)
    {
        Traductor("Este es un texto a traducir");
    }

    private static void Traductor(string text)
    {
        var textLeet = text.ToLower()
            .Replace("a", "Д")
            .Replace("b", "ß")
            .Replace("c", "<")
            .Replace("d", "cl")
            .Replace("e", "[-")
            .Replace("f", "ph")
            .Replace("g", "gee")
            .Replace("h", "}{")
            .Replace("i", "eye")
            .Replace("j", "._]")
            .Replace("k", "|<")
            .Replace("l", "£")
            .Replace("m", "/V\\")
            .Replace("n", "И")
            .Replace("ñ", "^/")
            .Replace("o", "p")
            .Replace("p", "|o")
            .Replace("q", "(_,)")
            .Replace("r", "I2")
            .Replace("s", "ehs")
            .Replace("t", "†")
            .Replace("u", "บ")
            .Replace("v", "|/")
            .Replace("w", "Щ")
            .Replace("x", "ecks")
            .Replace("y", "Ч")
            .Replace("z", "7_")
            .Replace("0", "o")
            .Replace("1", "L")
            .Replace("2", "R")
            .Replace("3", "E")
            .Replace("4", "A")
            .Replace("5", "S")
            .Replace("6", "b")
            .Replace("7", "T")
            .Replace("8", "B")
            .Replace("9", "g");
        Console.WriteLine(textLeet);
    }
}
