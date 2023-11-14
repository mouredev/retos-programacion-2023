/*
 * Crea una función que reciba un número decimal y lo trasforme a Octal
 * y Hexadecimal.
 * - No está permitido usar funciones propias del lenguaje de programación que
 * realicen esas operaciones directamente.
 */


function SystemChange(number) {
    const octal = OctalSystem(number)
    const hexadecimal = HexadecimalSystem(number)

    return `Sistema Octal: ${octal} - Sistema Hexadecimal: ${hexadecimal}`
}

function OctalSystem(number) {
    let arr = []
    let a = number
    let b = 8
    while (a > b) {
        arr.unshift(a % b)
        a = Math.floor(a / b)
    }
    arr.unshift(a)
    return arr.join('')
}

function HexadecimalSystem(number) {
    const obj = { 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F' }
    let arr = []
    let a = number
    let b = 16
    while (a > b) {
        if (a % b >= 10) {
            arr.unshift(obj[a % b])
        } else {
            arr.unshift(a % b)
        }
        a = Math.floor(a / b)
    }

    if (a >= 10) {
        arr.unshift(obj[a % b])
    } else {
        arr.unshift(a)
    }
    return arr.join('')
}

console.log(SystemChange(10));
console.log(SystemChange(20));
console.log(SystemChange(30));
