using System;
using System.Collections.Generic;

class miguelex
{
    static void FindParameters(string cadena)
    {
        List<string> paramsList = new List<string>();

        string[] urlDividida = cadena.Split('?');

        if (urlDividida.Length > 1)
        {
            string[] listaParams = urlDividida[1].Split('&');

            foreach (string param in listaParams)
            {
                string[] clearParam = param.Split('=');
                if (clearParam.Length > 1 && clearParam[1] != "")
                {
                    paramsList.Add(clearParam[1]);
                }
            }

            if (paramsList.Count > 0)
            {
                Console.Write("[");
                foreach (string param in paramsList)
                {
                    Console.Write("\"" + param + "\"");
                    if (param != paramsList[paramsList.Count - 1])
                    {
                        Console.Write(", ");
                    }
                }
                Console.Write("]\n");
            }
            else
            {
                Console.WriteLine("La Url no tiene parametros");
            }
        }
        else
        {
            Console.WriteLine("La Url no tiene parametros");
        }
    }

    static void Main(string[] args)
    {
        FindParameters("https://retosdeprogramacion.com?year=2023&challenge=0");
        FindParameters("https://retosdeprogramacion.com");
        FindParameters("https://retosdeprogramacion.com?");
        FindParameters("https://retosdeprogramacion.com?year=2023");
        FindParameters("https://retosdeprogramacion.com?year=2023&");
        FindParameters("https://retosdeprogramacion.com?year=&");
        FindParameters("https://retosdeprogramacion.com?year=2023&challenge=0&languaje=python");
    }
}
