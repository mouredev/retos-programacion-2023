using Newtonsoft.Json.Linq;
using System;
using System.IO;
using System.Net;
/*
* Llamar a una API es una de las tareas más comunes en programación.
*
* Implementa una llamada HTTP a una API (la que tú quieras) y muestra su
* resultado a través de la terminal. Por ejemplo: Pokémon, Marvel...
*
* Aquí tienes un listado de posibles APIs: 
* https://github.com/public-apis/public-apis
*/

namespace LaApi
{
    class Program
    {
        static void Main(string[] args)
        {

            Console.WriteLine("Deseas agregar el clima actual? (Y/N)");
            string respuesta = Console.ReadLine();
            Api api = new Api();

            var withWeather = respuesta == "y" ? true : false;
            api.getApi(withWeather);
        }
    }

    public class Api
    {
        public void getApi()
        {
            var url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m&current_weather=false";
            var request = (HttpWebRequest)WebRequest.Create(url);
            request.Method = "GET";
            request.ContentType = "application/json";
            request.Accept = "application/json";
            getResponse(request);

        }

        public void getApi(bool weather)
        {
            string url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m&current_weather=" + weather;
            var request = (HttpWebRequest)WebRequest.Create(url);
            request.Method = "GET";
            request.ContentType = "application/json";
            request.Accept = "application/json";
            getResponse(request);
        }

        private static void getResponse(HttpWebRequest request)
        {
            try
            {
                using (WebResponse response = request.GetResponse())
                {
                    using (Stream strReader = response.GetResponseStream())
                    {
                        if (strReader == null) return;
                        using (StreamReader objReader = new StreamReader(strReader))
                        {
                            string responseBody = objReader.ReadToEnd();
                            // Do something with responseBody
                            JObject jsonResponse = JObject.Parse(responseBody);
                            Console.WriteLine(jsonResponse);
                        }
                    }
                }
            }
            catch
            {

            }
        }
    }
}
