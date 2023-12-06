/*
 * Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
 * - La función recibirá el mes y el año y retornará verdadero o falso.
 */
import 'dart:io';

const List<String> strMonths = [
  'ENE = 1',
  'FEB = 2',
  'MAR = 3',
  'ABR = 4',
  'MAY = 5',
  'JUN = 6',
  'JUL = 7',
  'AGO = 8',
  'SEP = 9',
  'OCT = 10',
  'NOV = 11',
  'DIC = 12',
];

void main() {
  late String? monthStr;
  late String? yearStr;
  late final int month;
  late final int year;
  bool monthIsReady = false;

  while (true) {
    // If month was already asignned, don't ask for it again.
    if (monthIsReady) {
      // Year
      print(
          "Escribe el año que deseas consultar en números: (por ejemplo: 1999)\n");
      yearStr = stdin.readLineSync();
      if (yearStr != null && int.tryParse(yearStr) != null) {
        year = int.parse(yearStr);
      } else {
        print('ERROR: Escribe un año en números..');
        continue;
      }

      // Friday thirteen check
      bool thereIsThirteenFriday = fridayThirteen(month: month, year: year);
      if (thereIsThirteenFriday) {
        print('¡Si hay un viernes 13!');
      } else {
        print('No se encontró un viernes 13 :(');
      }
      break;
    } else {
      // Month
      print(
          "Escribe el NÚMERO que representa al mes que deseas verificar, acá está la lista de opciones: \n$strMonths\n");
      monthStr = stdin.readLineSync();
      if (monthStr != null && int.tryParse(monthStr) != null) {
        int checkValidMonth = int.parse(monthStr);
        if (checkValidMonth > 0 && checkValidMonth < 13) {
          month = checkValidMonth;
          monthIsReady = true;
          continue;
        } else {
          print(
              'ERROR: Debes escoger un número entre el 1 y el 12 para escoger un mes válido.');
          continue;
        }
      } else {
        print(
            'ERROR: Debes escoger un número entre el 1 y el 12 para escoger un mes válido de esta lista: \n$strMonths');
        continue;
      }
    }
  }
}

bool fridayThirteen({
  required int month,
  required int year,
}) {
  DateTime date = DateTime(year, month, 13);

  // Verificar si el día 13 es un viernes
  return date.weekday == DateTime.friday;
}
