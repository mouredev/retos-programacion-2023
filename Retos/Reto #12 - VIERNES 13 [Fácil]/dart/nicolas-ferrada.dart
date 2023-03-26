/*
 * Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
 * - La función recibirá el mes y el año y retornará verdadero o falso.
 */
import 'dart:io';

enum Months {
  jan,
  feb,
  mar,
  apr,
  may,
  jun,
  jul,
  aug,
  sep,
  oct,
  nov,
  dec,
}

extension MonthsNumber on Months {
  int getMonthNumber() {
    switch (this) {
      case Months.jan:
        return 1;
      case Months.feb:
        return 2;
      case Months.mar:
        return 3;
      case Months.apr:
        return 4;
      case Months.may:
        return 5;
      case Months.jun:
        return 6;
      case Months.jul:
        return 7;
      case Months.aug:
        return 8;
      case Months.sep:
        return 9;
      case Months.oct:
        return 10;
      case Months.nov:
        return 11;
      case Months.dec:
        return 12;
    }
  }
}

const List<String> strMonths = [
  'JAN = 1',
  'FEB = 2',
  'MAR = 3',
  'APR = 4',
  'MAY = 5',
  'JUN = 6',
  'JUL = 7',
  'AUG = 8',
  'SEP = 9',
  'OCT = 10',
  'NOV = 11',
  'DEC = 12',
];

void main() {
  late final String? monthStr;
  late final String? yearStr;
  late final int month;
  late final int year;

  while (true) {
    // Month
    print(
        "Type the month's NUMBER you want to consult, here are the options $strMonths\n ${monthStr = stdin.readLineSync()}");
    if (monthStr != null && int.tryParse(monthStr) != null) {
      month = int.parse(monthStr);
    } else {
      print(
          '$strMonths:\n Please, enter the number between 1 and 12 of the month you want to check');
      continue;
    }
    // Year
    print(
        "Type the year's NUMBER you want to consult, here are the options ${yearStr = stdin.readLineSync()}");
    if (yearStr != null && int.tryParse(yearStr) != null) {
      year = int.parse(yearStr);
    } else {
      print('Please, enter the year you want to check in numbers');
      continue;
    }

    fridayThirteen(month: month, year: year);
    break;
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
