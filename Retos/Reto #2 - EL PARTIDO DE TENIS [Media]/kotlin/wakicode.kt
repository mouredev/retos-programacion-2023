
fun main(args: Array<String>) {
    /**
     * @ Wakicode
     * Una versión más escalable de un Set de Tenis.
     */
    TennisSet.getPointsFromSet(list = listOf("P1", "P2", "P1", "P2", "P1", "P2", "P1", "P2", "P2", "P1", "P2", "P2"))
    TennisSet.getPointsFromSet(list = listOf("P1", "P2", "P1", "P2", "P1", "P1"))
    TennisSet.play()
}

/**
 * Clase de puntuaciones
 */
data class Score(
    val index: Int, val score: String
) {
    companion object {
        val values = mutableListOf(
            Score(0, "Love"), Score(1, "15"), Score(2, "30"), Score(3, "40"), Score(4, "Ventaja"), Score(5, "Ha Ganado")
        )
    }
}

/**
 * Clase que identifica a un jugador
 */
data class Player(val name: String = "") {
    var score: Int = 0

    fun play(point: Int) {
        score += point
    }

    fun scoreToString(): String = Score.values.firstOrNull { it.index == score }!!.score

    val isWinner
        get() = score == 5

    val isAdvantage
        get() = score == 4

    val thirtyOrAdvantage
        get() = score == 3 || score == 4

    override fun toString(): String = name
}

/**
 * Clase que define un Set
 * Contiene 2 métodos estáticos:
 * play.- Inicia una nueva partida desde el teclado
 * getPointsFromSet.- Muestra en pantalla desde una lista el resultado de un set
 */
class TennisSet(
    name1: String,
    name2: String,
    ) {

    private val mySet: MutableList<Player> = mutableListOf()
    private val p1: Player = Player(name1)
    private val p2: Player = Player(name2)
    private val isDeuce: Boolean
        get() = p1.score == p2.score && p1.thirtyOrAdvantage
    private val isAdvantage
        get() = p1.isAdvantage == !p2.isAdvantage

    /**
     * Función que solicita entrada desde el teclado
     * @param p: String Devuelve true si la entrada es correcta
     */
    private fun ballWin(p: String): Boolean {
        if (p == "1" || p.lowercase() == p1.name.lowercase()) ballWin(p1)
        else if (p == "2" || p.lowercase() == p2.name.lowercase()) ballWin(p2)
        return p == "1" || p == "2" || p.lowercase() == p1.name.lowercase() || p.lowercase() == p2.name.lowercase()
    }

    /**
     * función que asigna el punto al ganador de la bola
     */
    private fun ballWin(player: Player) {
        val point = if (!isDeuce && player.score == 3 && !isAdvantage) 2 else 1
        player.play(point)

        if (isDeuce) {
            p1.score = 3
            p2.score = 3
        }
        mySet.add(player)

    }

    /**
     * función que determina si existe un ganador
     */
    private fun thereIsWinner() = p1.isWinner || p2.isWinner

    /**
     * Punción que devuelve la puntuación actual
     */
    private fun score(): String {
        return when {
            isDeuce -> "Deuce"
            p1.isWinner || p1.isAdvantage -> "${p1.scoreToString()} P1"
            p2.isWinner || p2.isAdvantage -> "${p2.scoreToString()} P2"
            else -> "${p1.scoreToString()} - ${p2.scoreToString()}"
        }
    }

    companion object {
        /**
         * Función que muestra el resultado de un set en función de una lista
         * @param list lista de elementos
         */
        fun getPointsFromSet(list: List<String> = listOf()) {
            val players = list.distinct()
            if (players.count() != 2)
            {
                println("La lista $list no es correcta. Compruebe el número de jugadores")
                return
            }

            val set = TennisSet(players.first(), players.last())
            list.forEach {
                set.ballWin(it)
                println(set.score())
            }
            if (!set.thereIsWinner()) println("La lista no es correcta, el set no ha finalizado")
        }

        fun play() {
            val set = TennisSet("P1", "P2")
            println("${"*".repeat(22)}\n* Nuevo set de Tenis *\n${"*".repeat(22)}")
            do {
                println("Introduzca el jugador ganador (1 -> P1 - 2 -> P2)")
                val input = readln()
                if (set.ballWin(input)) {
                    println(set.score())
                }
            } while (!set.thereIsWinner())

            println("Fin del set")
        }
    }
}