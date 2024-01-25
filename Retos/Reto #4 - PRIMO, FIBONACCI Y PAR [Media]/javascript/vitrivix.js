/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */

const fibonacciNumber = (arg) => {
    let count = 0, a = 0, b = 1
    while(count < 1000) {
        count = a + b;
        if(arg === count) return 'Es fibonacci';
        a = b;
        b = count;
    } return 'No es fibonacci';
}

const cousinNumber = (arg) => {
    if (arg <= 1) return 'No es primo';
    for (let i = 2; i <= Math.sqrt(arg); i++) {        
        if (arg % i === 0) return 'No es primo';
    } return 'Es primo';
}

const evenNumber = (arg) => {
    if (arg % 2 === 0) return 'Es par';
    return 'Es impar';
}

const checkNumber = (arg) => {
    return `${arg} => ${cousinNumber(arg)}, ${fibonacciNumber(arg)} y ${evenNumber(arg)}`;
}

console.log(checkNumber(2))
console.log(checkNumber(7))