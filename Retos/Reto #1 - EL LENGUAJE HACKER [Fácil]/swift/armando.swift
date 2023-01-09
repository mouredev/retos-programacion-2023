/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */


import UIKit

func getTextHacker(inputText: String) -> String {
    let alpaphet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    let hackerAlpha = ["4", "13", "[", ")", "3", "|=", "&", "#", "1", ",_|", ">|", "1", "^^", "^/", "0", "|*", "(_,)", "12", "5", "7", "(_)", "\\/", "\\/\\/", "><", "j", "2"]
    
    let lowerCaseText = inputText.lowercased()
    var hackerText = ""
    lowerCaseText.forEach { element in
        alpaphet.forEach { letter in
            if  letter.contains(element) {
                let index = alpaphet.firstIndex(where: {$0.contains(element)})
                hackerText = hackerText + hackerAlpha[index ?? 0]
            }
        }
    }
    
    return(hackerText)
}


let testText = "LEET"

print(getTextHacker(inputText: testText))
