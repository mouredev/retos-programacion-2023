/*
    * Crea una función que reciba un número decimal y lo trasforme a Octal
    * y Hexadecimal.
    * - No está permitido usar funciones propias del lenguaje de programación que
    * realicen esas operaciones directamente.
*/
const decToOctal = (number) => {
    let numberOctal = '';
    while (number > 0) {
        const rest = number % 8;
        numberOctal = rest + numberOctal;
        number = Math.floor(number / 8);
    }
    return numberOctal;
}

const charHexa = (number) => {
    let convertions = {
        10: "A",
        11: "B",
        12: "C",
        13: "D",
        14: "E",
        15: "F"
    }
    if (number in convertions) {
        return convertions[number];
    } else {
        return number;
    }
}
const decToHexa = (number) => {
    let numberHexa = '';
    while (number > 0) {
        const rest = number % 16;
        let char = charHexa(rest);
        numberHexa = char + numberHexa
        number = Math.floor(number / 16);
    }
    return numberHexa;
}
console.log(decToOctal(179))
console.log(decToHexa(179))