
class Reto14(var decimal: Int) {
    init {
        Octal()
        println()
        Hexadecimal()
    }

    private fun Octal() {
        var consiente = decimal
        var residuo = ""

        while (consiente > 8) {
            residuo += consiente % 8
            consiente = consiente / 8
        }

        print("El decimal: $decimal en octal es :")
        print(consiente)

        for (it in (residuo.length - 1 downTo 0)) {
            print(residuo[it])
        }
    }

    private fun Hexadecimal() {
        var consiente = decimal
        val residuo = mutableListOf<Int>()

        while (consiente > 16) {
            residuo.add(consiente % 16)
            consiente = consiente / 16
        }

        print("El decimal: $decimal en Hexadecimal es :")
        print(octenerLetra(consiente))

        for (it in (residuo.size - 1 downTo 0)) {
            print(octenerLetra(residuo[it]))
        }
    }

    private fun octenerLetra(digito: Int): String {
        return when (digito) {
            10 -> "A"
            11 -> "B"
            12 -> "C"
            13 -> "D"
            14 -> "E"
            15 -> "F"
            else -> digito.toString()
        }
    }
}

fun main() {
    println("De decimal a Octal y Hexadecimal")
    print("Ingrese el decimal:")
    Reto14(readln().toInt())
}
