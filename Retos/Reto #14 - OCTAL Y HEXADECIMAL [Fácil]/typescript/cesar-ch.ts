/*
 * Crea una función que reciba un número decimal y lo trasforme a Octal
 * y Hexadecimal.
 * - No está permitido usar funciones propias del lenguaje de programación que
 * realicen esas operaciones directamente.
 */


function SystemChange2(number: number): string {
    const octal: string = OctalSystem2(number);
    const hexadecimal: string = HexadecimalSystem2(number);

    return `Sistema Octal: ${octal} - Sistema Hexadecimal: ${hexadecimal}`;
}

function OctalSystem2(number: number): string {
    let arr: number[] = [];
    let a: number = number;
    let b: number = 8;

    while (a > b) {
        arr.unshift(a % b);
        a = Math.floor(a / b);
    }
    arr.unshift(a);
    return arr.join('');
}

function HexadecimalSystem2(number: number): string {
    const obj: { [key: number]: string } = { 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F' };
    let arr: (number | string)[] = [];
    let a: number = number;
    let b: number = 16;

    while (a > b) {
        if (a % b >= 10) {
            arr.unshift(obj[a % b]);
        } else {
            arr.unshift(a % b);
        }
        a = Math.floor(a / b);
    }

    if (a >= 10) {
        arr.unshift(obj[a % b]);
    } else {
        arr.unshift(a);
    }
    return arr.join('');
}

console.log(SystemChange2(10));
console.log(SystemChange2(20));
console.log(SystemChange2(30));

