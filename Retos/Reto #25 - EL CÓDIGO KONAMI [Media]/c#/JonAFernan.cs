using System.Text;
using System.Text.RegularExpressions;

/*
 * Crea un programa que detecte cuando el famoso "Código Konami" se ha introducido correctamente
 * desde el teclado. Si sucede esto, debe notificarse mostrando un mensaje en la terminal.
 */

namespace reto25;
class Program
{
    static void Main(string[] args)
    {
        string konamiCode = "UpArrowUpArrowDownArrowDownArrowLeftArrowRightArrowLeftArrowRightArrowAB";
        var userInput = new StringBuilder();
        bool konamiCodeInsert = true;
        while(!Regex.IsMatch(userInput.ToString(),konamiCode))
        {
            ConsoleKeyInfo push = Console.ReadKey(true);
            if(push.Key== ConsoleKey.Escape)
            {
                konamiCodeInsert= false;
                break;
            }
            userInput.Append(push.Key);
        } 
        
        System.Console.WriteLine(konamiCodeInsert ? "You have entered the Konami Code": "Game over");
    }

}
