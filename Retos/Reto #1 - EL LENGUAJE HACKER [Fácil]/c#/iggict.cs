using System;
using System.Collections.Generic;
using System.Linq;

Dictionary<string, string> leetDict = new(StringComparer.OrdinalIgnoreCase) {
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
        { "9", "g" }
    };

do
{
    Console.WriteLine("\nEscribe el texto que quieras traducir a leet:");
    string originalText = Console.ReadLine() ?? "";

    string translatedText = string.Concat(
        originalText.Select(x =>
        {
            string c = x.ToString();
            return leetDict.ContainsKey(c) ? leetDict[c] : c;
        })
    );

    Console.WriteLine(translatedText);

} while (true);