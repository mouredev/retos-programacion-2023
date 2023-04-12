/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */

function par (num) {

    if (num % 2 === 0) {
        console.log("EL numero es par")
    } else {
        console.log("El numero es impar")
    }
}


function esPrimo (num) {
    if (num <= 1) return false;
    if (num === 2) return true;
    for(let i = 2; i <= Math.sqrt(num); i++) {
        if (num % i === 0) {
            return console.log("No es primo");
        }
    }
    return console.log("Es primo");
}


function esFibonacci(num) {
    const root1 = 5* (num **2 ) + 4;
    const root2 = 5* (num **2 ) - 4;
    return console.log("Es fibonacci? "+Math.sqrt(root1) % 1 === 0 || Math.sqrt(root2) % 1 === 0);
}


function chequearNumero(num) {
    const esNumeroPrimo = esPrimo(num);
    const esNumeroFibonacci = esFibonacci(num);
    const esNumeroPar = par(num);

    let resultString = `${num} es `; 
        if (esNumeroPrimo) {
            resultString += "primo, ";
        } else {
            resultString += "no es primo, " ;
        } 
        if (esNumeroFibonacci) {
            resultString += "fibonacci, ";
        } else {
            resultString += "no es fibonacci, ";
        } if (esNumeroPar) {
            resultString += "y es par. ";
        } else {
            resultString += " y es impar. ";
        }
        return resultString;
}

console.log(chequearNumero(2));