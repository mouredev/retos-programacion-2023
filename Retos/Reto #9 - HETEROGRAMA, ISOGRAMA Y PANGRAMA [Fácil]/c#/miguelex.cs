using System;
using System.Collections.Generic;
using System.Linq;

class miguelex
{
    static string RemoveDiacritics(string cadena)
    {
        Dictionary<char, char> diacriticos = new Dictionary<char, char>
        {
            {'á', 'a'}, {'é', 'e'}, {'í', 'i'}, {'ó', 'o'}, {'ú', 'u'},
            {'à', 'a'}, {'è', 'e'}, {'ì', 'i'}, {'ò', 'o'}, {'ù', 'u'},
            {'ä', 'a'}, {'ë', 'e'}, {'ï', 'i'}, {'ö', 'o'}, {'ü', 'u'},
            {'â', 'a'}, {'ê', 'e'}, {'î', 'i'}, {'ô', 'o'}, {'û', 'u'},
            {'ã', 'a'}, {'ñ', 'n'}, {'õ', 'o'},
            {'ç', 'c'}
        };

        string cadena_sin_diacriticos = "";
        foreach (char caracter in cadena)
        {
            if (diacriticos.ContainsKey(caracter))
            {
                cadena_sin_diacriticos += diacriticos[caracter];
            }
            else
            {
                cadena_sin_diacriticos += caracter;
            }
        }

        return cadena_sin_diacriticos;
    }

    static bool IsHeterogram(string cadena)
    {
        return cadena.Length == cadena.Distinct().Count() && cadena == RemoveDiacritics(cadena);
    }

    static bool IsIsogram(string cadena)
    {
        HashSet<char> letras_vistas = new HashSet<char>();
        foreach (char letra in RemoveDiacritics(cadena))
        {
            if (letras_vistas.Contains(letra))
            {
                return false;
            }
            letras_vistas.Add(letra);
        }
        return true;
    }

    static bool IsPangram(string cadena)
    {
        HashSet<char> alfabeto = new HashSet<char>("abcdefghijklmnopqrstuvwxyz");
        string cadena_sin_diacriticos = RemoveDiacritics(cadena.ToLower());
        foreach (char letra in cadena_sin_diacriticos)
        {
            if (alfabeto.Contains(letra))
            {
                alfabeto.Remove(letra);
            }
            if (!alfabeto.Any())
            {
                return true;
            }
        }
        return false;
    }

    static void Main(string[] args)
    {
        string string1 = "murcielago";
        string string2 = "esdrújula";
        string string3 = "El veloz murciélago hindú comía feliz cardillo y kiwi. La cigüeña tocaba el saxofón detrás del palenque de paja";

        Console.WriteLine(IsHeterogram(string1));  // True
        Console.WriteLine(IsHeterogram(string2));  // False
        Console.WriteLine(IsIsogram(string1));  // True
        Console.WriteLine(IsIsogram(string2));  // False
        Console.WriteLine(IsPangram(string3));  // True
    }

}