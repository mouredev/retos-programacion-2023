import java.time.Month
import java.util.*

fun hasFriday13(year: Int, month: Month): Boolean {
    val a = (14 - month.ordinal + 1) / 12
    val y = year - a
    val m = month.ordinal + 1 + 12 * a - 2
    val d = (13 + y + y/4 - y/100 + y/400 + (31 * m) / 12) % 7
    return d == Calendar.FRIDAY - 1
}

fun main() {
    println(hasFriday13(2022, Month.JANUARY))
    println(hasFriday13(2000, Month.OCTOBER))
    println(hasFriday13(2022, Month.MAY))
    println(hasFriday13(2023, Month.OCTOBER))
    println(hasFriday13(2024, Month.SEPTEMBER))
    println(hasFriday13(2024, Month.DECEMBER))
}