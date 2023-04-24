using Reto_1;
using System;

namespace Translator
{
    public class Program
    {
        public static void Main(string[] args)
        {
            Input.Translate();
			Console.WriteLine("La útlima línea es la traducción.");
        }
    }
}

// Creamos una nueva clase que hará la función de traducir.
namespace Reto_1
{
    internal class Input
    {
        static public void Translate()
        {
            Console.WriteLine("Ingrese un texto:");
            string input = Console.ReadLine();

            // Si el usuario no escribe nada en el input, se le pide que lo vuelva a hacer.
            if (input == "")
            {
                Console.WriteLine("¡Uepa! Debes de escribir un mensaje a traducir.");
                Input.Translate();
            }
            else
            {

            }
            // Convertimos el input del usuario a letras mayúsculas.
            input = input.ToUpper();
            string output = string.Empty;

            string[] leetLetters = { "4", "I3", "[", ")", "3", "|=", "&", "#", "1", ",_|", ">|", "1", @"/\/\", "^/", "0", "|*", "(_,)", "I2", "5", "7", "(_)", @"\/", @"\/\/", "><", "j", "2"};
            foreach(char letter in input)
            {
				// Se compara la letra escrita con el indice al que pertenece. Es decir: A tiene indice [0] == 4. B tiene indice [1] == I3.
                if (letter >= 'A' && letter <= 'Z')
                {
                    int index = letter - 'A';
                    output += leetLetters[index];
                }
                else
                {
                    output += letter;
                }
                Console.WriteLine(output);
            }
        }
    }
}
