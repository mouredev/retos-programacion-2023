import Foundation

func escalera(escalones e: Int) {
    if e == 0 {
        print("__")
        return
    }
    let n = abs(e)
    let c = e > 0 ? "_|" : "|_"
    var arr = [String]()
    var espacios = ""
    for i in (0...n){
        if i == n && e > 0 {
            arr.append(espacios + "_")
        } else if i == 0 && e < 0 {
            arr.append(espacios + "_")
            espacios += " "
        } else {
            arr.append(espacios + c)
            espacios += "  "
        }
    }
    
    e > 0 ? arr.reversed().forEach{ print($0) } : arr.forEach{ print($0) }
}
escalera(escalones: -4)
escalera(escalones: 9)
escalera(escalones: 0)


