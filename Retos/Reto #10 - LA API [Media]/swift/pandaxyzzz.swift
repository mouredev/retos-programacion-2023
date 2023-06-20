import Foundation

func makeRequest() {
    let url = URL(string: "https://api.ipify.org")!
    var components = URLComponents(url: url, resolvingAgainstBaseURL: false)!
    components.queryItems = [URLQueryItem(name: "format", value: "json")]

    var request = URLRequest(url: components.url!)
    request.setValue("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36", forHTTPHeaderField: "User-Agent")

    let task = URLSession.shared.dataTask(with: request) { data, response, error in
        guard let data = data, error == nil else {
            print("Error: \(error?.localizedDescription ?? "Unknown error")")
            return
        }

        if let json = try? JSONSerialization.jsonObject(with: data, options: []) as? [String: Any],
           let ipAddress = json["ip"] as? String {
            print(ipAddress)
        } else {
            print("Error: Invalid response format")
        }
    }

    task.resume()
}
