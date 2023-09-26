using System.Xml.Linq;


public class Program
{
    static async Task Main(string[] args)
    {
        using (HttpClient httpClient = new HttpClient())
        {
            HttpResponseMessage response = await httpClient.GetAsync("https://api.geekdo.com/xmlapi/search?search=arkham horror");

            if (response.IsSuccessStatusCode)
            {
                var stream = response.Content.ReadAsStream();
                StreamReader sr = new StreamReader(stream, System.Text.Encoding.UTF8);
                var result = sr.ReadToEnd();

                List<XElement> boardGames = XElement.Parse(result).Elements().ToList();

                boardGames.ForEach(boardGame =>
                {
                    Console.WriteLine(boardGame.Elements().Where(e => e.Name.LocalName == "name").Single().Value);
                });
            }
        }
    }
}
