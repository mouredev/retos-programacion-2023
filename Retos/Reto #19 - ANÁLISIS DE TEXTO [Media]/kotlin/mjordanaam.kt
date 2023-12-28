/*
 * Crea un programa que analice texto y obtenga:
 * - Número total de palabras.
 * - Longitud media de las palabras.
 * - Número de oraciones del texto (cada vez que aparecen un punto).
 * - Encuentre la palabra más larga.
 *
 * Todo esto utilizando un único bucle.
 */

fun analyzeText(text: String) {
    var sentences: Int = 0
    var words = arrayOf<String>()
    var aux: String = ""
    var nwords: Int = 0
    var length: Int = 0
    var longest = hashMapOf<Int, Array<String>>(0 to arrayOf<String>())
    
    for (letter in text) {
        val regex1 = Regex("[.?!]+")
        val regex2 = Regex("[¿|:()/@%$,]+")
        if (regex1.matches(letter.toString())) {
            sentences++
            words += aux
            length += aux.length
            nwords++
            
            if (aux.length > longest.keys.first()) {
                longest = hashMapOf(aux.length to arrayOf<String>(aux))
            } else if (aux.length == longest.keys.first()) {           
                longest[aux.length] = longest.getOrDefault(aux.length, emptyArray()) + aux
            }
            
            aux = ""
        }else if (letter == ' ') {
            if (aux != "") {
                words += aux
                length += aux.length
                nwords++

                if (aux.length > longest.keys.first()) {
                    longest = hashMapOf(aux.length to arrayOf(aux))
                } else if (aux.length == longest.keys.first()) {
                    longest[aux.length] = longest.getOrDefault(aux.length, emptyArray()) + aux
                }
                aux = ""
            }
        }else if (regex2.matches(letter.toString())){
            
        }else {
            aux += letter
        }
    }
    
    var average = length/nwords
    
    println("> Total Words = $nwords")
    println("> Average length = $average")
    println("> Number of sentences = $sentences")
    println("> Longest word/words (${longest.keys.first()} letters) = ${longest.get(longest.keys.first()).contentToString()}")
    println()

}

fun main() {
    var text: String = "Hello. World!"
    
    analyzeText(text)


    text = "Crea un programa que analice texto y obtenga:." + 
            "Número total de palabras." +
            "Longitud media de las palabras." +
            "Número de oraciones del texto (cada vez que aparecen un punto)." +
            "Encuentre la palabra más larga." + 
            "Todo esto utilizando un único bucle."
    
    analyzeText(text)

    text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis condimentum mauris non enim mollis dictum. In " +
           "feugiat ut justo in vulputate. Aliquam erat volutpat. Vivamus porttitor commodo felis, sed gravida eros " +
           "fermentum non. Mauris sagittis id neque sit amet ullamcorper. Sed eu pretium ex, ut ornare quam. Maecenas " +
           "consectetur elit a nisi maximus, et vehicula lorem finibus. Duis sapien justo, placerat in vestibulum a, " +
           "vestibulum non lacus. Sed egestas, nisi."
    
    analyzeText(text)

}