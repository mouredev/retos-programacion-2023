/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */

// Created by Gonzalo González on 3/1/23.

import Foundation

let normalAbc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
let hackerAbc = ["4", "13", "[", ")", "3", "|=", "&", "#", "1", ",_|", ">|", "1", "^^", "^/", "0", "|*", "(_,)", "12", "5", "7", "(_)", "\\/", "\\/\\/", "><", "j", "2"]


var dict: Dictionary<String, String> = Dictionary(uniqueKeysWithValues: zip(normalAbc, hackerAbc))

func translateToHacker (of input: String) -> String {
    
    var result = String()
    
    input.lowercased().forEach { word in
        result.append(dict[String(word)] ?? " ")
    }
    
    return result
}

let text = "Texto para comprobar reto primero de dos mil veintitres"
let result = translateToHacker(of: text)
