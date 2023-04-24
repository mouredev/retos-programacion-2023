/*
 * Dada una URL con parámetros, crea una función que obtenga sus valores.
 * No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
 *
 * Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
 * los parámetros serían ["2023", "0"]
 */


string url ="https://retosdeprogramacion.com?yr=2023&challenge=0&parmetro5=otracosa&parametro7=2345";

var data = GetParameters(url);
foreach (var item in data)
{
    Console.WriteLine(item); 
}

Console.ReadKey();


static  List<string> GetParameters(string url)
{
    int total = url.Length;
    int position = url.IndexOf("?");
  
    if (position < total)
    {
        string parameter = url.Substring(position, total - position).Trim();
        parameter = parameter.Substring(1, parameter.Length-1); 
        char[] delimiterChars = {'&'};
        var parameters = parameter.Split(delimiterChars);
        List<string> returnData = new List<string>();
        foreach (var parameterValue in parameters)
        {
            Console.WriteLine(parameterValue.Substring(parameterValue.IndexOf("=") + 1, parameterValue.Length - parameterValue.IndexOf("=") - 1));
        }
    }
    return new List<string>();
}