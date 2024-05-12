import Foundation

struct Info: Codable {
    let count: Int
    let totalPages: Int
    let previousPage: String?
    let nextPage: String?
}

struct CharacterDataResponse: Codable {
    let info: Info
    let data: [DisneyCharacter]
}

struct DisneyCharacter: Codable {
    let _id: Int
    let films: [String]
    let shortFilms: [String]
    let tvShows: [String]
    let videoGames: [String]
    let parkAttractions: [String]
    let allies: [String]
    let enemies: [String]
    let sourceUrl: String
    let name: String
    let imageUrl: String?
    let createdAt: String
    let updatedAt: String
    let url: String
    let __v: Int
}

// Definir la URL de la API
var apiUrlString = "https://api.disneyapi.dev/character"
guard let apiUrl = URL(string: apiUrlString) else {
    print("URL inválida")
    exit(1)
}

// Crear una solicitud URLRequest
var request = URLRequest(url: apiUrl)
request.httpMethod = "GET"

// Crear una sesión URLSession
let session = URLSession.shared

// Crear una tarea de datos
let task = session.dataTask(with: request) { (data, response, error) in
    // Verificar si hay algún error
    if let error = error {
        print("Error: \(error)")
        return
    }
    
    // Verificar si se recibió una respuesta HTTP
    guard let httpResponse = response as? HTTPURLResponse else {
        print("Respuesta HTTP inválida")
        return
    }
    
    // Verificar si la solicitud fue exitosa (código de estado 2xx)
    guard (200...299).contains(httpResponse.statusCode) else {
        print("Error en la solicitud. Código de estado: \(httpResponse.statusCode)")
        return
    }
    
    // Verificar si se recibieron datos
    guard let responseData = data else {
        print("No se recibieron datos")
        return
    }
    
    do {
        // Decodificar la respuesta en la estructura CharacterDataResponse
        let characterDataResponse = try JSONDecoder().decode(CharacterDataResponse.self, from: responseData)
        
        // Acceder a los datos de los personajes
        for character in characterDataResponse.data {
            print("Nombre: \(character.name), Películas: \(character.films)")
            // Puedes acceder a otros datos aquí según sea necesario
        }
    } catch {
        print("Error al decodificar los datos: \(error)")
    }
}

// Empezar la tarea
task.resume()

// Espera un segundo para que de tiempo ha terminar la tarea
sleep(1)

