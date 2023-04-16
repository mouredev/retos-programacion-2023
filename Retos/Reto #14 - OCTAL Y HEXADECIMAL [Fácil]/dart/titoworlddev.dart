/*
 * Crea una función que reciba un número decimal y lo trasforme a Octal
 * y Hexadecimal.
 * - No está permitido usar funciones propias del lenguaje de programación que
 * realicen esas operaciones directamente.
 */

void main() {
  print(decimalToOctal(5487));
  print(decimalToHexa(5487));
}

decimalToOctal(num number) {
  String resultado = '';

  do {
    resultado = '${(number % 8)}$resultado';
    number = number ~/ 8;
  } while (number > 0);

  return resultado;
}

decimalToHexa(num number) {
  const numToLetter = {
    '10': 'A',
    '11': 'B',
    '12': 'C',
    '13': 'D',
    '14': 'E',
    '15': 'F'
  };
  List rests = [];

  do {
    rests.add(number % 16);
    number = number ~/ 16;
  } while (number > 0);

  rests = rests.map((number) {
    return number > 9 ? numToLetter['$number'] : number;
  }).toList();

  return rests.join();
}
