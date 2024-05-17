/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */

const checkNumber = (toCheck: number) => {
    let check: any = {
        primo: true,
        fibonacci: false,
        par: false
    };
    
    let number: number = toCheck;
    let answer: string = ""

    //CHECK NUMEROS PRIMOS
    if (number === 1) check.primo = true;

    for (let i = 2 ; i < number ; i++) {
        if(number % i === 0) {
            check.primo = false          
            break;
        };
    };

    //CHECK NUMEROS DE FIBONACCI
    let fibonacci: number[] = [2,1,1,0];

    for (let i = 0; i < number; i++) {
        let newFibonacci: number = fibonacci[0] + fibonacci[1]

        if (newFibonacci === number) {
            check.fibonacci = true;
            break;
        };

        fibonacci.unshift(newFibonacci);
    };

    //CHECK PAR O IMPAR
    toCheck % 2 === 0 ? check.par = true : check.par = false;

    //HANDLER DE RESPUESTAS
    check.primo === true ? answer += "es primo, " : answer += "no es primo, ";
    check.fibonacci === true ? answer += "es fibonacci " : answer += "no es fibonacci ";
    check.par === true ? answer += "y es par." : answer += "y es impar.";

    return `${number} ` + answer;
};

checkNumber(5);