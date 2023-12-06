import Foundation

struct CommitAuthor: Decodable {
    let name: String
    let date: String

    func getFormattedDate() -> String{
        let timeRange = date.index(date.endIndex, offsetBy: -9)..<date.index(date.endIndex, offsetBy: -4)
        let dayRange = date.index(date.startIndex, offsetBy: 8)..<date.index(date.startIndex, offsetBy: 10)
        let monthRange = date.index(date.startIndex, offsetBy: 5)..<date.index(date.startIndex, offsetBy: 7)
        return "\(date[dayRange])/\(date[monthRange])/\(date.prefix(4)) \(date[timeRange])"
    }
}

struct Commit: Decodable {
    let author: CommitAuthor
    let message: String

    func getFormattedMessage() -> String {
        return message.replacingOccurrences(of: "\n", with: " ")
    }
}

struct CommitResponse: Decodable {
    let sha: String
    let commit: Commit

    func getHash() -> String {
        return sha.prefix(7).uppercased()
    }
}

struct GitHubResponse: Decodable {
    var commitResponses: [CommitResponse] = Array()
}

func printLastCommits() {
    let repoUrl = URL(string: "https://api.github.com/repos/mouredev/retos-programacion-2023/commits?page=1&per_page=5")
    let session = URLSession.shared
    let task = session.dataTask(with: repoUrl!) { data, response, error in
        guard let data = data else { return }
        var index = 0
        let commitResponses = try! JSONDecoder().decode([CommitResponse].self, from: data)
        commitResponses.forEach{ commitResponse in
            index += 1
            print("Commit \(index) | \(commitResponse.getHash()) | \(commitResponse.commit.author.name) | \(commitResponse.commit.getFormattedMessage()) | \(commitResponse.commit.author.getFormattedDate())")
        }
    }
    task.resume()
}

printLastCommits()
