import UIKit

struct FactResponse: Codable {
    var success: Bool
    var facts: [String]
}

enum FactError: Error {
    case badURL
    case text(message: String)
    case noData
    
    var localizedDescription: String {
        switch self {
        case .badURL:
            return "URL mal formada"
        case .text(let message):
            return message
        case .noData:
            return "No se recibieron datos"
        }
    }
}

func getRandomFact(completion: @escaping (Result<FactResponse, FactError>) -> Void) {
    guard let url: URL = URL(string: "https://dog-api.kinduff.com/api/facts") else {
        completion(.failure(.badURL))
        return
    }
    URLSession.shared.dataTask(with: url) { data, response, error in
        guard error == nil else {
            completion(.failure(.text(message: error!.localizedDescription)))
            return
        }
        if let data = data {
            do {
                let response: FactResponse = try JSONDecoder().decode(FactResponse.self, from: data)
                completion(.success(response))
            } catch {
                completion(.failure(.text(message: error.localizedDescription)))
            }
        } else {
            completion(.failure(.noData))
        }
    }.resume()
}

func printFact() {
    getRandomFact { result in
        switch result {
        case .success(let response):
            for fact in response.facts {
                print("Fact: \(fact)")
            }
        case .failure(let error):
            print("Error: \(error.localizedDescription)")
        }
    }
}

printFact()
printFact()
printFact()
