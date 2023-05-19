/*
 * Crea una función que reciba un número decimal y lo trasforme a Octal
 * y Hexadecimal.
 * - No está permitido usar funciones propias del lenguaje de programación que
 * realicen esas operaciones directamente.
 */

class NumberTransformer {
  toOctal(number: number): string {
    let octal = '';
    let index = 1;
    while (number > 0) {
      const rest = number % 8;
      octal = rest + octal;
      number = Math.floor(number / 8);
    }
    return octal;
  }

  toHex(number: number): string {
    const digits = [1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F'];
    let hex = '';
    while (number > 0) {
        const rest = number % 16;
        let char = digits[rest];
        hex = char + hex
        number = Math.floor(number / 16);
    }
    return hex;
  }
}

const transformer = new NumberTransformer();
console.log(transformer.toOctal(333));
console.log(transformer.toHex(333));