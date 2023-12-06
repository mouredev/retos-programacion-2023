namespace reto10;
using System.Net.Http;
using Newtonsoft.Json.Linq;

/*
 * Llamar a una API es una de las tareas más comunes en programación.
 *
 * Implementa una llamada HTTP a una API (la que tú quieras) y muestra su
 * resultado a través de la terminal. Por ejemplo: Pokémon, Marvel...
 *
 * Aquí tienes un listado de posibles APIs: 
 * https://github.com/public-apis/public-apis
 */
class Program
{
    static void Main(string[] args)
    {    
        RandomPokemon();   
        Console.ReadKey();
    }

    static async void RandomPokemon()
    {
        Random PokeID = new Random();
        string url = $"https://pokeapi.co/api/v2/pokemon/{PokeID.Next(1,1010)}";
        HttpClient client = new HttpClient();
        Pokemon randomPokemon = new Pokemon();

        
        using(client)
        {
            HttpResponseMessage response = await client.GetAsync(url);
            string json = await response.Content.ReadAsStringAsync();
            
            JObject pokeData = JObject.Parse(json);

            randomPokemon.Name =  pokeData["name"]?.ToString() ?? "none";
            randomPokemon.Name =  randomPokemon.Name.Substring(0, 1).ToUpper() + randomPokemon.Name.Substring(1);
            
            randomPokemon.Id =  pokeData["id"]?.ToString() ?? "none";
            randomPokemon.Type =  pokeData.SelectToken("$.types[0].type.name")?.ToString() ?? "none";
            randomPokemon.HeldItem = pokeData.SelectToken("$.held_items[0].item.name")?.ToString() ?? "none";
  
            
            Console.WriteLine($"The ramdom pokemon is {randomPokemon.Name}, "+
            $"Pokedex number {randomPokemon.Id}, {randomPokemon.Type} type and his held item is {randomPokemon.HeldItem}.");
            
        } 
    }

    class Pokemon
    {
        public string? Name { get; set; }
        public string? Id { get; set; }
        public string? Type {get; set;}
        public string? HeldItem {get; set;}
    }
}
