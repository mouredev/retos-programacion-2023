import Foundation

print("\nIntroduce la palabra para comprobar si es heterograma:")
if let word = readLine() {
    let heterogram = isHeterogram(theWord: word)
    print(heterogram)
}

print("\nIntroduce la palabra para comprobar si es isograma:")
if let word = readLine() {
    let isogram = isIsogram(theWord: word)
    print(isogram)
}

print("\nIntroduce la palabra para comprobar si es pangrama:")
if let word = readLine() {
    let pangram = isPangram(theWord: word)
    print(pangram)
}




// Funcion Hetereograma
func isHeterogram(theWord word: String) -> Bool {
    var allCharacters: [Character] = []
    var lowerCharacter = ""
    var isHetereogram = true
    
    for character in word {
        lowerCharacter = character.lowercased()
        
        if allCharacters.contains(lowerCharacter) {
            isHetereogram = false
            break
        }
        allCharacters.append(Character(lowerCharacter))
        
        lowerCharacter.removeAll()
        
        if !allCharacters.isEmpty && character == " " {
            allCharacters.removeLast()
            
        }
    }
    if isHetereogram {
        print("\n\(word) - [√] Es hetereograma.")
        
        return isHetereogram
    } else {
        print("\n\(word) - [x] No es hetereograma.")
        
        return isHetereogram
    }
}


// Función Isograma.
func isIsogram(theWord word: String) -> Bool {
    var allCharacters: [Character] = []
    var lowerCharacter = ""
    var isIsogram = true
    
    for character in word {
        if character == " " {
            print("Un isograma no puede tener mas de una palabra.")
            isIsogram = false
            break
        }
        lowerCharacter = character.lowercased()
        
        if allCharacters.contains(character) {
            isIsogram = false
            break
        }
        allCharacters.append(Character(lowerCharacter))
        
        lowerCharacter.removeAll()
    }
    if isIsogram {
        print("\n\(word) - [√] Es Isograma.")
        
        return isIsogram
    } else {
        print("\n\(word) - [x] No es isograma")
        
        return isIsogram
    }
}


// Función Pangrama.
func isPangram(theWord word: String) -> Bool {
    var allCharacters: [Character] = []
    var lowerCharacter = ""
    var isPangram = true
    
    for character in word {
        lowerCharacter = character.lowercased()
        
        if allCharacters.contains(character) {
            allCharacters.removeAll { $0 == character }
        }
        
        allCharacters.append(Character(lowerCharacter))
        
        lowerCharacter.removeAll()
        
        if !allCharacters.isEmpty && character == " " {
            allCharacters.removeLast()
        }
    }
    if allCharacters.count == 26 {
        isPangram = true
        
        print("\n\(word) - [√] Es pangrama.")
        
        return isPangram
    } else {
        isPangram = false
        
        print("\n\(word) - [x] No es pangram.")
        
        return isPangram
    }
}

