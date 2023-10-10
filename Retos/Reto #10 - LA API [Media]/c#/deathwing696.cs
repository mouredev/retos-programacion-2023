/*
 * Llamar a una API es una de las tareas más comunes en programación.
 *
 * Implementa una llamada HTTP a una API (la que tú quieras) y muestra su
 * resultado a través de la terminal. Por ejemplo: Pokémon, Marvel...
 *
 * Aquí tienes un listado de posibles APIs: 
 * https://github.com/public-apis/public-apis
 */

using System;
using System.Net;
using System.IO;
using Newtonsoft.Json.Linq;


namespace deathwing696
{
    public class Deathwing696
    {
        public static void Main(string[] args)
        {
            string sURL;
            sURL = "https://api.open-meteo.com/v1/forecast?latitude=38.29&longitude=-0.66&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m";

            WebRequest wrGETURL;
            wrGETURL = WebRequest.Create(sURL);
            wrGETURL.Method = "GET";
            wrGETURL.ContentType = "application/json";

            try
            {
                using (WebResponse response = wrGETURL.GetResponse())
                {
                    using (Stream strReader = response.GetResponseStream())
                    {
                        if (strReader != null)
                        {
                            using (StreamReader objReader = new StreamReader(strReader))
                            {
                                string body = objReader.ReadToEnd();
                                JObject json = JObject.Parse(body);

                                foreach (var pair in json)
                                {
                                    Console.WriteLine("{0}: {1}", pair.Key, pair.Value);
                                }
                            }
                        }
                    }
                }
            }
            catch (Exception ex)
            {

            }


            Console.ReadLine();
        }
    }
}