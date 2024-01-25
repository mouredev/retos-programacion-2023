import Foundation
    

let puntuationForCharacter: [Character:Int] = [
    "a" : 1, "b" : 2, "c" : 3, "d" : 4, "e" : 5, "f" : 6, "g" : 7, "h" : 8, "i" : 9, "j" : 10,
    "k" : 11, "l" : 12, "m" : 13, "n" : 14, "ñ" : 15, "o" : 16, "p" : 17, "q" : 18, "r" : 19,
    "s" : 20, "t" : 21, "u" : 22, "v" : 23, "w" : 24, "x" : 25, "y" : 26, "z" : 27]

var counter: Int = 0
var flag = true

print("Introduce tu palabra")
print("Para salir del programa introduce [q")

while flag {
    if let word: String = readLine() {
        if word == "[q" {
            flag = false
            break
        }
        for character in word.lowercased() {
            counter += puntuationForCharacter[character] ?? 0
        }
        if counter == 100 {
            print("Palabra de \(counter) puntos. ¡Lo conseguiste!")
            flag = false
        } else {
            print("Palabra de \(counter), intentalo de nuevo")
        }
        counter = 0
    }
}

