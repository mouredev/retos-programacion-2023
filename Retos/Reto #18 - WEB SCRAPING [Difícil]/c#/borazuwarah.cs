/*
 * El día 128 del año celebramos en la comunidad el "Hola Mundo day"
 * Vamos a hacer "web scraping" sobre su sitio web: https://holamundo.day
 *
 * Crea un programa que se conecte a la web del evento e imprima únicamente la agenda de eventos
 * del día 8. Mostrando hora e información de cada uno.
 * Ejemplo: "16:00 | Bienvenida"
 *
 * Se permite utilizar librerías que nos faciliten esta tarea.
 *
 */

using System;
using HtmlAgilityPack;

namespace Reto18
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string url = "https://holamundo.day";
            var web = new HtmlWeb();
            var doc = web.Load(url);

            var events = doc.DocumentNode.SelectNodes("//blockquote[@class='BlockquoteElement___StyledBlockquote-sc-1dtx4ci-0 slate-BlockquoteElement notion-quote unset-width']");

            foreach (var event in events)
            {
                if (event.InnerText.Contains("|"))
                    Console.WriteLine(event.InnerText);
            }
            Console.ReadKey();
        }
    }
}
