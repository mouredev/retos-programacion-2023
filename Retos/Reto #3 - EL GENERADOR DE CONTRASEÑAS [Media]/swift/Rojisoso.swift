import Foundation


func GenerarContra(longitud: Int,numeros: Bool,minusculas: Bool,mayusculas: Bool,simbols: Bool){
    
    let MyNumbers = ["0","1","2","3","4","5","6","7","8","9"]
    let MyLowerCase = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","ñ","z","x","c","v","b","n","m"]
    let MyUpperCase = ["Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Ñ","Z","X","C","V","B","N","M"]
    let MySimbols = ["!","#","$","%","&","/","@",".",":",",",";","-","_","}","{","[","]","*","+","?","¿","¡","=","(",")"]

    var contraseña = ""
    var MyArray = [""]
    
    if longitud>7 && longitud<17{
        
        if numeros{
            MyArray = MyArray + MyNumbers
        }
        if minusculas{
            MyArray = MyArray + MyLowerCase
        }
        if mayusculas{
            MyArray = MyArray + MyUpperCase
        }
        if simbols{
            MyArray = MyArray + MySimbols
        }
        
        for _ in 0..<longitud{
            
            var temp = Int.random(in: 0..<MyArray.count)
            contraseña = contraseña + MyArray[temp]
        }
        print("La contraseña generada aleatoreamente de \(longitud) caracteres es: \(contraseña)")
    }
    else{
        print("Introduzca un número entre 8 y 16")
    }
}

GenerarContra(longitud: 16,numeros: true,minusculas: true,mayusculas: true,simbols: true)
GenerarContra(longitud: 8,numeros: false,minusculas: true,mayusculas: false,simbols: true)
GenerarContra(longitud: 5,numeros: true,minusculas: false,mayusculas: true,simbols: true)
GenerarContra(longitud: 10,numeros: false,minusculas: true,mayusculas: true,simbols: true)
GenerarContra(longitud: 14,numeros: true,minusculas: false,mayusculas: true,simbols: false)
