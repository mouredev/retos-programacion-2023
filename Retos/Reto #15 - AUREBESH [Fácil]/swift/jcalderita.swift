import Foundation

let latin = [
    "A", "B", "C", "D", "E", 
    "F", "G", "H", "I", "J",
    "K", "L", "M", "N", "O",
    "P", "Q", "R", "S", "T",
    "U", "V", "W", "X", "Y", "Z"
]

let aurebesh = [
    "Aurek", "Besh", "Cresh", "Dorn", "Enth",
    "Forn", "Grek", "Herf", "Isk", "Jenth",
    "Krill", "Leth", "Mern", "Nern", "Osk",
    "Peth", "Qek", "Resh", "Senth", "Trill",
    "Usk", "Vev", "Wesk", "Xesh", "Yirt", "Zerek"
]

func translate(sentence: String, latinToAurebesh: Bool) -> String {
    if latinToAurebesh {
        return sentence.uppercased().map { char in
            guard let idx = latin.firstIndex(of: String(char)) else { return String(char) }
            
            return aurebesh[idx]
        }.joined()
    } else {
        let separatedAurebesh = sentence.reduce(into: [String]()) { (result, character) in
            if character.isUppercase || character.isWhitespace || character.isNumber {
                result.append(String(character))
            } else {
                result[result.endIndex-1].append(character)
            }
        }
        
        return separatedAurebesh.map { word in
            guard let idx = aurebesh.firstIndex(of: word) else { return word }
            
            return latin[idx]
        }.joined()
    }
}

let translateAurebesh = translate(sentence: "May the Force be with you", latinToAurebesh: true)
print(translateAurebesh)
let translateLatin = translate(sentence: translateAurebesh, latinToAurebesh: false)
print(translateLatin)