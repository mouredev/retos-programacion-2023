import java.nio.file.Files
import java.nio.file.Paths

fun main() {
    val users = mutableMapOf("mouredev" to 0)
    val dir = "/Users/diegosanchez/Developer/retos-programacion-2023/Retos"
    var username: String

    Files.walk(Paths.get(dir)).use { paths ->
        paths.filter { Files.isRegularFile(it) }
                .forEach {
                    username = it.fileName.toString().split(".").first()

                    if (users.contains(username)) {
                        val amount: Int? = users[username]
                        if (amount != null) {
                            users[username] = amount + 1
                        }
                    } else {
                        users.put(username, 1)
                    }
                }
    }

    println("> Participaciones: ${users.count()}")
    println("> Correcciones enviadas: ${getRequests(users)}")
    println()
    printMap(users)
}

fun printMap(users: MutableMap<String, Int>) {
    val sortedUsers = users.toList().sortedByDescending { (_, amount) -> amount }.toMap()

    for ((user, amount) in sortedUsers) {
        println("$user = $amount")
    }
}

fun getRequests(users: MutableMap<String, Int>): Int {
    var requests = 0

    for ((user, amount) in users) {

        requests += amount
    }

    return requests
}