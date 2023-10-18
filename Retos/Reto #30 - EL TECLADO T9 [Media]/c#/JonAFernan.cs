using System.Text;
using System.Text.RegularExpressions;
/*
 * Los primeros dispositivos móviles tenían un teclado llamado T9
 * con el que se podía escribir texto utilizando únicamente su
 * teclado numérico (del 0 al 9).
 *
 * Crea una función que transforme las pulsaciones del T9 a su
 * representación con letras.
 * - Debes buscar cuál era su correspondencia original.
 * - Cada bloque de pulsaciones va separado por un guión.
 * - Si un bloque tiene más de un número, debe ser siempre el mismo.
 * - Ejemplo:
 *     Entrada: 6-666-88-777-33-3-33-888
 *     Salida: MOUREDEV
 */


namespace reto;
class Program
{
    static void Main(string[] args)
    {
       Console.WriteLine(T9KeyboardToText("6-666-88-777-33-3-33-888")); //MOUREDEV
       Console.WriteLine(T9KeyboardToText("22-777-2-444-7777-0-33-7777-0-6-666-88-777-33-3-33-888-11")); //BRAIS ES MOUREDEV.
       Console.WriteLine(T9KeyboardToText("666666-666-88-777-33-3-33-888")); //Error. Wrong text input. Wrong length.
       Console.WriteLine(T9KeyboardToText("6-686-88-777-33-3-33-888")); //Error. Wrong text input. No number or if a block has more than one number, it must always be the same.
       Console.WriteLine(T9KeyboardToText("6-686-88-777-33-3-33-")); //Error. Wrong text input. No number or if a block has more than one number, it must always be the same.
       Console.WriteLine(T9KeyboardToText("6,686-88-777-33-3-33-888")); //Error. Wrong text input. Wrong text format.
       
    }

    static string T9KeyboardToText(string numbers)
    {
        if(!Regex.IsMatch(numbers,@"^(\d+(\-)?)*$")) return "Error. Wrong text input. Wrong text format.";

        string[][] t9 = new string[][]
            {
            new string[] {" "},
            new string[] {",", ".","!","?"},
            new string[] {"a", "b","c"},
            new string[] {"d", "e","f"}, 
            new string[] {"g", "h","i"},
            new string[] {"j", "k","l"},
            new string[] {"m", "n","o","ñ"},
            new string[] {"p", "q","r","s"},
            new string[] {"t", "u","v"},
            new string[] {"w", "x","y","z"},
            };

        StringBuilder message= new StringBuilder();

        string[] splitString = numbers.Split('-');

        foreach (string item in splitString)
        {
            if(!Regex.IsMatch(item, @"^(\d)\1*$")) return "Error. Wrong text input. No number or if a block has more than one number, it must always be the same.";

            try
            {
                message.Append(t9[(int)Char.GetNumericValue(item[0])][item.Length - 1]);
            }
            catch (System.Exception)
            {
                
                return "Error. Wrong text input. Wrong length.";
            }
            
        }

        return message.ToString().ToUpper(); 
    }
        
        
}
