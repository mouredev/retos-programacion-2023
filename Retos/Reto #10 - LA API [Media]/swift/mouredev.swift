import Foundation
import PlaygroundSupport

let page = PlaygroundPage.current
page.needsIndefiniteExecution = true

struct PokemonList: Decodable {
    let results: [Pokemon]
}

struct Pokemon: Decodable {
    let name: String
}

if let url = URL(string: "https://pokeapi.co/api/v2/pokemon?limit=151") {
    
    let request = URLRequest(url: url)
    let (data, response) = try await URLSession.shared.data(for: request)
    
    if (response as? HTTPURLResponse)?.statusCode == 200 {
        let pokemonList = try JSONDecoder().decode(PokemonList.self, from: data)
        for (index, pokemon) in pokemonList.results.enumerated() {
            let pokemonName = pokemon.name
            print("#\(index + 1) \(pokemonName)")
        }
        
        page.finishExecution()
    }
}
