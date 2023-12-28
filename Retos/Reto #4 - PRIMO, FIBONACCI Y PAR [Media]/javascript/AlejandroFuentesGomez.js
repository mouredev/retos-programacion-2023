/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo,
 * fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */

console.log(describeNumberProperties(7));

function describeNumberProperties(number) {
    let result = `${number}`;
    result += isPrimeNumber(number) ? ' es primo,' : ' no es primo,'
    result += isFibonacciNumber(number) ? ' fibonacci' : ' no es fibonacci';
    result += number % 2 === 0 ? ' y es par.' : ' y es impar.'
    return result;
}

function isFibonacciNumber(num){
    let fibonacciList = generateFibonacciList(num);
    return fibonacciList.includes(num)
}
function generateFibonacciList(num){
     let result = [1,1]
     while(result[result.length-1]<=num){
        result.push(result[result.length-1] + result[result.length-2]);
     }
     return result;
}
function isPrimeNumber(num) {
    let primeNumberList = generatePrimeNumberList(num);
    return primeNumberList.includes(num) || primeNumberList.every((element)=> num % element !== 0);
}
function generatePrimeNumberList(num){
    let primeNumberList = []
    let list = [...Array(num+1).keys()].filter((element)=> element !== 0 && element!==1 && element!==num);
    list.forEach((element)=> {
        let divList = list.filter((div)=> element % div ===0)
        divList.length === 1 ? primeNumberList.push(element): '';
    });
    return primeNumberList;
}