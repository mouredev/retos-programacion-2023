using System.Text.RegularExpressions;

/*
 * Crea una función que reciba una expresión matemática (String)
 * y compruebe si es correcta. Retornará true o false.
 * - Para que una expresión matemática sea correcta debe poseer
 *   un número, una operación y otro número separados por espacios.
 *   Tantos números y operaciones como queramos.
 * - Números positivos, negativos, enteros o decimales.
 * - Operaciones soportadas: + - * / % 
 *
 * Ejemplos:
 * "5 + 6 / 7 - 4" -> true
 * "5 a 6" -> false
 */

namespace reto;
class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine(IsMathematicalExpressions("5 + 6 / 7 - 4"));//true
        Console.WriteLine(IsMathematicalExpressions("3 + 4 * -2 * 8 % 10 - -4.6589 + 25 * 7.66666"));// true
        Console.WriteLine(IsMathematicalExpressions("5 a 6.9"));// false

    }

    static bool IsMathematicalExpressions(string input)
    {   
        return Regex.IsMatch(input,@"\A(-?\d*\.{0,1}\d+)(\s[+]\s\-?\d*\.{0,1}\d+)+");
    }
}
