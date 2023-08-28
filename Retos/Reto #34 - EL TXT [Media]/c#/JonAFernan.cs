using System.IO;
using System.Text;

namespace reto;

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

class Program
{
    static void Main(string[] args)
    {
        WriteFile();
    }
 

    static void WriteFile()
    {
        string path = @"C:\Reto\text.txt";
        bool stop = false;
        bool append;
        List<string> ?newLines = new List<string>();

        if(!File.Exists(path))
        {
            FileStream newTextFile = File.Create(path);
            System.Console.WriteLine("New file created");
            newTextFile.Close();
            fileExists = false;    
        }

        ReadText(path);

        else
        {
            Console.WriteLine("To delete content and start from beginning type DELETE");
            if(Console.ReadLine().ToUpper() == "DELETE") append = false;
        }
        
        System.Console.WriteLine("To finish typing type EXIT");

        do
        {
            string ?newLine = Console.ReadLine();
            if(newLine.ToUpper() == "EXIT") stop = true;
            else if(newLine != string.Empty) newLines.Add(newLine);
            
        } while(!stop);

          AddLines(path,newLines,append);
    }


    static void ReadText(string path)
    {
        using (StreamReader readText = File.OpenText(path))
        {

            if(readText != null)
            {
                String ?newLine ="";
                while ((newLine = readText.ReadLine()) != null)
                {
                        Console.WriteLine(newLine);      
                }
            }
        }
    }
    static void AddLines (string path, List<string> userWriteLines, bool append)
    {   
        using (StreamWriter writeText = new StreamWriter(path, append))
            {
                foreach (string line in userWriteLines)
                {
                    writeText.WriteLine(line);
                } 
            }	   
    }    
}
