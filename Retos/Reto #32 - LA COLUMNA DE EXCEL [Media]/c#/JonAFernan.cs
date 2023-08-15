/*
 * Crea una función que calcule el número de la columna de una hoja de Excel
 * teniendo en cuenta su nombre.
 * - Las columnas se designan por letras de la "A" a la "Z" de forma infinita.
 * - Ejemplos: A = 1, Z = 26, AA = 27, CA = 79.
 */

namespace reto;
class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine(ColumnNumber("AAA")); //703
        Console.WriteLine(ColumnNumber("CA")); // 79
        Console.WriteLine(ColumnNumber("Z")); //26
        Console.WriteLine(ColumnNumber("XFD")); // 16384
        Console.WriteLine(ColumnNumber("AaA")); // Error. Wrong column format.
    }


   static string ColumnNumber(string columnName)
   {
        const int alphabetLength = 26;
        const int asciiFirstLetter = 65;
        int pow = columnName.Length - 1;
        char [] alphabetIndex = Array.ConvertAll(Enumerable.Range(asciiFirstLetter, alphabetLength).ToArray(), i=> (char)i);
        double columnNumber = 0;

        foreach (var letter in columnName)
        {  
            if(!alphabetIndex.Contains(letter)) return "Error. Wrong column format.";

            columnNumber += (Math.Pow(alphabetLength, pow) * (Array.IndexOf(alphabetIndex, letter) + 1)); 
            pow--;
        }

        return columnNumber.ToString();
   }
           
}
