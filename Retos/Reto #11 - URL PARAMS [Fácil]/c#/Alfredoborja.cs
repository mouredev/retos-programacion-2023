/*
 * Dada una URL con parámetros, crea una función que obtenga sus valores.
 * No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
 *
 * Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
 * los parámetros serían ["2023", "0"]
 */
using System;
using System.Collections.Generic;

namespace URLPARAMS
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string url = "https://www.google.com/search?q=et5x+accessories+guide&source=lnms&tbm=isch&sa=X&ved=2ahUKashZ-oz-3-D9AhXlcvbsSEQnHeMfD-sQ_AUoAXoECAEQAw&biw=1920&bih=919&dpr=1";
            Parameters parameters = new Parameters(url);
            parameters.getParams();
        }
    }

    public class Parameters
    {
        private string Url { get; set; }
        public Parameters(string url)
        {
            Url = url;
        }
        public void getParams()
        {
            int indexStart = Url.IndexOf("=");
            int indexEnd = Url.IndexOf("&") == -1 ? Url.Length : Url.IndexOf("&");
            
            List<string> values = new List<string>();
            while(Url.Contains("="))
            {
                values.Add(Url.Substring(indexStart + 1, indexEnd - indexStart - 1));

               if(indexEnd < Url.Length)
                {
                    Url = Url.Substring(indexEnd + 1);
                }
                else
                {
                    break;
                }
                
                indexStart = Url.IndexOf("=");
                indexEnd = Url.IndexOf("&") == -1 ? Url.Length : Url.IndexOf("&");
            }
            foreach(var value in values)
            {
                Console.WriteLine(value);
            }

        }
    }
}
