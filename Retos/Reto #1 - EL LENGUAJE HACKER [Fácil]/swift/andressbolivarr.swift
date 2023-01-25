//
//  code2.swift
//  
//
//  Created by Andres Bolivar on 1/22/23.
//
let leetSpeakAlphabet = [
    "A": "4", "B": "I3", "C": "[", "D": ")", "E": "3",
    "F": "|:", "G": "&", "H": "#", "I": "1", "J": ",_|",
    "K": ">|", "L": "1", "M": "/\\/\\", "N": "^/", "O": "0",
    "P": "|*", "Q": "(_,)", "R": "I2", "S": "5", "T": "7",
    "U": "(_)", "V": "\\/", "W": "\\/\\/", "X": "><", "Y": "j", "Z": "1",
    "0": "o", "1": "L", "2": "R", "3": "E", "4": "A",
    "5": "S", "6": "b", "7": "T", "8": "B", "9": "g"
]

func transformText(_ :String) -> String {
    var output = ""
    for character in text {
        let uppercaseCharacter = String(character).uppercased()
        if let leetSpeak = leetSpeakAlphabet[uppercaseCharacter] {
            output += leetSpeak
        } else {
            output += String(character)
        }
    }
    return output
}

let text = "Hello World!"
let transformedText = transformText(text)

print(transformedText)

