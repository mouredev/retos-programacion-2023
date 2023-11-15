using System.IO;

namespace RetosProgramacion
{
/*
 * Crea un programa capaz de interactuar con un fichero TXT.
 * IMPORTANTE: El fichero TXT NO debe subirse como parte de la corrección. 
 * Únicamente el código.
 * 
 * - Si no existe, debe crear un fichero llamado "text.txt".
 * - Desde el programa debes ser capaz de introducir texto por consola y guardarlo
 *   en una nueva línea cada vez que se pulse el botón "Enter".
 * - Si el fichero existe, el programa tiene que dar la opción de seguir escribiendo
 *   a continuación o borrar su contenido y comenzar desde el principio.
 * - Si se selecciona continuar escribiendo, se tiene que mostrar por consola
 *   el texto que ya posee el fichero.  
 */
    internal class Program
    {
        static void Main(string[] args)
        {
            string pathFile = Environment.GetFolderPath(Environment.SpecialFolder.Desktop) + @"\text.txt";
            string? option;
            string? text;

            if (File.Exists(pathFile))
            {
                Console.WriteLine("Pulse \"1\" para seguir escribiendo contenido en el archivo text.txt");
                Console.WriteLine("Pulse \"2\" para borrar el contenido del archivo text.txt");

                while ((option = Console.ReadLine()) != "1" && option != "2")
                {
                    Console.WriteLine("El valor insertado es incorrecto.");
                    Console.WriteLine("Pulse \"1\" para seguir escribiendo contenido en el archivo text.txt");
                    Console.WriteLine("Pulse \"2\" para borrar el contenido del archivo text.txt");
                }

                Console.WriteLine("Escriba el texto que quiera o escriba \"Exit\" para salir.");

                if (option == "1")
                {
                    Console.WriteLine();
                    ReadTextFile(pathFile);
                }
                else
                {
                    WriteTextFile(pathFile, string.Empty);
                }

            }
            else
            {
                FileStream fs = File.Create(pathFile);
                fs.Close();

                Console.WriteLine("Escriba el texto que quiera o escriba \"Exit\" para salir.");
            }

            while ((text = Console.ReadLine()) != "Exit")
            {
                if (text != null)
                    WriteTextFile (pathFile, text, true);
            }

        }

        private static void ReadTextFile(string pathFile)
        {
            using StreamReader reader = new StreamReader(pathFile);
                Console.WriteLine(reader.ReadToEnd());
        }

        private static void WriteTextFile(string path, string text, bool deleteContent = false)
        {
            using StreamWriter writer = new StreamWriter(path, deleteContent);
            {
                if (!deleteContent)
                    writer.Write(text);
                else
                    writer.WriteLine(text);

            }
        }
    }
}