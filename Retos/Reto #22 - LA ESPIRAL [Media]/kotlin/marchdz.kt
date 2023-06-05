fun drawSpiral(squareSideSize: Int) {
    if (squareSideSize > 0) {
        val firstHalfOfTheSquare = if (squareSideSize % 2 == 0) squareSideSize / 2 else squareSideSize / 2 + 1
        println("═".repeat(squareSideSize - 1) + "╗")
        (1 until firstHalfOfTheSquare).forEach { row ->
            println("║".repeat(row - 1) + "╔" + "═".repeat(squareSideSize - 2 * row - 1) + "╗" + "║".repeat(row))
        }
        (firstHalfOfTheSquare until squareSideSize).forEach { row ->
            println("║".repeat(squareSideSize - row - 1) + "╚" + "═".repeat(2 * row - squareSideSize) + "╝" +
                    "║".repeat(squareSideSize - row - 1))
        }
    }
}

fun main() {
    drawSpiral(5)
}