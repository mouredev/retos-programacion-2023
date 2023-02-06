using System;

namespace TextToHackerSpeak
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Ingrese una frase:");
            string input = Console.ReadLine();

            // Convierte la frase en lenguaje hacker
            string output = ConvertToHackerSpeak(input);

            Console.WriteLine("La frase en lenguaje hacker es: " + output);
            Console.ReadLine();
        }

        static string ConvertToHackerSpeak(string input)
        {
            string output = "";
            // Este programa lee una frase del usuario y la convierte en lenguaje hacker 
            // reemplazando las letras a con 4, e con 3, i con 1, o con 0 y s con 5.
            foreach (char c in input)
            {
                switch (c)
                {
                    case 'a':
                        output += "4";
                        break;
                    case 'e':
                        output += "3";
                        break;
                    case 'i':
                        output += "1";
                        break;
                    case 'o':
                        output += "0";
                        break;
                    case 's':
                        output += "5";
                        break;
                    default:
                        output += c;
                        break;
                }
            }
            return output;
        }
    }
}
