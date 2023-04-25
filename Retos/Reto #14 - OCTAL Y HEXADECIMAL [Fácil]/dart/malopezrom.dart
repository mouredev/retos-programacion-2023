/*
 * Crea una función que reciba un número decimal y lo trasforme a Octal
 * y Hexadecimal.
 * - No está permitido usar funciones propias del lenguaje de programación que
 * realicen esas operaciones directamente.
 */

/**
 * Funciones de Extension para un numero
 */
extension NumberExtensions on num {

  /**
   * Funcion de extension para convertir un numero a octal
   */
  int toOctal() {
    var octal = 0;
    var decimal = this.toInt();
    var i = 1;
    while (decimal != 0) {
      octal += (decimal % 8) * i;
      decimal ~/= 8;
      i *= 10;
    }
    return octal;
  }

  /**
   * Funcion de extension para convertir un numero a hexadecimal
   */
  String toHexadecimal() {
    var hexadecimal = "";
    var decimal = this.toInt();
    while (decimal != 0) {
      final value = decimal % 16;
      hexadecimal = value < 10
          ? '$value$hexadecimal'
          : '${String.fromCharCode(value + 55)}$hexadecimal';
      decimal ~/= 16;
    }
    return hexadecimal;
  }
}

/**
 * Funcion principal
 */
void main(){

  int value = 255;
  print(value.toOctal());
  print(value.toHexadecimal());

}