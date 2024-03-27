import Foundation

struct Character: Codable, Hashable {
    let id: UUID
    let name: String
}

if let url = URL(string: "https://hp-api.onrender.com/api/characters") {
    do {
        let data = try Data(contentsOf: url)
        let characters = try JSONDecoder().decode([Character].self, from: data)
        print(characters
            .map { $0.name }
            .formatted(.list(type: .and))
        )
    } catch {
        print(error)
    }
}