using HtmlAgilityPack;

namespace reto18;

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
class Program
{
    static void Main(string[] args)
    {
		HtmlWeb web = new HtmlWeb();
		HtmlAgilityPack.HtmlDocument doc = web.Load("https://holamundo.day/");

        HtmlNode agendaDate = doc.DocumentNode.SelectSingleNode("//html/body/div/div/div/div[2]/div/div/section[7]/div[2]/div/article/h1[2]");
       
        HtmlNode dateToPrintNode = agendaDate.NextSibling;

        while (dateToPrintNode.Attributes["class"].Value.Contains("BlockquoteElement___StyledBlockquote-sc-1dtx4ci-0 slate-BlockquoteElement notion-quote unset-width"))
        {
            Console.WriteLine(dateToPrintNode.InnerText);
            dateToPrintNode = dateToPrintNode.NextSibling;
        }
    }

}
