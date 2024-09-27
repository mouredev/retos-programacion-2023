import Foundation

func leetCode(word: String) -> String {
    let leetDictionary: [String : String] = ["A": "4", "B": "I3", "C": "[", "D": ")", "E": "3", "F": "|=", "G": "&", "H": "#", "I": "1", "J": ",_|", "K": ">|", "L": "1", "M": "/\\/\\", "N": "^/", "O": "0", "P": "|*", "Q": "(_,)", "R": "I2", "S": "5", "T": "7", "U": "(_)", "V": "\\/", "W": "\\/\\/", "X": "><", "Y": "j", "Z": "2", "1": "L", "2": "R", "3": "E", "4": "A", "5": "S", "6": "b", "7": "T", "8": "B", "9": "g", "0": "o"]

    var leetWord = ""
    for letter in word {
        leetWord += leetDictionary[letter.description.uppercased()] ?? letter.description
    }
    return leetWord
}

print(leetCode(word: "1337"))
print(leetCode(word: "Texto de prueba para comprobar que funciona"))