/*
 * Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
 * - La función recibirá el mes y el año y retornará verdadero o falso.
 */

/**
 * Listado de meses del año en castellano antiguo
 */
const MONTHS = [
    "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
]

/**
 * Funcion que determina si un mes tiene un viernes 13 o no
 * @param month Mes a evaluar
 * @param year Año a evaluar
 * @return true si el mes tiene un viernes 13, false en caso contrario
 */
function hasFriday13(month: number, year: number): boolean {
    //Tan fácil como obtener el dia de la semana que corresponde al dia 13 de un mes y año dados y si es Viernes.. voila!
    return new Date(year, month - 1, 13).getDay() === 5;
}
/**
 * Funcion que imprime si un mes tiene un viernes 13 o no
 * @param month Mes a evaluar
 * @param year Año a evaluar
 */
function printFriday13(month: number, year: number): void {
    console.log(`El mes de ${MONTHS[month-1]} del año ${year} ${hasFriday13(month, year) ? "" : "NO"} tiene viernes 13`);
}


printFriday13(3, 2020);
printFriday13(10, 2017);
printFriday13(1, 1985);
