import UIKit

extension String {
    static let aurebeshDic: [String: String] = [
        "A": "Aurek", "B": "Besh", "C":"Cresh", "D": "Dorn", "E": "Esk", "F": "Forn", "G": "Grek",
        "H": "Herf", "I": "Isk", "J": "Jenth", "K": "Krill", "L": "Leth", "M": "Mern", "N": "Nern",
        "O": "Osk", "P": "Peth", "Q": "Qek", "R": "Resh", "S": "Senth", "T": "Trill", "U": "Usk",
        "V": "Vev", "W": "Wesk", "X": "Xesh", "Y": "Yirt", "Z": "Zerek", " " : " ", "1": "1",
        "2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7", "8": "8", "9": "9", "0": "0"
    ]
    
    static let spanishDic: [String : String] = [
        "Aurek": "A", "Besh": "B", "Cresh": "C", "Dorn": "D", "Esk": "E", "Forn": "F", "Grek": "G",
        "Herf": "H", "Isk": "I", "Jenth": "J", "Krill": "K", "Leth": "L", "Mern": "M", "Nern": "N",
        "Osk": "O", "Peth": "P", "Qek": "Q", "Resh": "R", "Senth": "S", "Trill": "T", "Usk": "U",
        "Vev": "V", "Wesk": "W", "Xesh": "X", "Yirt": "Y", "Zerek": "Z", " ": " ", "1": "1",
        "2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7", "8": "8", "9": "9", "0": "0"
    ]
    
    func toSpanish() -> String {
        var result: String = self
        for key in Self.spanishDic.keys {
            if let value: String = Self.spanishDic[key] {
                result = result.replacingOccurrences(of: key, with: value)
            }
        }
        return result
    }
    
    func toAurebesh() -> String {
        var result: String = ""
        for char in Array(self.uppercased()) {
            let key: String = String(char)
            if let value: String = Self.aurebeshDic[key] {
                result = result + value
            }
        }
        return result
    }
}

print("hola a todos".toAurebesh())
print("HerfOskLethAurek Aurek TrillOskDornOskSenth".toSpanish())
