/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */

const isEven = (number) => {
    if (number % 2 ===0){
        return true
    }
    else{
        return false
    }
}

console.log(isEven(5));