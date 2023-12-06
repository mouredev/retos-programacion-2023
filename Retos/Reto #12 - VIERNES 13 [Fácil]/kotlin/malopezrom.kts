import java.time.DayOfWeek
import java.time.LocalDate
import java.util.Calendar

/*
 * Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
 * - La función recibirá el mes y el año y retornará verdadero o falso.
 */


/**
 * Listado de meses del año en castellano antiguo
 */
val MOUNTHS = mapOf(
    1 to "Enero",
    2 to "Febrero",
    3 to "Marzo",
    4 to "Abril",
    5 to "Mayo",
    6 to "Junio",
    7 to "Julio",
    8 to "Agosto",
    9 to "Septiembre",
    10 to "Octubre",
    11 to "Noviembre",
    12 to "Diciembre"
)
/**
 * Funcion que determina si un mes tiene un viernes 13 o no
 * @param month Mes a evaluar
 * @param year Año a evaluar
 * @return true si el mes tiene un viernes 13, false en caso contrario
 */
fun hasFriday13(month: Int, year: Int): Boolean {
    //Tan fácil como obtener el dia de la semana que corresponde al dia 13 de un mes y año dados y si es Viernes.. voila!
    return LocalDate.of(year, month, 13).dayOfWeek == DayOfWeek.FRIDAY
}
/**
 * Funcion que imprime si un mes tiene un viernes 13 o no
 * @param month Mes a evaluar
 * @param year Año a evaluar
 */
fun printResult(month: Int, year: Int) {
    println("El mes de ${MOUNTHS[month]} del año $year ${if (hasFriday13(month, year)) "" else "no"} tiene Viernes 13")
}


printResult(1, 2023)
printResult(3, 2023)
printResult(5, 2023)
