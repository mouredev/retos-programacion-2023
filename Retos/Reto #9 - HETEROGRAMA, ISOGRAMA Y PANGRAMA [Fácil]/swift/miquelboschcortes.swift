//  Created by Miquel Bosch

/*
 * Crea 3 funciones, cada una encargada de detectar si una cadena de
 * texto es un heterograma, un isograma o un pangrama.
 * - Debes buscar la definición de cada uno de estos términos.
 
 - Heterogram: Word, phrase or sentence all the letter only occur once.
 - Isogram: Is a word with no letters repeated within the word.
 - Pangram: A sentence that contains every letter of the alphabet, if possible with each letter only being used once
 */

enum Alphabet: String {
    case english = "abcdefghijklmnopqrstuvwxyz"
    case spanish = "abcdefghijklñmnopqrstuvwxyz"
}

func isAnHeterogram(string: String) -> Bool {
    let stringWithoutSpaces = string.replacingOccurrences(of: " ", with: "")
    return Set(stringWithoutSpaces.lowercased()).count == stringWithoutSpaces.count
}

func isAnIsogram(string: String) -> Bool {
    return Set(string.lowercased()).count == string.count && string.components(separatedBy: .whitespacesAndNewlines).filter({ !$0.isEmpty }).count <= 1
}

func isAPangram(string: String, alphabet: Alphabet) -> Bool {
    var (alphabetSet, phraseSet) = (Set(alphabet.rawValue), Set(string.lowercased()))
    return  alphabetSet.subtracting(phraseSet).count == 0
}

isAnHeterogram(string: "The big dwarf only jumps")
isAnIsogram(string: "table")
isAPangram(string: "The quick brown fox jumps over a lazy dog", alphabet: .english)
isAPangram(string: "Fabio me exige, sin tapujos, que añada cerveza al whisky", alphabet: .spanish)

