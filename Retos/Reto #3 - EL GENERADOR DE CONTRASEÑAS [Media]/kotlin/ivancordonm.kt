import java.util.*

fun main() {

    val reader = Scanner(System.`in`)

    fun question(q: String): Boolean {
        var response = "X"
        while (response != "N" && response != "S") {
            print(q)
            response = reader.next().uppercase(Locale.getDefault())
        }
        return response == "S"
    }

    var len = 0
    while (len < 8 || len > 16) {
        print("Longitud: Entre 8 y 16: ")
        len = reader.nextInt()
    }

    val withCapitals = question("¿Incluir mayúsculas? (S/N): ")
    val withNumbers = question("¿Incluir números? (S/N): ")
    val withSymbols = question("¿Incluir símbolos? (S/N): ")


    var chars = ('a'..'z').toList()
    val capitals = ('A'..'Z').toList()
    val numbers = ('0'..'9').toList()
    val symbols = listOf(':', '.', ';', '_', '-', '$', '%', '&')

    val message = buildString {
        append("Contraseña de longitud $len ")
        if (withCapitals) {
            chars = chars + capitals
            append("que incluye mayúsculas ")
        }
        if (withNumbers) {
            chars = chars + numbers
            append("que incluye números ")
        }
        if (withSymbols) {
            chars = chars + symbols
            append("que incluye símbolos ")
        }
        append(": ")
    }

    val password = (1..len).map { chars[(0..chars.lastIndex).random()] }.joinToString("")
    println("$message $password")

}
