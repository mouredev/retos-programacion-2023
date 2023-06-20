/*

 Crea una función que reciba un número decimal y lo trasforme a Octal
 y Hexadecimal.
 - No está permitido usar funciones propias del lenguaje de programación que
 realicen esas operaciones directamente.

*/

function decimalOctalHexadecimal(numero) {
  let arrayOctal = [];
  let arrayHexadecimal = [];
  let octal = "";
  let hexadecimal = "";
  let division = 0;
  let residuo = 0;

  let numeroAOctal = numero;
  // regresa el numero en el sistma octal
  while (numeroAOctal !== 0) {
    division = Math.floor(numeroAOctal / 8);
    residuo = numeroAOctal % 8;
    arrayOctal.push(residuo);
    numeroAOctal = division;
  }
  octal = arrayOctal.reverse().join("");

  let numeroAHexadecimal = numero;
  // regresa el numero en el sistema hexadecimal
  while (numeroAHexadecimal !== 0) {
    division = Math.floor(numeroAHexadecimal / 16);
    residuo = numeroAHexadecimal % 16;
    switch (residuo) {
      case 10:
        arrayHexadecimal.push("A");
        break;
      case 11:
        arrayHexadecimal.push("B");
        break;
      case 12:
        arrayHexadecimal.push("C");
        break;
      case 13:
        arrayHexadecimal.push("D");
        break;
      case 14:
        arrayHexadecimal.push("E");
        break;
      case 15:
        arrayHexadecimal.push("F");
        break;
      default:
        arrayHexadecimal.push(residuo);
        break;
    }
    numeroAHexadecimal = division;
  }

  hexadecimal = arrayHexadecimal.reverse().join("");

  // Hexadecimal validacion

  if (hexadecimal.match(/[A-F]/)) {
    hexadecimal = String(hexadecimal);
  } else {
    hexadecimal = Number(hexadecimal);
  }

  return {
    "sistema octal": Number(octal),
    "sistema hexadecimal": hexadecimal,
  };
}

console.log(decimalOctalHexadecimal(8000)); // { 'sistema octal': 17500, 'sistema hexadecimal': '1F40' }
console.log(decimalOctalHexadecimal(1500));  // { 'sistema octal': 2734, 'sistema hexadecimal': '5DC' }
console.log(decimalOctalHexadecimal(500)); // { 'sistema octal': 764, 'sistema hexadecimal': '1F4' }
console.log(decimalOctalHexadecimal(80)); // { 'sistema octal': 120, 'sistema hexadecimal': 50 }