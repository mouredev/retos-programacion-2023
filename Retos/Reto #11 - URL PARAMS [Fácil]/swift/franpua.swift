import Foundation

func urlParams(url: String) -> [String] {
    
    guard let indexParams = url.firstIndex(of: "?") else {
        return ["Esta URL no tiene parámetros"]
    }
    let stringParams = url[indexParams...]
    let paramsNoQuestion = stringParams.dropFirst()
    let arrayParams = paramsNoQuestion.split(separator: "&")
    
    let valores = arrayParams.compactMap { (parameter) -> String? in
        let elements = parameter.split(separator: "=")
        guard elements.count == 2 else { return nil}
        
        let valor = elements[1]
        return valor.description
    }
    
    return valores
}

print(urlParams(url: "https://retosdeprogramacion.com?year=2023&challenge=0"))
print(urlParams(url: "https://retosdeprogramacion.com?year=2023"))
print(urlParams(url: "https://retosdeprogramacion.com"))
print(urlParams(url: "https://www.amazon.es/?&tag=hydesnav-21&ref=pd_sl_781oit2196_e&adgrpid=55589983189&hvpone=&hvptwo=&hvadid=366505385428&hvpos=&hvnetw=g&hvrand=12839864960490236407&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1005453&hvtargid=kwd-10573980&hydadcr=4855_1809862"))