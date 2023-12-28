fun main() {
    val jugada1 = listOf(Pair("🗿", "🦎"), Pair("🦎", "🖖"), Pair("🖖", "✂️"), Pair("✂️", "📄"))
    val jugada2 = listOf(Pair("✂️", "🖖"), Pair("🦎", "🗿"), Pair("🗿", "📄"), Pair("🖖", "🦎"))
    val jugada3 = listOf(Pair("🗿", "🗿"), Pair("🖖", "✂️"), Pair("🖖", "📄"), Pair("✂️", "✂️"))
    println(reto(jugada1))
    println(reto(jugada2))
    println(reto(jugada3))
}

fun reto(moves: List<Pair<String, String>>): String {
    val puntuacion = arrayOf(0, 0)
    val signos = mapOf(
        "🗿" to setOf("✂️", "🦎"),
        "📄" to setOf("🗿", "🖖"),
        "✂️" to setOf("📄", "🦎"),
        "🦎" to setOf("📄", "🖖"),
        "🖖" to setOf("✂️", "🗿")
    )
    moves.forEach {
        if (it.first == it.second) return "Empate"
        if (signos[it.first]!!.contains(it.second)) puntuacion[0]++
        else puntuacion[1]++
    }
    return if (puntuacion[0] > puntuacion[1]) "Jugador 1" else "Jugador 2"
}

