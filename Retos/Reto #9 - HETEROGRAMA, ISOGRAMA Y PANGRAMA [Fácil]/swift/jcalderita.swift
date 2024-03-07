import Foundation

let characters = Set("abcdefghijklmnopqrstuvwxyz")

func transformSentence(_ sentence: String) -> String {
    sentence.trimmingCharacters(in: .whitespaces).lowercased()
}

func isHeterogram(_ sentence: String) -> Bool {
    let compare = transformSentence(sentence)
    return compare.count == Set(compare).count
}

func isIsogram(_ sentence: String) -> Bool {
    let compare = transformSentence(sentence)
    return compare.count != Set(compare).count
}

func isPangram(_ sentence: String) -> Bool {
    let compare = transformSentence(sentence)
    return characters.subtracting(compare).isEmpty
}

print("Yuxtaponer es heterograma: \(isHeterogram("yuxtaponer"))")
print("Centrifugado es heterograma: \(isHeterogram("centrifugado"))")
print("Luteranismo es heterograma: \(isHeterogram("luteranismo"))")
print("Adulterinos es heterograma: \(isHeterogram("adulterinos"))")
print("Hiperblanduzcos es heterograma: \(isHeterogram("hiperblanduzcos"))")
print("Acondicionar es heterograma: \(isHeterogram("acondicionar"))")

print("\nAcondicionar es isograma: \(isIsogram("acondicionar"))")
print("Escritura es isograma: \(isIsogram("escritura"))")
print("Intestinos es isograma: \(isIsogram("intestinos"))")
print("Papelera es isograma: \(isIsogram("papelera"))")
print("Hiperblanduzcos es isograma: \(isIsogram("hiperblanduzcos"))")

print("\n'Benjamín pidió una bebida de kiwi y fresa. Noé, sin vergüenza, la más exquisita champaña del menú' es pangrama: \(isPangram("Benjamín pidió una bebida de kiwi y fresa. Noé, sin vergüenza, la más exquisita champaña del menú"))")
