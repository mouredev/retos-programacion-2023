using System.Globalization;
using System.Text;
using System.Text.RegularExpressions;

/*
 * Crea una función que sea capaz de leer el número representado por el ábaco.
 * - El ábaco se representa por un array con 7 elementos.
 * - Cada elemento tendrá 9 "O" (aunque habitualmente tiene 10 para realizar operaciones)
 *   para las cuentas y una secuencia de "---" para el alambre.
 * - El primer elemento del array representa los millones, y el último las unidades.
 * - El número en cada elemento se representa por las cuentas que están a la izquierda del alambre.
 *
 * Ejemplo de array y resultado:
 * ["O---OOOOOOOO",
 *  "OOO---OOOOOO",
 *  "---OOOOOOOOO",
 *  "OO---OOOOOOO",
 *  "OOOOOOO---OO",
 *  "OOOOOOOOO---",
 *  "---OOOOOOOOO"]
 *  
 *  Resultado: 1.302.790
 */


namespace reto;
class Program
{
    static void Main(string[] args)
    {
        string [] abacus = 
        {   
            "O---OOOOOOOO",
            "OOO---OOOOOO",
            "---OOOOOOOOO",
            "OO---OOOOOOO",
            "OOOOOOO---OO",
            "OOOOOOOOO---",
            "---OOOOOOOOO"};
        
        Console.WriteLine(AbacusToDigits(abacus)); //1.302.790

        
        string [] abacus2 = 
        {   "---OOOOOOOOO",
            "---OOOOOOOOO",
            "---OOOOOOOOO",
            "OO---OOOOOOO",
            "OOOOOOO---OO",
            "OOOOOOOOO---",
            "---OOOOOOOOO"};
        
        Console.WriteLine(AbacusToDigits(abacus2)); //2.790 

        string [] abacusErrorLength = 
        {   "---OOOOOOOOO",
            "---OOOOOOOOO",
            "OO---OOOOOOO",
            "OOOOOOO---OO",
            "OOOOOOOOO---",
            "---OOOOOOOOO"};
        
        Console.WriteLine(AbacusToDigits(abacusErrorLength)); //Error. Wrong length. The abacus must have 7 elements

        string [] abacusErrorFormat = 
        {   "---OOOOOOOOO",
            "---OOOOOOOOO",
            "---OOOOOOOOO",
            "OO---OOOOOOO",
            "OOOOOOO---OO",
            "-OOOOOOO---O",//error
            "---OOOOOOOOO"};
        
        Console.WriteLine(AbacusToDigits(abacusErrorFormat)); //Error. Wrong abacus format.

    }


    static string AbacusToDigits(string [] abacus)
    {
        if(abacus.Length != 7) return "Error. Wrong length. The abacus must have 7 elements";

        StringBuilder digits = new StringBuilder();

        foreach (string item in abacus)
        {
            if(Regex.Matches(item,@"[O]").Count != 9 || Regex.Matches(item,@"\-{3}").Count !=1 || Regex.Matches(item,@"\-").Count !=3 ) return "Error. Wrong abacus format";
            digits.Append(item.IndexOf('-'));
        }

        return Int32.Parse(digits.ToString()).ToString("#,##0", new CultureInfo("es-ES"));
    }
           
}
