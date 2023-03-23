fun main() {
    (0..100).forEach { _ -> println(random()) }
}

private fun random(): Int {
    return (System.nanoTime() % 101).toInt()
}
