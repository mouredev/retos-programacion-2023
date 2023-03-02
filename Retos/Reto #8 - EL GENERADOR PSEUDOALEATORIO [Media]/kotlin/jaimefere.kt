import sun.util.calendar.CalendarUtils.mod
import java.util.*
import kotlin.math.max
import kotlin.math.pow

private enum class Operations {
    MULTIPLICATION, POW, ADDITION
}

private fun generateRandomNumber(): Int {
    val now = Calendar.getInstance().timeInMillis.toString()
    val milli = Integer.parseInt(now[now.length - 1].toString())
    var operationsResult = 0
    (1..now.length).forEach { index ->
        val digit = Integer.parseInt(now[index - 1].toString())
        operationsResult +=
            when(Operations.values()[mod(digit, Operations.values().size)]) {
                Operations.ADDITION -> digit + milli + index
                Operations.MULTIPLICATION -> digit * milli * index
                Operations.POW -> max(digit, max(milli, index)).toDouble().pow(4).toInt()
            }
    }
    return mod(operationsResult, 100)
}

fun main() {
    println(generateRandomNumber())
}