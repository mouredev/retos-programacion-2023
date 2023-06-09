fun drawStaircase(steps: Int) {
    if (steps > 0) {
        println(" ".repeat(steps * 2) + "_")
        for (index in steps - 1 downTo 0) {
            println(" ".repeat(index * 2) + "_|")
        }
    } else if (steps < 0) {
        println("_")
        for (index in 0 until -steps) {
            println(" ".repeat(index * 2 + 1) + "|_")
        }
    } else {
        println("__")
    }
}

fun main() {
    drawStaircase(4)
    drawStaircase(7)
    drawStaircase(-5)
    drawStaircase(-8)
    drawStaircase(0)
}
