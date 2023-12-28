import Foundation

func caesarCipher(text: String, decrypt: Bool = false, shift: Int = 3) {
    let alphabet = Array("abcdefghijklmnopqrstuvwxyz")
    var caesarText = ""
    
    for value in text.lowercased() {
        if let index = alphabet.firstIndex(of: value) {
            let newIndex = ((index + (decrypt ? -shift: shift) + alphabet.count) % alphabet.count)
            caesarText.append(alphabet[newIndex])
        } else {
            caesarText += value.description
        }
        
    }
    print(caesarText)
}

caesarCipher(text: "Paco")
caesarCipher(text: "sdfr", decrypt: true)
caesarCipher(text: "estoy cansado de vivir en zaragoza")
caesarCipher(text: "hvwrb fdqvdgr gh ylylu hq cdudjrcd", decrypt: true)