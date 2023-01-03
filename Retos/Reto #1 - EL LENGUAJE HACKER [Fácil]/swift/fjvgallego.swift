//
//  fjvgallego.swift
//  
//
//  Created by Francisco Javier Gallego Lahera on 3/1/23.
//

import Foundation

/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */

// DATA

let hackerDictionary: [String: String] = [
    // Alphabet
    "A": "4",       "B": "I3",      "C": "[",
    "D": ")",       "E": "3",       "F": "|:",
    "G": "&",       "H": "#",       "I": "1",
    "J": ",_|",     "K": ">|",      "L": "1",
    "M": "/\\/\\",  "N": "^/",      "O": "0",
    "P": "|*",      "Q": "(_,)",    "R": "I2",
    "S": "5",       "T": "7",       "U" : "(_)",
    "V": "\\/",     "W": "\\/\\/",  "X": "><",
    "Y": "j",       "Z": "2",
    
    // Numbers
    "1": "L",       "2": "R",       "3": "E",
    "4": "A",       "5": "S",       "6": "b",
    "7": "T",       "8": "B",       "9": "g",
    "0": "o"
]

func getHackerTranslation(of input: String) -> String {
    var hackerTranslation = ""
    
    for character in input {
        let strCharacter = String(character).uppercased()
        let hackerCharacter = hackerDictionary[strCharacter, default: strCharacter]
        hackerTranslation.append(hackerCharacter)
    }
    
    return hackerTranslation
}

// RESULTS

let message = "¡Los retos de mouredev me ayudan a practicar Swift en 2023!"
let hackerTranslation = getHackerTranslation(of: message)
print(hackerTranslation)
