import Foundation


let hackerDictionary: [Character : String] = [
    "a" : "4", "b" : "I3", "c" : "[", "d" : ")", "e" : "3", "f" : "|=", "g" : "&", "h" : "#",
    "i" : "1", "j" : ",_|", "k" : ">|", "l" : "|_", "m" : "/\\/\\", "n" : "^/", "o" : "0",
    "p" : "|*", "q" : "(_,)", "r" : "I2", "s" : "5", "t" : "7", "u" : "(_)", "v" : "\\/", "w" : "\\/\\/",
    "x" : "><", "y" : "`/", "z" : "-/_", " " : " ", "A" : "4", "B" : "I3", "C" : "[", "D" : ")",
    "E" : "3", "F" : "|=", "G" : "&", "H" : "#", "I" : "1", "J" : ",_|", "K" : ">|", "L" : "|_",
    "M" : "/\\/\\", "N" : "^/", "O" : "0","P" : "|*", "Q" : "(_,)", "R" : "I2", "S" : "5",
    "T" : "7", "U" : "(_)", "V" : "\\/", "W" : "\\/\\/", "X" : "><", "Y" : "`/", "Z" : "-/_"
]

func printHackerLenguage(_ str: String) -> String {
    var hackerWord = ""

    for s in str {
        if let value = hackerDictionary[s] {
            hackerWord.append(value)
        }
    }
    return hackerWord
}

print("Ingresa el texto:")
if let input = readLine() {
    let hackerWord = printHackerLenguage(input)
    print(hackerWord)
}

