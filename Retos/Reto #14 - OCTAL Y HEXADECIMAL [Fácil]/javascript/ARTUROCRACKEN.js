/*
 * Crea una función que reciba un número decimal y lo trasforme a Octal
 * y Hexadecimal.
 * - No está permitido usar funciones propias del lenguaje de programación que
 * realicen esas operaciones directamente.
 */

function main(num) {
  // validations
  if (typeof num !== 'number') {
    console.error('Number must be a positive integer.');
    return;
  }

  num = Math.floor(num);

  // To Octal
  const octalNum = numToOctal(num);

  // To Hexadecimal
  const hexadecimalNum = numToHexadecimal(num);

  console.log(`Decimal number received: ${num}
    Octal: ${octalNum}
    Hexadecimal: ${hexadecimalNum}
  `);
}

function numToOctal(num) {
  let remainder;
  let quotient;
  let octalNum = [];

  if (num < 8) {
    return num;
  } else if (num >= 8) {
    quotient = num;
    while (quotient > 0) {
      remainder = Math.floor(quotient % 8);
      quotient = Math.floor(quotient / 8);
      octalNum.push(remainder);
    }
    octalNum = parseInt(octalNum.reverse().join(''));
    return octalNum;
  }
}

function numToHexadecimal(num) {
  let remainder;
  let quotient;
  let hexadecimalNum = [];

  const hex = { 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F' }

  if (num < 10) {
    return num;
  } else if (num < 16 && num > 9) {
    return hex[num];
  } else if (num >= 16) {
    quotient = num;
    while (quotient > 0) {
      remainder = Math.floor(quotient % 16);
      quotient = Math.floor(quotient / 16);
      
      if (remainder > 10) {
        hexadecimalNum.push(hex[remainder])
      } else {
        hexadecimalNum.push(remainder)
      }
    }
    hexadecimalNum = hexadecimalNum.reverse().join('');
    return hexadecimalNum;
  }
}

main(960)
main(1792)
main(15)
main(8)
