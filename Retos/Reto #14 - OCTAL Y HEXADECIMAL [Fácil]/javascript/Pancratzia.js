/*
 * Crea una función que reciba un número decimal y lo trasforme a Octal
 * y Hexadecimal.
 * - No está permitido usar funciones propias del lenguaje de programación que
 * realicen esas operaciones directamente.
 * 
 * 
 * Hecho por LAURA ORTEGA - 30/08/2023
 */
function decimalToOctal(decimalNumber) {
    if (decimalNumber === 0) {
        return '0';
    }

    let octalResult = '';
    
    while (decimalNumber > 0) {
        const remainder = decimalNumber % 8;
        octalResult = remainder + octalResult;
        decimalNumber = Math.floor(decimalNumber / 8);
    }
    
    return octalResult;
}
  
function decimalToHexadecimal(decimalNumber) {
    if (decimalNumber === 0) {
        return '0';
    }

    const hexadecimalDigits = '0123456789ABCDEF';
    let hexadecimalResult = '';

    while (decimalNumber > 0) {
        const remainder = decimalNumber % 16;
        hexadecimalResult = hexadecimalDigits[remainder] + hexadecimalResult;
        decimalNumber = Math.floor(decimalNumber / 16);
    }

    return hexadecimalResult;
}

const main = (number) => {
  number = parseInt(number);

  console.log(`El numero decimal ${number} en octal es ${decimalToOctal(number)} y el numero decimal ${number} en hexadecimal es ${decimalToHexadecimal(number)}`);
};

main(10);
main(15);
main(20);
main(8);
main(7);
main(161);
