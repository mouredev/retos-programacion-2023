/*
 * Crea una función que reciba un número decimal y lo trasforme a Octal
 * y Hexadecimal.
 * - No está permitido usar funciones propias del lenguaje de programación que
 * realicen esas operaciones directamente.
 */

const convertToOctal = (number) => {
  let octal = '';
  while (number > 0) {
    const rest = number % 8;
    octal = rest + octal;
    number = Math.floor(number / 8);
  }

  return octal;
};

const convertToHexadecimal = (number) => {
  let hexadecimal = '';
  while (number > 0) {
    const remainder = number % 16;
    const char = remainder < 10 ? remainder : String.fromCharCode(remainder + 55);
    hexadecimal = char + hexadecimal;
    number = Math.floor(number / 16);
  }
  return hexadecimal;
};

const convertToHexadecimalAndOctal = (number) => ({
  octal: convertToOctal(number),
  hexadecimal: convertToHexadecimal(number),
});

// Visita mi repo en GitHub para ver y correr los tests de este código --> https://github.com/marcode24/weekly-challenges
