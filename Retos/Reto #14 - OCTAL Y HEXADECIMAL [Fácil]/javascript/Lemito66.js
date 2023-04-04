/*
 * Crea una función que reciba un número decimal y lo trasforme a Octal
 * y Hexadecimal.
 * - No está permitido usar funciones propias del lenguaje de programación que
 * realicen esas operaciones directamente.
 */

const decimalToOctal = (decimal) => {
  let octal = "";
  while (decimal > 0) {
    octal = (decimal % 8) + octal;
    decimal = Math.floor(decimal / 8);
  }
  return octal;
};

console.log(decimalToOctal(500)); // 12
