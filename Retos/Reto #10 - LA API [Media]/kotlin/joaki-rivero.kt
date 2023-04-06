import java.net.URL

/*
 * Como normalmente hacemos el ejercicio en un fichero "script" único
 * y sacando las cosas por consola he realizado el ejercicio sin usar librerías externas
 * (para añadirle algo de complejidad) y haciendo el mapeado manualmente
 */

data class AnimechanResponse(var anime: String, var character: String, var quote: String)

fun main() {
    val json = URL("https://animechan.vercel.app/api/random").readText()

    val animeIndex = json.indexOf("\"anime\":") + 8
    val animeFinIndex = json.indexOf(",", animeIndex)
    val anime = json.substring(animeIndex, animeFinIndex).replace("\"", "")

    val characterIndex = json.indexOf("\"character\":") + 12
    val characterFinIndex = json.indexOf(",", characterIndex)
    val character = json.substring(characterIndex, characterFinIndex).replace("\"", "")

    val quoteIndex = json.indexOf("\"quote\":") + 8
    val quoteFinIndex = json.indexOf("}", quoteIndex)
    val quote = json.substring(quoteIndex, quoteFinIndex).replace("\"", "")

    val quoteObject = AnimechanResponse(anime, character, quote)

    println("Anime: ${quoteObject.anime}")
    println("Personaje: ${quoteObject.character}")
    println("Cita: ${quoteObject.quote}")
}