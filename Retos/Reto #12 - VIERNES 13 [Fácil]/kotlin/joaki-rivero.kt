import java.time.LocalDate

fun main() {
    println(haveFriday13(3, 2023))
    println(haveFriday13(1, 2023))
}

fun haveFriday13(month: Int, year: Int): Boolean {
    if (month > 12 || month < 1) return false

    return LocalDate.of(year, month, 13).dayOfWeek.toString() == "FRIDAY"
}