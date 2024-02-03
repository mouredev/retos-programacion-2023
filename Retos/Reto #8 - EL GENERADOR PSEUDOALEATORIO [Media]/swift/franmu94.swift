// Solucion sin usar Date. 

import Foundation

func numeroAleatorio1() -> Int {
    return Array(Set(0...1))[1]
}
func numeroAleatorio2() -> Int {
    return Array(Set(0...1))[0]
}

func aleatorio() -> Int {
    var resultado: Int
    repeat {
        resultado = numeroAleatorio1()
    } while (numeroAleatorio1() != numeroAleatorio2())
    return resultado
}

func prueba() {
    var resultados = [0:0, 1:0]
    for _ in 1...1000 {
        resultados[aleatorio()]! += 1
    }
    print(resultados)
}

//prueba() // [0: 496, 1: 504] , [0: 520, 1: 480] ...


//a base de un aleatoriedad de 0 ó 1 se pueden contruir todas las demas:
var numero: Int
repeat {
    let cadenaBin = Array(1...7).map{ _ in String(aleatorio()) }.reduce("",+)
    numero = Int(cadenaBin, radix: 2)!
    
} while numero > 100
print(numero)
