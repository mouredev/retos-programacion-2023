/*
 * Crea un programa que detecte cuando el famoso "Código Konami" se ha introducido correctamente
 * desde el teclado. Si sucede esto, debe notificarse mostrando un mensaje en la terminal.
 */

import Foundation

// Secuencia del código Konami
let konamiCode: [String] = ["⬆️", "⬆️", "⬇️", "⬇️", "⬅️", "➡️", "⬅️", "➡️", "B", "A"]

// Variables para realizar el seguimiento del código ingresado
var currentInput: [String] = []
var currentIndex = 0

// Función para verificar si se ha ingresado el código completo
func checkKonamiCode() {
    if currentInput == konamiCode {
        print("¡Código Konami introducido correctamente!")
    } else {
        print("Código incorrecto. Inténtalo de nuevo.")
        currentInput.removeAll()
        currentIndex = 0
    }
}

// Función para procesar las teclas ingresadas por el usuario
func processKey(_ key: String) {
    if key == konamiCode[currentIndex] {
        currentInput.append(key)
        currentIndex += 1

        if currentIndex == konamiCode.count {
            checkKonamiCode()
        }
    } else {
        print("Código incorrecto. Inténtalo de nuevo.")
        currentInput.removeAll()
        currentIndex = 0
    }
}

// Iniciar la lectura de teclas
print("Introduce el Código Konami:")

while currentIndex < konamiCode.count {
    if let key = readLine(strippingNewline: true) {
        processKey(key)
    }
}

