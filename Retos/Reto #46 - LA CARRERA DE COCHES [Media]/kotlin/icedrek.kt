/*
 * Crea un programa que simule la competición de dos coches en una pista.
 * - Los dos coches estarán representados por 🚙 y 🚗. Y la meta por 🏁.
 * - Cada pista tendrá entre 1 y 3 árboles 🌲 colocados de forma aleatoria.
 * - Las dos pistas tendrán una longitud configurable de guiones bajos "_".
 * - Los coches comenzarán en la parte derecha de las pistas. Ejemplo:
 *   🏁____🌲_____🚙
 *   🏁_🌲____🌲___🚗
 *
 * El juego se desarrolla por turnos de forma automática, y cada segundo
 * se realiza una acción sobre los coches (moviéndose a la vez), hasta que
 * uno de ellos (o los dos a la vez) llega a la meta.
 * - Acciones:
 *   - Avanzar entre 1 a 3 posiciones hacia la meta.
 *   - Si al avanzar, el coche finaliza en la posición de un árbol,
 *     se muestra 💥 y no avanza durante un turno.
 *   - Cada turno se imprimen las pistas y sus elementos.
 *   - Cuando la carrera finalice, se muestra el coche ganador o el empate.
 */

import kotlin.random.Random


fun main() {
    val circuitSize = Random.nextInt(10, 20)

    val player1 = Player(circuitSize + 1, "🚙")
    val player2 = Player(circuitSize + 1, "🚗")

    val circuit1 = makeCircuit(circuitSize, player1.icon)
    val circuit2 = makeCircuit(circuitSize, player2.icon)

    race(circuit1, circuit2, player1, player2)
}


class Player(
    var position: Int,
    val icon: String,
    var crash: Boolean = false,
) {
    fun move(movement: Int) {
        position -= movement

        if (position < 0) {
            position = 0
        }
    }
}

fun makeCircuit(circuitSize: Int, car: String): MutableList<String> {
    val circuit = mutableListOf("🏁")
    var treeCounter = 0

    for (i in 1..circuitSize) {
        val stretch = Random.nextInt(0, 100)

        if (stretch >= 90) {
            treeCounter += 1
            if (treeCounter > 3) {
                circuit.add("_")
            } else {
                circuit.add("🌲")
            }
        } else {
            circuit.add("_")
        }
    }

    if (treeCounter == 0) {
        circuit[circuit.size - 1] = "🌲"
    }

    circuit.add(car)

    return circuit
}

fun race(
    circuit1: MutableList<String>,
    circuit2: MutableList<String>,
    player1: Player,
    player2: Player,
) {
    println("\nCOMIENZA LA CARRERA!!!")

    drawCircuit(circuit1)
    drawCircuit(circuit2)

    while (true) {
        Thread.sleep(1000)
        clearScreen()

        if (player1.crash) {
            player1.crash = false
            println("${player1.icon} se ha estrellado")
        } else {
            moveCar(circuit1, player1)
        }

        if (player2.crash) {
            player2.crash = false
            println("${player2.icon} se ha estrellado")
        } else {
            moveCar(circuit2, player2)
        }

        drawCircuit(circuit1)
        drawCircuit(circuit2)


        if (player1.position == 0 && player2.position == 0) {
            print("EMPATE!!!")
            break
        }

        if (player1.position == 0) {
            print("GANADOR ${player1.icon}")
            break
        }

        if (player2.position == 0) {
            print("GANADOR ${player2.icon}")
            break
        }
    }
}

fun drawCircuit(circuit: MutableList<String>) {
    for (i in circuit) {
        print(i)
    }

    print("\n")
}


fun moveCar(circuit: MutableList<String>, player: Player) {
    val movement = Random.nextInt(1, 3)

    if (circuit[player.position] === "💥") {
        circuit[player.position] = "🌲"
    } else {
        circuit[player.position] = "_"
    }

    player.move(movement)

    if (circuit[player.position] == "🌲") {
        player.crash = true
        circuit[player.position] = "💥"
    } else {
        circuit[player.position] = player.icon
    }

    println("${player.icon} avanza $movement posiciones")
}

fun clearScreen() {
    try {
        val os: String? = System.getProperty("os.name")

        if (os != null) {
            if (os.contains("Windows")) {
                Runtime.getRuntime().exec("cls")
            } else {
                Runtime.getRuntime().exec("clear")
            }
        }
    } catch (e: Exception) {
        println(e.message)
    }
}
