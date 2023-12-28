 
/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */

namespace Reto1
{
    class Program
    {
        static void Main(string[] args)
        {
           string SenteceHacker = "" ;
           Dictionary <string,string> alphabetHacker= CreateAlphabetHacker();  
           string sentece =  Console.ReadLine();  

        foreach (var x in sentece)
        {
            string caracter = x.ToString().ToUpper();
        
           if (alphabetHacker.ContainsKey(caracter)){

                    SenteceHacker += alphabetHacker[caracter].ToString();
            }else
            {
                SenteceHacker += x; 
            }  
        } 

        Console.WriteLine(SenteceHacker); 
        }

        static public Dictionary<string,string> CreateAlphabetHacker()
        {
           var alphabetHacker= new Dictionary<string, string>(){
                {"A", "4"},
				{"B", "I3"},
				{"C", "["},
				{"D", ")"},
				{"E", "3"},
				{"F", "|="},
				{"G", "&"},
				{"H", "#"},
				{"I", "1"},
				{"J", ",_|"},
				{"K", ">|"},
				{"L", "1"},
				{"M", @"/\/\"},
				{"N", "^/"},  
				{"Ñ", "Na4" },
				{"O", "0"},
				{"P", "|*"},
				{"Q", "(_,)"},
				{"R", "I2"},
				{"S", "5"},
				{"T", "7"},
				{"U", "(_)"},
				{"V", @"\/"},
				{"W", @"\/\/"},
				{"X", "><"},
				{"Y", "j"},
				{"Z", "2"}
           }; 
            return alphabetHacker;
        }
    }
    
}


 