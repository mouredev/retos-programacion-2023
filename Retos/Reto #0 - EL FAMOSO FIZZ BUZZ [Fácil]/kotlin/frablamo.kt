fun main() {
    (1..100).forEach { println(it.toFizzBuzz()) }
}

private fun Int.toFizzBuzz(): String =
        when {
            isFizz(this) && isBuzz(this) -> "fizzbuzz"
            isFizz(this) -> "fizz"
            isBuzz(this) -> "buzz"
            else -> this.toString()
        }

private fun isFizz(value: Int): Boolean = value % 3 == 0
private fun isBuzz(value: Int): Boolean = value % 5 == 0


