fun triforce(rows: Int) {
    val triangle = mutableListOf<String>()
    for (row in 1..rows) {
        val asterisks = "*".repeat(2 * row - 1)
        val spaces = " ".repeat((2 * rows - asterisks.length) / 2)
        triangle.add("$spaces$asterisks$spaces")
    }
    triangle.forEach { row -> println(row.padStart((1.5 * row.length + 1).toInt())) }
    triangle.forEach { row -> println("$row $row") }
}

fun main() {
    triforce(2)
}