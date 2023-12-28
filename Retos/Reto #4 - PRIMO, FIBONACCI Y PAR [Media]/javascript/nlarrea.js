/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */

function isPrime(number){
    if(number === 1 || number <= 0) return false;
    for(let i=2; i<number; i++){
        if(number%i === 0) return false;
    }
    return true;
}

function isFibonacci(number){
    let current = 0;
    let next = 1;

    while(current <= number){
        if(current === number) return true;
        let aux = current + next;
        current = next;
        next = aux;
    }

    return false;
}

function isEven(number){
    return number % 2 === 0;
}

function checkNumber(number){
    let answer = isPrime(number)? `${number} es primo,` : `${number} no es primo,`;
    answer += isFibonacci(number)? " es fibonacci" : " no es fibonacci";
    answer += isEven(number)? " y es par" : " y es impar";
    
    return answer;
}

console.log(checkNumber(2));    // 2 es primo, es fibonacci y es par
console.log(checkNumber(7));    // 7 es primo, no es fibonacci y es impar
console.log(checkNumber(8));    // 8 no es primo, es fibonacci y es par