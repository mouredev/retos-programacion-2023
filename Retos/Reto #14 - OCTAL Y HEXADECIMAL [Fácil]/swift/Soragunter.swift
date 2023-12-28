import UIKit

OctalHexadecimal(numeroentrada:1000)

func OctalHexadecimal(numeroentrada: Int)->(String, String){
    
    let numerodecimal = numeroentrada
    
    print("Has escrito el número \(numerodecimal) en decimal")
    
    // Sacar un número binario
    
    var arrayNumeroBinario : [Int] = []
    var numeroBinario = ""
    var dividendobinario = numerodecimal
    var cocientebinario = 0
    var restobinario = 0
    
    while true{
        
        if dividendobinario < 4 {
            
            cocientebinario = dividendobinario / 2
            restobinario = dividendobinario % 2
            
            arrayNumeroBinario.append(restobinario)
            arrayNumeroBinario.append(cocientebinario)
            break
            
        }else{
            
            cocientebinario = dividendobinario / 2
            restobinario = dividendobinario % 2
            
            arrayNumeroBinario.append(restobinario)
            dividendobinario = cocientebinario
            
        }
    }
    
    arrayNumeroBinario = arrayNumeroBinario.reversed()
    
    numeroBinario = arrayNumeroBinario.map({String($0)}).joined()
    
    print("Su correspondiente número en binario es: \(numeroBinario)")
    
    // Sacar un número octal
    
    var numeroOctal = ""
    var dividendoOctal = numerodecimal
    var cocienteOctal = 0
    var restoOctal = 0
    var arrayNumeroOctal : [Int] = []
    
    
    while true{
        
        if dividendoOctal < 64 {
            
            cocienteOctal = dividendoOctal / 8
            restoOctal = dividendoOctal % 8
            arrayNumeroOctal.append(restoOctal)
            arrayNumeroOctal.append(cocienteOctal)
            break
            
        }else{
            
            cocienteOctal = dividendoOctal / 8
            restoOctal = dividendoOctal % 8
            
            arrayNumeroOctal.append(restoOctal)
            dividendoOctal = cocienteOctal
            
        }
        
    }
    
    arrayNumeroOctal = arrayNumeroOctal.reversed()
    
    numeroOctal = arrayNumeroOctal.map({String($0)}).joined()
    
    print("Su correspondiente número en octal es: \(numeroOctal)")
    
    // Sacar un número hexadecimal
    
    var numeroHexadecimal = ""
    var dividendoHexadecimal = numerodecimal
    var cocienteHexadecimal = 0
    var restoHexadecimal = 0
    var arrayNumeroHexadecimalEntero : [Int] = []
    var arrayNumeroHexadecimal : [String] = []
    
    
    while true{
        
        if dividendoHexadecimal < 256 {
            
            cocienteHexadecimal = dividendoHexadecimal / 16
            restoHexadecimal = dividendoHexadecimal % 16
            arrayNumeroHexadecimalEntero.append(restoHexadecimal)
            arrayNumeroHexadecimalEntero.append(cocienteHexadecimal)
            break
            
        }else{
            
            cocienteHexadecimal = dividendoHexadecimal / 16
            restoHexadecimal = dividendoHexadecimal % 16
            
            arrayNumeroHexadecimalEntero.append(restoHexadecimal)
            dividendoHexadecimal = cocienteHexadecimal
            
        }
        
    }
    
    for i in arrayNumeroHexadecimalEntero{
        
        switch i{
        case 10:
            arrayNumeroHexadecimal.append("A")
        case 11:
            arrayNumeroHexadecimal.append("B")
        case 12:
            arrayNumeroHexadecimal.append("C")
        case 13:
            arrayNumeroHexadecimal.append("D")
        case 14:
            arrayNumeroHexadecimal.append("E")
        case 15:
            arrayNumeroHexadecimal.append("F")
        default:
            arrayNumeroHexadecimal.append(String(i))
        }
        
    }
    
    arrayNumeroHexadecimal = arrayNumeroHexadecimal.reversed()
    
    numeroHexadecimal = arrayNumeroHexadecimal.map({String($0)}).joined()
    
    print("Su correspondiente número en hexadecimal es: \(numeroHexadecimal)")
    
    return (numeroOctal, numeroHexadecimal)
}
