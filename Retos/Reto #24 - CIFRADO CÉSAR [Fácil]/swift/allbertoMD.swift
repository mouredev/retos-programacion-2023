
import Foundation

let abc: [Character] = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

var text = """
 El sol brillaba en el cielo despejado mientras las aves revoloteaban entre los árboles. El aroma fresco de la hierba recién cortada llenaba el aire. Los niños jugaban en el parque, riendo y corriendo felices. En el centro de la ciudad, las calles estaban llenas de vida, con gente apresurada de un lado a otro. En los cafés, las personas disfrutaban de su taza de café matutina. Mientras tanto, en un rincón tranquilo de la biblioteca, un estudiante se sumergía en sus libros, absorbido por el conocimiento. El mundo seguía girando, lleno de momentos cotidianos que hacen que la vida sea maravillosa.
"""

func cesarCipher(transport: Int, text: String) {
    var textArray: [Character] = []

    let moveIndex = transport
    
    for i in text {
        textArray.append(i)
    }

    for n in 0..<textArray.count {
        var checkUppercase = false
        
        if textArray[n].isUppercase {
            checkUppercase = true
            textArray[n] = Character(textArray[n].lowercased())
        }
        for m in 0..<abc.count {
            if textArray[n] == abc[m] {
                if m >= (abc.count - moveIndex) {
                    textArray[n] = abc[(m - abc.count) + moveIndex]
                    break
                }
                textArray[n] = abc[m + moveIndex]
                break
            }
        }
        if checkUppercase {
            textArray[n] = Character(textArray[n].uppercased())
        }
    }

    var newText = ""
    for i in textArray {
        newText.append(i)
    }

    print(newText)
}

cesarCipher(transport: 3, text: text)
