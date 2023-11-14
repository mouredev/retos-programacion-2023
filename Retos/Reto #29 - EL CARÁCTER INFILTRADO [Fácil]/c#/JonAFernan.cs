/*
 * Crea una función que reciba dos cadenas de texto casi iguales,
 * a excepción de uno o varios caracteres. 
 * La función debe encontrarlos y retornarlos en formato lista/array.
 * - Ambas cadenas de texto deben ser iguales en longitud.
 * - Las cadenas de texto son iguales elemento a elemento.
 * - No se pueden utilizar operaciones propias del lenguaje
 *   que lo resuelvan directamente.
 * 
 * Ejemplos:
 * - Me llamo mouredev / Me llemo mouredov -> ["e", "o"]
 * - Me llamo.Brais Moure / Me llamo brais moure -> [" ", "b", "m"]
 */


namespace reto;
class Program
{
    static void Main(string[] args)
    {
        
        FindDifferences("Me llamo mouredev" , "Me llamo mouredev"); // No differences found
        FindDifferences("Me llamo mouredev" , "Me llamo Paco"); // Error. Different length.
        FindDifferences("Me llamo brais moure" , "Me llamo.Brais Moure"); // [".", "B", "M"]

    }

    static void FindDifferences(string originalInput , string inputToCheck )
    {   
       List<char> differences = new List<char>();
       bool firstDifference = true;

       if(originalInput.Length != inputToCheck.Length)
       {

            Console.WriteLine("Error. Different length.");
            return;
        
       }

       for (int i = 0; i < originalInput.Length; i++)
       {
            if(originalInput[i] != inputToCheck[i]) differences.Add(inputToCheck[i]);
       }
       
       if(differences.Count != 0)
       {
            Console.Write("[");
            foreach(char item in differences) 
            {    
                Console.Write(firstDifference ? "" : ", ");
                Console.Write($"\"{item}\"");
                firstDifference = false;
            
            }
            Console.Write("]");
       }

       else Console.WriteLine("No differences found");
       
       

    }
}
