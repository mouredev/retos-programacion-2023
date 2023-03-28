import java.time.LocalDate

private fun main() {
    println(friday13(2023, 3))
    println(friday13(2023, 1))
    println(friday13(2023, 13))
    println(friday13(-2023, 1))
    println(friday13(2023, 0))
}

fun friday13(year: Int, month: Int): Boolean {
    return try {
        LocalDate.of(year, month, 13).dayOfWeek.value == 5
    } catch (e: Exception) {
        false
    }
}
