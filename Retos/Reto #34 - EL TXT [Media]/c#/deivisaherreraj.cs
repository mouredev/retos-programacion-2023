using System;
using System.IO;

namespace deivisaherreraj
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string filePath = "text.txt";

            if (!File.Exists(filePath))
            {
                File.Create(filePath).Close();
                Console.WriteLine("Se ha creado un nuevo archivo 'text.txt'.");
            }
            else
            {
                Console.WriteLine("El archivo 'text.txt' ya existe.");
                Console.WriteLine("¿Qué deseas hacer?");
                Console.WriteLine("1. Continuar escribiendo desde donde lo dejaste");
                Console.WriteLine("2. Borrar el contenido y comenzar desde el principio");
                Console.Write("Selecciona una opción (1/2): ");

                string? choice = Console.ReadLine();

                if (choice == "2")
                {
                    File.WriteAllText(filePath, string.Empty);
                    Console.WriteLine("Contenido borrado. Comienza a escribir desde el principio.");
                }
                else if (choice == "1")
                {
                    string content = File.ReadAllText(filePath);
                    Console.WriteLine("Contenido actual del archivo:");
                    Console.WriteLine(content);
                }
                else
                {
                    Console.WriteLine("Opción no válida. Continuando con el programa.");
                }
            }

            Console.WriteLine("\nEscribe el texto (presiona Enter para añadir una nueva línea):");

            using (StreamWriter writer = new StreamWriter(filePath, append: true))
            {
                while (true)
                {
                    string? input = Console.ReadLine();
                    if (string.IsNullOrWhiteSpace(input))
                    {
                        break;
                    }
                    writer.WriteLine(input);
                }
            }

            Console.WriteLine("Texto guardado en el archivo.");
        }
    }
}