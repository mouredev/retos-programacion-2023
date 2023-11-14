/*
 * Crea una función que reciba un número decimal y lo trasforme a Octal
 * y Hexadecimal.
 * - No está permitido usar funciones propias del lenguaje de programación que
 * realicen esas operaciones directamente.
 */
let hexas = {
    10: 'A',
    11: 'B',
    12: 'C',
    13: 'D',
    14: 'E',
    15: 'F'
}
function decimalToOctal(number) {
  let octal = "";
  let result = number;
  while (result > 0) {
    octal = (result % 8) + octal;
    result = Math.floor(result / 8);
  }
  return octal;
}

function decimalToHexadecimal(number) {
    let hexadecimal = "";
    let result = number;
    while (result > 0) {
        let temp = result % 16;
        if (temp > 9) {
        temp = hexas[temp];
        }
        hexadecimal = temp + hexadecimal;
        result = Math.floor(result / 16);
    }
    return hexadecimal;
    }

console.log(decimalToOctal(10));
console.log(decimalToHexadecimal(16852));
