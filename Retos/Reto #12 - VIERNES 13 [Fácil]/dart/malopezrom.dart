/*
 * Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
 * - La función recibirá el mes y el año y retornará verdadero o falso.
 */

/**
 * Listado de meses del año en castellano antiguo
 */
List<String> months = [
  'Enero',
  'Febrero',
  'Marzo',
  'Abril',
  'Mayo',
  'Junio',
  'Julio',
  'Agosto',
  'Septiembre',
  'Octubre',
  'Noviembre',
  'Diciembre'

];

/**
 * Funcion principal
 */
void main() {
  printFriday13(4, 2022);
  printFriday13(3, 2023);
  printFriday13(1, 2023);

}

/**
 * Funcion que determina si un mes tiene un viernes 13 o no
 * @param month Mes a evaluar
 * @param year Año a evaluar
 * @return true si el mes tiene un viernes 13, false en caso contrario
 */
bool hasFriday13(int month, int year) {
  //Tan fácil como obtener el dia de la semana que corresponde al dia 13 de un mes y año dados y si es Viernes.. voila!
  final date = DateTime(year, month, 13);
  return date.weekday == DateTime.friday;

}

/**
 * Funcion que imprime si un mes tiene un viernes 13 o no
 * @param month Mes a evaluar
 * @param year Año a evaluar
 */
void printFriday13(int month, int year) {
  if (hasFriday13(month, year)) {
    print("El mes de ${months[month-1]} de $year tiene un Viernes 13");

  }
  else {
    print("El mes de ${months[month-1]} de $year NO tiene un Viernes 13");
  }
}
