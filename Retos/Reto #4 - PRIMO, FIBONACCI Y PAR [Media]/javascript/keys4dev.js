/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo,
 * fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */

const esFibonacci = (numero)=>{
    if (numero == 0) return "es fibonacci"; 
    let secuencia = [0,1]
    while (secuencia[secuencia.length-1]<numero){
        secuencia.push(parseInt(secuencia.slice(-1))+parseInt(secuencia.slice(-2,-1)))
    }
    return secuencia.pop()==numero ? "es fibonacci" : "no es fibonacci" 
};

const esPrimo = (numero)=>{
    if(numero < 2) return "no es primo";
    for (let index = 2; index < numero; index++) {
        if (numero % index  == 0) return "no es primo"
    }
    return "es primo"
};

const esPar = (numero)=>{
    return numero%2==0 ? "es par" : "es impar";
};

const esFibonacciEsParEsPrimo = (numero)=>{
    return `${numero} ${esPrimo(numero)}, ${esFibonacci(numero)} y ${esPar(numero)}`;
}

console.log(esFibonacciEsParEsPrimo(0));





