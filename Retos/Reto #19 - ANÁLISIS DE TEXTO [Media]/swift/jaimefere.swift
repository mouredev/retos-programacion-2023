import Foundation

func analyze(text: String) {
    let symbols = " .,:;-¡!¿?()[]\"\t\n"
    var wordLengths: [Int] = []
    var pointsCounter = 0
    var largestWord = ""
    var currentWord = ""

    text.forEach { char in
        if(symbols.contains(String(char))) {
            if(char == ".") {
                pointsCounter += 1
            }
            if(!currentWord.isEmpty) {
                if(currentWord.count > wordLengths.max() ?? 0) {
                    largestWord = currentWord
                }
                wordLengths.append(currentWord.count)
                currentWord = ""
            }
        } else {
            currentWord.append(char)
        }
    }

    print("Número de palabras: \(wordLengths.count)")
    print("Longitud media de las palabras: \(Int(wordLengths.reduce(0, +) / wordLengths.count))")
    print("Número de oraciones: \(pointsCounter)")
    print("Palabra más larga: \(largestWord)\n")
}

analyze(text: "En un lugar de la Mancha, de cuyo nombre no quiero acordarme, no ha mucho tiempo que vivía un hidalgo de los de lanza en astillero, adarga antigua, rocín flaco y galgo corredor. Una olla de algo más vaca que carnero, salpicón las más noches, duelos y quebrantos los sábados, lantejas los viernes, algún palomino de añadidura los domingos, consumían las tres partes de su hacienda.")
analyze(text: "Find out exactly how many sentences are in your text content using this online sentence counter. This sentence counting tool will also give you basic information on the number of words and characters in your text.\nThis tool will automatically figure out the number of sentences, words, and characters that you have in most any type of text content. The text information you want to analyze can be many formats. This sentence counter can handle anything from a single string of text or to very long content composed of numerous text paragraphs separated by multiple line breaks.\nThe text box may look small but it can handle text content with thousands upon thousands of words very easily and quickly. It's a ideal sentence calculator for short stories, long articles, and even some books.")
