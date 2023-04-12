/*
 *Crea una función que reciba un número decimal y lo trasforme a Octal
 * y Hexadecimal.
 * - No está permitido usar funciones propias del lenguaje de programación que
 * realicen esas operaciones directamente.
 */

using System.Globalization;
using System.Runtime.InteropServices;

namespace Reto_14
{
    internal class Program
    {
        static void Main(string[] args)
        {
            bool isNumber;
            string input;
            int num;

            Console.WriteLine("Bienvenido al conversor de números de decimal a octal y hexagonal. Pulse cualquier tecla para continuar.");
            Console.ReadKey();

            while (true)
            {
                Console.WriteLine("Escriba un número a procesar:");

                do
                {
                    input = Console.ReadLine();
                    isNumber = int.TryParse(input, out num);
                    if (!isNumber)
                    {
                        Console.WriteLine("¡Uepa! Eso no es un número. Prueba a introducir otro.");
                    }
                }

                while (!isNumber); //Repetimos el ciclo hasta que la entrada sea un número.

                Console.WriteLine($"El número a procesar es: {num}.");
                Console.WriteLine($"Decimal = {num}.");
                Program.Octal(num);
                Program.Hexadecimal(num);
                Console.WriteLine("¿Quiere convertir otro número decimal a octal y hexadecimal? Pulse 1 para repetir el programa o 0 para cerrarlo.");
                string exit = Console.ReadLine();

                if (exit == "1")
                {

                }
                else
                {
                    Console.WriteLine("Cerrando programa en 3 segundos...");
                    Thread.Sleep(1000); //Esperamos 1 segundos.
                    Console.WriteLine("2 segundos...");
                    Thread.Sleep(1000);
                    Console.WriteLine("1 segundo...");
                    Thread.Sleep(1000);
                    Console.WriteLine("Adios :)");
                    Thread.Sleep(500);
                    break;
                }
            }
        }


        static void Octal(int num) //Pasamos la variable "num" como argumento para poder utilizarla dentro del método.
        {
            string octal = "";

            while (num > 0)
            { 
                int rest = num % 8;
                num /= 8;
                octal = rest.ToString() + octal;
            }
            Console.WriteLine($"Octal = {octal}.");
        }

        static void Hexadecimal(int num)
        {
            string hexadecimal = "";
            Dictionary<int, char> hexChars = new Dictionary<int, char>
            {
                {0,'0'},
                {1,'1'},
                {2,'2'},
                {3,'3'},
                {4,'4'},
                {5,'5'},
                {6,'6'},
                {7,'7'},
                {8,'8'},
                {9,'9'},
                {10,'A'},
                {11,'B'},
                {12,'C'},
                {13,'D'},
                {14,'E'},
                {15,'F'}
            };

            while (num > 0)
            {
                int rest = num % 16;
                num /= 16; //Dividimos num entre 8 y le asignamos el valor resultante.
                hexadecimal = hexChars[rest] + hexadecimal;
            }
            Console.WriteLine($"Hexadecimal = {hexadecimal}.");
        }
    }
}
