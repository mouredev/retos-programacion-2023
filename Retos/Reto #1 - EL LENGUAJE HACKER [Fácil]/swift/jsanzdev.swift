/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */

import Foundation

// Declaramos un diccionario con las equivalencias

let equivalencias: [Character: String] = [
    "a": "4",
    "b": "8",
    "c": "(",
    "d": "|)",
    "e": "3",
    "f": "|=",
    "g": "6",
    "h": "#",
    "i": "!",
    "j": "_|",
    "k": "|<",
    "l": "1",
    "m": "|\\/|",
    "n": "|\\|",
    "o": "0",
    "p": "|2",
    "q": "(_,)",
    "r": "|2",
    "s": "5",
    "t": "7",
    "u": "|_|",
    "v": "\\/",
    "w": "\\/\\/",
    "x": "><",
    "y": "`/",
    "z": "2",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
    "0": "0"
]

let string = "Hello World!"

// Recorremos el string y vamos sustituyendo los caracteres

var result = ""

for char in string {
    if let value = equivalencias[char] {
        result += value
    } else {
        result += String(char)
    }
}

print("The String \(string) is \(result) in leet language")




 
