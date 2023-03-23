import SwiftUI

func transleet(_ text: String) -> String {
    let leetAlphabet = ["A" : "4", "B" : "I3", "C" : "[", "D" : ")", "E" : "3", "F" : "|=", "G" : "6", "H" : "#", "I" : "1", "J" : ",_|", "K" : ">|", "L" : "1", "M" : "/\\/\\", "N" : "^/", "O" : "0", "P" : "|*", "Q" : "(_,)", "R" : "I2", "S" : "5", "T" : "7", "U" : "(_)", "V" : "\\/", "W" : "\\/\\/", "X" : "><", "Y" : "j", "Z" : "2", "1" : "L", "2" : "R", "3" : "E", "4" : "A", "5" : "S", "6" : "b", "7" : "T", "8" : "B", "9" : "g", "0" : "o"]
    let cleanedText = text.folding(options: .diacriticInsensitive, locale: .current).uppercased()
    var result = ""

    cleanedText.forEach { char in
        result += leetAlphabet.keys.contains(String(char)) ? leetAlphabet[String(char)]! : String(char)
    }

    return result
}

print(transleet("¿Estás mirándolo?"))   // ¿357á5 /\/\1I2á|\||)010?
print(transleet("Mira cómo escribo leet, ¿tú lo puedes hacer así de bien?"))   // /\/\1I24 [ó/\/\0 35[I21I30 1337, ¿7ú 10 |>(_)3|)35 #4[3I2 45í |)3 I313|\|?
print(transleet("Esto es la Wikipedia, la enciclopedia libre"))   // 3570 35 14 \/\/1|<1|>3|)14, 14 3|\|[1[10|>3|)14 11I3I23
print(transleet("Esto es Leet Speak, ¿sabes hacerlo?"))   // 3570 35 1337 5|>34|<, ¿54I335 #4[3I210?
print(transleet("Puedes usar algunas letras si te resulta demasiado difícil"))    // |>(_)3|)35 (_)54I2 416(_)|\|45 137I245 51 73 I235(_)174 |)3/\/\4514|)0 |)1phí[11
