fun interpretAbacusNumber(abacus: Array<String>) {
    var number = ""
    if (abacus.size == 7 && abacus.all { row ->
            row.length == 12 && row.replace("---", "") == "OOOOOOOOO"
        }) {
        abacus.forEach { number += it.split("---")[0].length }
        println("Resultado: ${number.reversed().chunked(3).joinToString(".").reversed()}")
    } else {
        println("El ábaco debe tener 7 filas y cada fila debe tener 12 caracteres y en este caso no se cumple:")
        abacus.forEach { println(it) }
    }
}

fun main() {
    interpretAbacusNumber(
        arrayOf(
            "O---OOOOOOOO",
            "OOO---OOOOOO",
            "---OOOOOOOOO",
            "OO---OOOOOOO",
            "OOOOOOO---OO",
            "OOOOOOOOO---",
            "---OOOOOOOOO"
        )
    )
}