import Foundation

private func getParams(url: String) -> Array<String> {
    var params = Array<String>()
    
    let urlParts = url.split(separator: "?")
    if(urlParts.count > 1) {
        let paramPairs = urlParts[1]
        paramPairs.split(separator: "&").forEach {
            let paramPair = $0.split(separator: "=")
            if(paramPair.count > 1) {
                params.append(String(paramPair[1]))
            }
        }
    }
    
    return params    
}

print(getParams(url: "https://retosdeprogramacion.com?year=2023&challenge=0"))
print(getParams(url: "https://retosdeprogramacion.com?year=2023&challenge"))
print(getParams(url: "https://retosdeprogramacion.com"))