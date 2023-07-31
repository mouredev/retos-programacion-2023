import Foundation

func cuentaAtras(inicio: Int, intervalo: Int) {
    guard inicio >= 0 && intervalo >= 0 else {
        print("Error: Solo se aceptan números enteros positivos.")
        return
    }
    
    var contador = inicio
    
    while contador > 0 {
        print(contador)
        contador -= 1
        sleep(UInt32(intervalo))
    }
    
    print("¡Cuenta atrás finalizada!")
}


cuentaAtras(inicio: 15, intervalo: 2)
