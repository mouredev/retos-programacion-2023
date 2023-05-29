import com.google.gson.Gson
import java.net.HttpURLConnection
import java.net.URL

data class RickAndMortyCharacter(
    val id: Int,
    val name: String,
    val status: String,
    val species: String,
    val type: String,
    val gender: String
)

fun main() {
    val apiUrl = "https://rickandmortyapi.com/api/character/2"
    val connection = URL(apiUrl).openConnection() as HttpURLConnection
    connection.connect()

    val statusCode = connection.responseCode
    if (statusCode == HttpURLConnection.HTTP_OK) {
        val response = connection.inputStream.bufferedReader().readText()
        val gson = Gson()
        val rick = gson.fromJson(response, RickAndMortyCharacter::class.java)

        println("Rick and Morty character:")
        println("- ID: ${rick.id}")
        println("- Name: ${rick.name}")
        println("- Status: ${rick.status}")
        println("- Species: ${rick.species}")
        println("- Type: ${rick.type}")
        println("- Gender: ${rick.gender}")
    } else {
        println("Error al hacer la petición, código de estado: $statusCode")
    }
}
