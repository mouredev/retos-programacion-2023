import Foundation

enum errorContra: Error {
    case longitudInvalida
}




func genrarContra(long l: Int = 8, conMayus: Bool = true, conNumeros: Bool = true, conSimbolos: Bool = true ) throws -> String {
    
    if l < 8 || l > 16 {
        throw errorContra.longitudInvalida
    }
    
    var arr = Array("qwertyuiopasdfghjklzxcvbnm")
    if conMayus {
        arr += Array("QWERTYUIOPASDFGHJKLZXCVBNM")
    }
    if conNumeros {
        arr += Array("1234567890")
    }
    if conSimbolos {
        arr += Array("!·$%&()=?¿*^¨Ç+`´ç-.,_:;")
    }
    var result = ""
    
    for i in 1...l {
        result += String(arr.randomElement()!)
    }
    
    
    
    
    return (result)
}


print(genrarContra(long: 16))


