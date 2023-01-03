/*
* Escribe un programa que reciba un texto y transforme lenguaje natural a
* "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
*  se caracteriza por sustituir caracteres alfanuméricos.
* - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
*   con el alfabeto y los números en "leet".
*   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
*/

namespace Soluciones
{
  class Reto_01
  {
    static readonly Dictionary<string, string> leetDictionary = new()
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
      { "m", "/\\/\\" },
      { "n", "^/" },
      { "o", "0" },
      { "p", "|*" },
      { "q", "(_,)" },
      { "r", "I2" },
      { "s", "5" },
      { "t", "7" },
      { "u", "(_)" },
      { "v", "\\/" },
      { "w", "\\/\\/" },
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


    // Traduce la cadena de entrada cotejando cada caracter contra el diccionario
    // Si el caracter existe en el diccionario usa su equivalencia, sino el original
    static string LeetTranslate(string input)
    {
      string output = "";

      foreach (char inChar in input)
      {
        if (leetDictionary.TryGetValue(inChar.ToString(), out string? newChar))
        {
          output += newChar;
        }
        else
        {
          output += inChar;
        }
      }

      return output;
    }

    static public void Main()
    {
      Console.Write("Texto a traducir: ");
      string input = Console.ReadLine() ?? "";

      string output = LeetTranslate(input.ToLower());

      Console.WriteLine($"Texto traducido:  {output}");

      // Caso de uso:
      // prueba de lenguaje hacker
      // |*I2(_)3I34 )3 13^/&(_)4,_|3 #4[>|3I2

      Console.ReadKey();
    }
  }
}