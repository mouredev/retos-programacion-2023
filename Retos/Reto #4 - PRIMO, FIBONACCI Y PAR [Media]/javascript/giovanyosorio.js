
/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */

function esPrimo(numero) {
    let primo=true
    if (numero <= 1) {
    primo=false
    }
    // Comprobamos si el número es divisible por algún número menor que él mismo
    for (let i = 2; i < numero; i++) {
    if (numero % i === 0) {
        primo=false
    }
    } 
    primo==true ? console.log(`el numero ${numero} es Primo`): console.log(`el numero ${numero} No es Primo`)
    }
function esPar(num) {
    num%2===0 ? console.log(`el numero ${num} es Par`): console.log(`el numero ${num} No es Par`)
}
function fibonacci(num){
 
    let prev1 =1
    let prev2=0
    let c=0
     let i=0
    while (i<num) {
       
      c=prev1+prev2
      prev2=prev1
      prev1=c
    i++

    }
    num==c ? console.log(`el numero ${num} es Fibonacci`) : console.log(`el numero ${num} No es Fibonacci`)

}

function comprobar(num) {
    
    esPrimo(num)
    esPar(num)
    fibonacci(num)
}

comprobar(12)