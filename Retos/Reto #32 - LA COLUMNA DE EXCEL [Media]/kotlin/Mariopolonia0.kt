package EjercicioKotlin.Mouredev

/*
 * Crea una función que calcule el número de la columna de una hoja de Excel
 * teniendo en cuenta su nombre.
 * - Las columnas se designan por letras de la "A" a la "Z" de forma infinita.
 * - Ejemplos: A = 1, Z = 26, AA = 27, CA = 79.
 */

fun main() {
    reto32_columna_exel("A")
    reto32_columna_exel("Z")
    reto32_columna_exel("AA")
    reto32_columna_exel("CA")
    reto32_columna_exel("AAA")
}

class reto32_columna_exel(columna: String) {
  
    init {
        var contador = 0

        if (columna.length > 1) {

            for (it in 0..columna.length - 2) {
                for (char in 'A'..columna[it]) {
                    contador += 26
                }
            }

            for (it in 'A'..columna[columna.length - 1]) {
                contador++
            }

        } else {
            for (it in 'A'..columna[0]) {
                contador++
            }
        }

        println("columna $columna = $contador")
    }
}
