/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */

function isFibonacci(number){
    if (number === 0 || number === 1) {
        return true;
      }
    
      let previous = 0;
      let current = 1;
    
      while (current <= number) {
        const next = previous + current;
        if (next === number) {
          return true;
        }
        previous = current;
        current = next;
      }
      return false;
}

function isPar(number){
    return number%2==0;
}

function isPrime(number){
    if (number <= 1) {
        return false;
      }
      for (let i = 2; i <= Math.sqrt(number); i++) {
        if (number % i === 0) {
          return false;
        }
      }
      return true;
}

const sample1 = 2
const sample2 = 7
const sample3 = 21
const sample4 = 13
const sample5 = 54

console.log(`1. El número ${sample1} ${!isPrime(sample1)?'no':''} es primo, ${!isFibonacci(sample1)?'no':''} es fibonacci y ${!isPar(sample1)?'no':''} es par`)
console.log(`2. El número ${sample2} ${!isPrime(sample2)?'no':''} es primo, ${!isFibonacci(sample2)?'no':''} es fibonacci y ${!isPar(sample2)?'no':''} es par`)
console.log(`3. El número ${sample3} ${!isPrime(sample3)?'no':''} es primo, ${!isFibonacci(sample3)?'no':''} es fibonacci y ${!isPar(sample3)?'no':''} es par`)
console.log(`4. El número ${sample4} ${!isPrime(sample4)?'no':''} es primo, ${!isFibonacci(sample4)?'no':''} es fibonacci y ${!isPar(sample4)?'no':''} es par`)
console.log(`5. El número ${sample5} ${!isPrime(sample5)?'no':''} es primo, ${!isFibonacci(sample5)?'no':''} es fibonacci y ${!isPar(sample5)?'no':''} es par`)