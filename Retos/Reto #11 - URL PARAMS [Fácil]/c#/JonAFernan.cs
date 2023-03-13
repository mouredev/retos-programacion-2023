namespace reto11;

/*
 * Dada una URL con parámetros, crea una función que obtenga sus valores.
 * No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
 *
 * Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
 * los parámetros serían ["2023", "0"]
 */
class Program
{
    static void Main(string[] args)
    {
        UrlParam("https://retosdeprogramacion.com?year=2023&challenge=0");
    }

    static void UrlParam(string url)
    {
        string parameter ="";
        List<string> listParameter = new List<string>();
        for (int i = 0; i < url.Length; i++)
        {
            if(url[i] == '=')
            {
                for (int j = i+1; j < url.Length; j++)
                {
                    if(url[j] == '&')
                    {
                        i = j;
                        listParameter.Add(parameter);
                        parameter="";
                        break;
                    } 
                    parameter += url[j];  
                    
                }
            }
        }
        if(parameter != "")listParameter.Add(parameter);

        if(listParameter.Count == 0) 
        {
            System.Console.WriteLine("No parameters in the URL");
            return;
        }

        if (listParameter.Count == 1) System.Console.Write("The parametes is ");
        else System.Console.Write("The parameters are ");
        System.Console.Write("[");
        
        foreach (var item in listParameter)
        {
            if(item == listParameter[listParameter.Count-1]) System.Console.Write($"\"{item}\"");
            else System.Console.Write($"\"{item}\", ");
        }
        
        System.Console.WriteLine("]");
    }
}
