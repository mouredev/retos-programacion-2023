/*
 * Crea una función que reciba un número decimal y lo trasforme a Octal
 * y Hexadecimal.
 * - No está permitido usar funciones propias del lenguaje de programación que
 * realicen esas operaciones directamente.
 */

void main() {
  print(decimalToOctal(245));
}

decimalToOctal(num number) {
  final hasDecimals = number.toString().contains('.');
  List numToList = number.toString().split('.');
  num dividendo = hasDecimals ? num.parse(numToList[0]) : number;
  num decimales = hasDecimals ? num.parse('0.${numToList[1]}') : 0;
  int divisor = 8;
  List resultado = [];

  do {
    resultado.add(dividendo % divisor);
    dividendo = dividendo ~/ divisor;
  } while (dividendo > 0);

  if (hasDecimals) {
    decimales = (decimales * divisor).toInt();
  }

  return hasDecimals
      ? '${resultado.reversed.join()}.$decimales'
      : resultado.reversed.join();
}
