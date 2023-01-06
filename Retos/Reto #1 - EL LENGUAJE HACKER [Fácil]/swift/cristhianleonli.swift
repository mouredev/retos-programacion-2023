import Foundation

let leetSpeakAlphabet = [
    // Alphabet
    "A": "4",       "B": "I3",
    "C": "[",       "D": ")",
    "E": "3",       "F": "|:",
    "G": "&",       "H": "#",
    "I": "1",       "J": ",_|",
    "K": ">|",      "L": "1",
    "M": "/\\/\\",  "N": "^/",
    "O": "0",       "P": "|*",
    "Q": "(_,)",    "R": "I2",
    "S": "5",       "T": "7",
    "U": "(_)",     "V": "\\/",
    "W": "\\/\\/",  "X": "><",
    "Y": "j",       "Z": "1",
    
    // Numbers
    "0": "o",
    "1": "L",
    "2": "R",
    "3": "E",
    "4": "A",
    "5": "S",
    "6": "b",
    "7": "T",
    "8": "B",
    "9": "g"
]

func convertToLeetSpeak(text: String) -> String {
    return text
        .map { String($0).uppercased() }
        .compactMap { leetSpeakAlphabet[$0] }
        .joined()
}

let result = convertToLeetSpeak(text: "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
print(result)
