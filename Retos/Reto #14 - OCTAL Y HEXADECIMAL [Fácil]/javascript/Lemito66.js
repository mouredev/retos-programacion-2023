/*
 * Crea una función que reciba un número decimal y lo trasforme a Octal
 * y Hexadecimal.
 * - No está permitido usar funciones propias del lenguaje de programación que
 * realicen esas operaciones directamente.
 */

const decimalToOctal = (decimal) => {
  let array_response = [];
  let octal = "";
  while (decimal > 0) {
    array_response.push(decimal % 8);
    decimal = Math.floor(decimal / 8);
  }
  for (const i in array_response) {
    octal += array_response[i];
  }
    
  return octal.split("").reverse().join("");
};

const decimalToHexadecimal = (decimal) => {
    let array_response = [];
    let hexadecimal = "";
    while (decimal > 0) {
        array_response.push(decimal % 16);
        decimal = Math.floor(decimal / 16);
    }
    for (const i in array_response) {
        hexadecimal += array_response[i];
    }
    return hexadecimal.split("").reverse().join("");
};



console.log(decimalToOctal(500)); 
console.log(decimalToHexadecimal(500));

