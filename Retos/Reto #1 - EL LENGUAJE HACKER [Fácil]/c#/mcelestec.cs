using System;
using System.Collections.Generic;

public class Retos2013_Reto2
{

    private static Dictionary<char, string> transformRules = new Dictionary<char, string>
    {
        { 'A', "4" },
        { 'B', "I3" },
        { 'C', "[" },
        { 'D', ")" },
        { 'E', "3" },
        { 'F', "|=" },
        { 'G', "&" },
        { 'H', "#" },
        { 'I', "1" },
        { 'J', ",_|" },
        { 'K', ">|" },
        { 'L', "1" },
        { 'M', "/\\/\\" },
        { 'N', "^/" },
        { 'O', "0" },
        { 'P', "|*" },
        { 'Q', "(_,)" },
        { 'R', "I2" },
        { 'S', "5" },
        { 'T', "7" },
        { 'U', "(_)" },
        { 'V', "\\/" },
        { 'W', "\\/\\/" },
        { 'X', "><" },
        { 'Y', "j" },
        { 'Z', "2" },
        { '1', "L" },
        { '2', "R" },
        { '3', "E" },
        { '4', "A" },
        { '5', "S" },
        { '6', "b" },
        { '7', "T" },
        { '8', "B" },
        { '9', "g" },
        { '0', "o" }
    };

    private static string transformText(string text)
    {
        string newText = string.Empty;

        foreach (char c in text)
        {
            char upperChar = Char.ToUpper(c);
            newText += transformRules.ContainsKey(upperChar) ? transformRules[upperChar] : c.ToString();
        }

        return newText;
    }


    static void Main(string[] args)
    {
        Console.Write("Ingresa el texto a traducir, finaliza presionando enter: ");
        string naturalLanguageText = Console.ReadLine();
        if (naturalLanguageText.Length > 0)
        {
            string hackerLanguageText = transformText(naturalLanguageText);
            System.Console.WriteLine($"Result: {hackerLanguageText}");
        }
        else
        {
            Console.Write("Entrada inválida: el texto no puede ser vacío.");
        }
    }
}
