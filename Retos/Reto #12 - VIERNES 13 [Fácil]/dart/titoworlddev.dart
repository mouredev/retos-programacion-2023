/*
 * Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
 * - La función recibirá el mes y el año y retornará verdadero o falso.
 */

void main() {
  print(isFriday13(3, 2020));
  print(isFriday13(10, 2017));
  print(isFriday13(1, 1985));
}

int isFriday13(int month, int year) {
  final date = DateTime(year, month, 13);
  return date.weekday;
}
