import Foundation

func findParameters(_ url: String) -> Any {
    var params = [String]()
    let urlDividida = url.split(separator: "?")
    
    if urlDividida.count > 1 {
        let listaParams = urlDividida[1].split(separator: "&")
        
        for param in listaParams {
            let clearParam = param.split(separator: "=")
            if clearParam.count > 1 && !clearParam[1].isEmpty {
                params.append(String(clearParam[1]))
            } else {
                return "La cadena no tiene parametros validos"
            }
        }
        
        return params
    } else {
        return "La cadena no tiene parametros"
    }
}

print(findParameters("https://retosdeprogramacion.com?year=2023&challenge=0"))
print(findParameters("https://retosdeprogramacion.com"))
print(findParameters("https://retosdeprogramacion.com?"))
print(findParameters("https://retosdeprogramacion.com?year=2023"))
print(findParameters("https://retosdeprogramacion.com?year=2023&"))
print(findParameters("https://retosdeprogramacion.com?year=&"))
print(findParameters("https://retosdeprogramacion.com?year=2023&challenge=0&languaje=python"))

