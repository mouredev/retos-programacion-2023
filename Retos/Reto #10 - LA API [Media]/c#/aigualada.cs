
using System.Net.Http.Json;

public class Program
{
    static async Task Main(string[] args)
    {
        using (var httpClient = new HttpClient())
        {

            HttpResponseMessage response = await httpClient.GetAsync("https://api.chucknorris.io/jokes/random");
            if (response.IsSuccessStatusCode)
            {
                var chuckNorrisResponse = await response.Content.ReadFromJsonAsync<ChuckNorrisJokesResponse>();
                Console.WriteLine($"Chuck Norris joke: {chuckNorrisResponse.Value}");
            }
            else
            {
                Console.WriteLine("No se ha podido conectar");
            }
        }
    }
}


public class ChuckNorrisJokesResponse
{
    public string IconUrl { get; set; }
    public string Id { get; set; }
    public string Url { get; set; }
    public string Value { get; set; }
}


