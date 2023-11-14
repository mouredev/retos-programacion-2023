import org.json.JSONArray
import org.json.JSONObject
import java.net.URL

fun printLastCommits() {
    val repoURL = "https://api.github.com/repos/mouredev/retos-programacion-2023/commits?page=1&per_page=5"
    var jsonResponse = URL(repoURL).readText()
    val commitResponses = JSONArray(jsonResponse)

    commitResponses.forEachIndexed { index, commitResponse ->
        val hash = (commitResponse as JSONObject).getString("sha").substring(0, 7).uppercase()
        val commit = commitResponse.getJSONObject("commit")
        val message = commit.getString("message").replace("\n", " ")
        val author = commit.getJSONObject("author")
        val authorName = author.getString("name")
        val date = author.getString("date").dropLast(4).replace("T", " ")
        val formattedDate = "${date.substring(8,10)}/${date.substring(5,7)}/${date.substring(0,4)} ${date.substring(11)}"

        println("Commit ${index + 1} | $hash | $authorName | $message | $formattedDate")
    }
}

fun main() {
    printLastCommits()
}