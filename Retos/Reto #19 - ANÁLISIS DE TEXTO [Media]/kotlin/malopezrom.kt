/*
 * Crea un programa que analice texto y obtenga:
 * - Número total de palabras.
 * - Longitud media de las palabras.
 * - Número de oraciones del texto (cada vez que aparecen un punto).
 * - Encuentre la palabra más larga.
 *
 * Todo esto utilizando un único bucle.
 */

fun main(){
    val text ="""
        la luna asoma: federico garcía lorca
                       cuando sale la luna
                       se pierden las campanas
                       y aparecen las sendas
                       impenetrables.
                       cuando sale la luna,
                       el mar cubre la tierra
                       y el corazón se siente
                       isla en el infinito.
                       nadie come naranjas
                       bajo la luna llena.
                       es preciso comer
                       fruta verde y helada.
                       cuando sale la luna
                       de cien rostros iguales,
                       la moneda de plata
                       solloza en el bolsillo.
        
    """.trimIndent()

    analizeText(text)
}

/**
 * Función que analiza un texto y obtiene:
 * - Número total de palabras.
 * - Longitud media de las palabras.
 * - Número de oraciones del texto (cada vez que aparecen un punto).
 * - Palabra más larga.
 */
fun analizeText(text:String){
    val wordsRegex = Regex("\\p{L}+[\\p{L}',@!.-]*")
    val sentenceRegex = Regex("\\p{L}+[\\p{L}',@!.-]*\\.+\$")
    val words = text.replace("\n"," ").split(" ")
    var sentences =0
    var longestWord= ""
    var length=0
    var size = 0


    words.forEach {
        if(wordsRegex.matches(it)){
            size++
            if(sentenceRegex.matches(it)){
                sentences++
            }
        }
        length += it.length
        if(it.length > longestWord.length){
            longestWord= it
        }

    }

    val averageLength = length/size

    println("Total de palabras: ${size}")
    println("Longitud media: $averageLength")
    println("Numero de frases: $sentences")
    println("Palabra mas larga: $longestWord(${longestWord.length})")



}

