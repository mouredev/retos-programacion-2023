import java.time.LocalDate

fun main() {

    /*
    * Reto #12 20/03/2023
    *
    * Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
    * - La función recibirá el mes y el año y retornará verdadero o falso.
    *
    */

    // Muestra los meses que tienen Viernes 13 en el intervalo de años dado
    // muestraViernes13(2022, 2025);

    var month = 1
    var year = 2023

    if (hasViernes13(month, year) )
        println ("${month.toString().padStart(2,'0')}-${year} TIENE UN VIERNES 13")
    else
        println ("${month.toString().padStart(2,'0')}-${year} NO TIENE UN VIERNES 13")

    month = 2
    year = 2023

    if (hasViernes13(month, year) )
        println ("${month.toString().padStart(2,'0')}-${year} TIENE UN VIERNES 13")
    else
        println ("${month.toString().padStart(2,'0')}-${year} NO TIENE UN VIERNES 13")

}



fun hasViernes13(month: Int, year: Int): Boolean {

    val fecha = LocalDate.parse("${year}-${month.toString().padStart(2, '0')}-13")
    return ("FRIDAY" == fecha.dayOfWeek.toString())

}

fun muestraViernes13(desde: Int, hasta: Int) {
    (desde..hasta).forEach { year ->
        (1..12).forEach { month ->
            if (hasViernes13(month, year)) {
                val mes = LocalDate.parse( "2023-${month.toString().padStart(2, '0')}-01" )
                println("${mes.month} de ${year} tiene un VIERNES 13")
            }

        }

    }
}