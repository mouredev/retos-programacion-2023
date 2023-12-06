/*
 * Crea una función que reciba un número decimal y lo trasforme a Octal
 * y Hexadecimal.
 * - No está permitido usar funciones propias del lenguaje de programación que
 * realicen esas operaciones directamente.
 */

function decimalToOctalAndHexa(decNum) {
    const convertions = {
        0: [0, 0],
        1: [1, 1],
        2: [2, 2],
        3: [3, 3],
        4: [4, 4],
        5: [5, 5],
        6: [6, 6],
        7: [7, 7],
        8: [10, 8],
        9: [11, 9],
        10: [12, 'A'],
        11: [13, 'B'],
        12: [14, 'C'],
        13: [15, 'D'],
        14: [16, 'E'],
        15: [17, 'F']
    };

    const decimalTo = (base, index) => {
        let number = decNum;
        let numList = [];

        if (convertions[number]) return convertions[number][index];

        while (number > base) {
            numList.push(convertions[number % base][index]);
            number = parseInt(number / base);
        }

        numList.push(convertions[number % base][index]);

        return numList.reverse().join("");
    };

    let octal = parseInt(decimalTo(8, 0));
    let hexa = decimalTo(16, 1);

    return {octal, hexa};
}

console.log(decimalToOctalAndHexa(11));     // {octal: 13, hexa: 'B'}
console.log(decimalToOctalAndHexa(495));    // {octal: 757, hexa: '1EF'}