fun main() {

    /*
    * Reto #32 07/08/2023 LA COLUMNA DE EXCEL
    *
    * Crea una función que calcule el número de la columna de una hoja de Excel
    * teniendo en cuenta su nombre.
    * - Las columnas se designan por letras de la "A" a la "Z" de forma infinita.
    * - Ejemplos: A = 1, Z = 26, AA = 27, CA = 79.
    *
    */
    val columnas = listOf("A", "Z", "AA", "CA", "AZ", "AFR")
    columnas.forEach { columna ->
        println("La columna $columna es ${dameNumColumnaExcel(columna)}")
        println("-".padStart(20, '-'))
    }
}

fun dameNumColumnaExcel(columna: String):Int {
    var valor = 0
    val len = columna.length - 1

    (len downTo 0).forEach {
        val valorLetra = (columna[it].code%65) + 1
        val multiplicador: Double = Math.pow( 26.toDouble(), (len-it).toDouble() )
        valor += (valorLetra * multiplicador.toInt())
    }

    return valor

}


