import Foundation

func executeApi() {

    let urlSession = URLSession.shared
    let url = URL(string: "https://goweather.herokuapp.com/weather/leon")

    urlSession.dataTask(with: url!) { data, response, error in

        if let data = data {
            let json = try? JSONSerialization.jsonObject(with: data)
            print(String(describing: json))
        }
        print("Error \(String(describing: error))")
    }.resume()
    
}
print(executeApi())