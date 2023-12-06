package EjercicioKotlin.Mouredev

import java.time.LocalDate

class Reto12 {
    var month = 0
    var year = 0

    init {
        readDate()
        isFriday13()
    }

    private fun readDate() {
        print("Enter the number of the month:")
        month = readLine()!!.toInt()

        print("Enter year:")
        year = readLine()!!.toInt()
    }

    private fun isFriday13() {
        val date = LocalDate.of(year, month, 13)

        if (date.dayOfWeek.toString() == "FRIDAY") 
            println("The 13th is Friday")
        else 
            println("The 13th is not Friday")
    }
}

fun main() {
    Reto12()
}
