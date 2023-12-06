import 'package:intl/intl.dart';

void main() {
  print(viernesTrece(1, 2023));
  print(viernesTrece(2, 2023));
  print(viernesTrece(15, 2023));
}

dynamic viernesTrece(int month, int year) {
  if (month >= 1 && month <= 12) {
    final date = DateTime(year, month, 13);
    return DateFormat('EEEE').format(date) == "Friday";
  } else {
    return "El mes ingresado no es válido. Ingrese un mes entre 1 y 12";
  }
}
