import com.google.gson.Gson
import kotlinx.coroutines.runBlocking
import java.net.HttpURLConnection
import java.net.URL
import java.text.SimpleDateFormat
import java.util.*


/**
 * Función principal
 */
fun main(){
    val repositoryName = "mouredev/retos-programacion-2023"
    val github = GitHub(repositoryName)
    val commits = runBlocking  { github.getCommits(10) }
    github.printCommits(commits)
}


/**
 * Clase que representa el autor de un commit
 */

data class Author(
        val name: String,
        val date: String,
        val email: String
)

/**
 * Clase que representa el detalle de un commit
 */
data class CommitDetail(
        val author: Author,
        val message: String,
)

/**
 * Clase que representa un commit
 */
data class Commit(
        val sha: String,
        val commit: CommitDetail
)

/**
 * Clase para manejar la API de GitHub
 * @param repositoryName Nombre del repositorio
 */
class GitHub(val repositoryName:String){
    private val GIT_HUB_URL = "https://api.github.com/repos/"


    /**
     * Método para leer los commits de un repositorio
     * @param commits Número de commits a leer
     * @returns Array de commits
     */
    suspend fun getCommits(commits:Int): List<Commit> {
        val url = "${GIT_HUB_URL}${repositoryName}/commits?per_page=${commits}"

        val values: Array<Commit> by lazy {
            val gitHubAPIURL = URL(url)
            val gitHubConnection = gitHubAPIURL.openConnection() as HttpURLConnection
            try {
                val responseText = gitHubConnection.inputStream.bufferedReader().readText()
                Gson().fromJson(responseText, Array<Commit>::class.java)
            } catch (e: Exception) {
                throw e
            } finally {
                gitHubConnection.disconnect()
            }
        }

        return values.toList()
    }
    /**
     * Método para imprimir los commits
     * @param commits Array de commits a imprimir
     */
    fun printCommits(commits:List<Commit>){
        commits.forEachIndexed { index, commit ->
            val hash = commit.sha
            val (name,date,_) = commit.commit.author
            val message = commit.commit.message

            val formattedDate = SimpleDateFormat("yyyy-MM-dd'T'HH:mm:ss'Z'", Locale.getDefault())
                    .parse(date)?.let {
                        SimpleDateFormat("yyyy-MM-dd HH:mm:ss", Locale.getDefault()).format(it)
                    } ?: ""
            println("Commit ${index + 1} | ${hash.red()} | ${name.blue()} | ${message.cyan()} | ${formattedDate.yellow()} |")

        }
    }

}


/**
 * Extensiones para colorear la salida
 */
fun String.red() = "\u001B[31m$this\u001B[0m"
fun String.blue() = "\u001B[34m$this\u001B[0m"
fun String.cyan() = "\u001B[36m$this\u001B[0m"
fun String.yellow() = "\u001B[33m$this\u001B[0m"