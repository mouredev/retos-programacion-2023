import UIKit

func getParams(from url: String) -> [String: String]? {
    var params: [String: String] = [:]
    let parts = url.split(separator: "?")
    
    if parts.count > 1 {
        let query: String = String(parts[1])
        for param in query.split(separator: "&") {
            let paramParts = param.split(separator: "=")
            if paramParts.count > 1 {
                let key: String = String(paramParts[0])
                let value: String = String(paramParts[1])
                params[key] = value
            } else {
                print("saltando parametro mal formado: \(param)")
                continue
            }
        }
    } else {
        return nil
    }
    
    return params
}

func printParams(of url: String) {
    print("-------------------- parametros --------------------")
    if let params = getParams(from: url) {
        print("Parametros encontrados: \(params)")
    } else {
        print("Sin parametros")
    }
    print("------------------ FIN parametros ------------------\n")
}

printParams(of: "https://retosdeprogramacion.com?year=2023&challenge=0")
printParams(of: "https://retosdeprogramacion.com")
printParams(of: "https://retosdeprogramacion.com?llave=valor&vacio=")
