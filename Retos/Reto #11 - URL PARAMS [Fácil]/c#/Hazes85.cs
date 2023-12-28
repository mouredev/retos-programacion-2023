namespace urlparams
{
    class urlparams
    {
        /*
        * Dada una URL con parámetros, crea una función que obtenga sus valores.
        * No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
        *
        * Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
        * los parámetros serían ["2023", "0"]
        */
        
        static void Main(string[] args)
        {
            string url = "https://retosdeprogramacion.com?year=2023&challenge=0";
            List<string> urlParams = (url.Split('?')[1]).Split('&').ToList();
            Dictionary<string, string> keyValues = new Dictionary<string, string>();

            urlParams.ForEach(param =>
            {
                string key = param.Split('=')[0];
                string value = param.Split('=')[1];
                keyValues.Add(key, value);
            });

            if (keyValues.Count > 0)
            {
                foreach (var keyvalue in keyValues)
                {
                    Console.WriteLine($"key: {keyvalue.Key} -> value: {keyvalue.Value}");
                }
            }
            else
            {
                Console.WriteLine("Don't contain parameters");
            }
        }
    }
}