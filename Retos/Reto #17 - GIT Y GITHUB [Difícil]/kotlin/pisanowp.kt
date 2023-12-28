import retrofit2.Call
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory
import retrofit2.http.GET

import java.time.*
import java.time.format.*


fun main() {

    /*
    * Reto #17 24/04/2023
    *
    * ¡Estoy de celebración! He publicado mi primer libro:
    * "Git y GitHub desde cero"
    * - Papel: mouredev.com/libro-git
    * - eBook: mouredev.com/ebook-git
    *
    * ¿Sabías que puedes leer información de Git y GitHub desde la gran
    * mayoría de lenguajes de programación?
    *
    * Crea un programa que lea los últimos 10 commits de este repositorio y muestre:
    * - Hash
    * - Autor
    * - Mensaje
    * - Fecha y hora
    *
    * Ejemplo de salida:
    * Commit 1 (el más reciente) | 12345A | MoureDev | Este es un commit | 24/04/2023 21:00
    *
    * Se permite utilizar librerías que nos faciliten esta tarea.
    *
    */


    /*
      Preparaciión registrar las dependencias.
      Para IntelliJ IDEA editar el fichero build.gradle.kts en el bloque dependencies añadir:

        // Retrofit
        implementation("com.squareup.retrofit2:retrofit:2.9.0")
        // Gson (To convert raw JSON to pretty JSON)
        implementation("com.squareup.retrofit2:converter-gson:2.9.0")



      Para este ejercicio he usado chatgpt para:

    * La creación de las Data Class que almacenan la respuesta, con el siguiente prompt.
        En kotlin, ¿puedes darme los data class necesarios para guardar el resultado json
        de la siguiente petición https://api.github.com/repos/mouredev/retos-programacion-2023/commits ?

    * Como las fechas son mi caballo de batalla, pues lo mismo para formatear la fecha
        De los datos recuperados tengo la siguiente fecha 2023-04-25T09:11:53Z,
        ¿puedes darme el código kotlin para mostrarla de la siguiente forma 25-04-2023 09:11 ?

     */

    getLastCommits()


}

fun getLastCommits(numCommits : Int = 10){

    val commits = GitHubClient.service.getCommits()
    val body = commits.execute().body()
    if (body != null) {
        var count = 0 // variable para contar el número de elementos iterados
        body.forEach {

            if (count < numCommits) {
                mostrarInfoCommit(it)
                count++
            } else {
                // si ya hemos iterado 10 elementos, salimos del bucle
                return@forEach
            }

        }

    } else {
        println("error al recuperar commits")

    }

}

fun mostrarInfoCommit(commit: Commit) {

    println("Hash : ${commit.sha} ")
    println("Autor : ${commit.commit.author.name}")
    println("Mensaje : ${commit.commit.message}")

    val fechaString = commit.commit.author.date

    // Convertir la cadena de fecha a un objeto LocalDateTime
    val fecha = LocalDateTime.parse(fechaString, DateTimeFormatter.ISO_DATE_TIME)

    // Crear un objeto DateTimeFormatter personalizado para el formato requerido
    val formatter = DateTimeFormatter.ofPattern("dd-MM-yyyy HH:mm")

    // Convertir la fecha a una cadena en el nuevo formato
    val fechaFormateada = fecha.format(formatter)

    println("Fecha y hora : ${fechaFormateada}")

    println("".padStart(50, '-'))

}

object GitHubClient {

    private val retrofit = Retrofit.Builder()
        .baseUrl("https://api.github.com/repos/mouredev/retos-programacion-2023/")
        .addConverterFactory(GsonConverterFactory.create())
        .build()

    val service: GitHubAPIService = retrofit.create(GitHubAPIService::class.java)

}

interface GitHubAPIService {

    @GET("commits")
    fun getCommits(): Call<List<Commit>>

}


data class Commit(
    val sha: String,
    val commit: CommitDetails,
    val author: AuthorDetails,
    val committer: CommitterDetails
)

data class CommitDetails(
    val message: String,
    val author: AuthorInfo,
    val committer: CommitterInfo
)

data class AuthorDetails(
    val login: String,
    val avatar_url: String
)

data class CommitterDetails(
    val login: String,
    val avatar_url: String
)

data class AuthorInfo(
    val name: String,
    val email: String,
    val date: String
)

data class CommitterInfo(
    val name: String,
    val email: String,
    val date: String
)
