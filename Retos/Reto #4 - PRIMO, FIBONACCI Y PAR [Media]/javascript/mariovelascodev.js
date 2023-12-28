"use strict"

function whatIsIt(number) {

    //Variables
    let result = "";
    let fibonacci = [1, 1];

    //Comprobar si el número introducido es par
    if (number % 2 === 0) {
        result += "par";
    }else {
        result += "impar";
    }

    //Comprobar si el número es primo
    if(number % 2 === 0 && number % 3 === 0 && number % 5 === 0 && number % 7 === 0 && number % 11 === 0) {
        result += ", no es primo";
    }else {
        result += ", es primo";
    }

    //Comprobar Fibonacci
    
    //Sacamos la secuencia de Fibonacci del rango introducido por parametro y añadimos al array
    for(let i=1 ; i < number; i++) {
        let nextNumber = fibonacci[i] + fibonacci[i-1];
        fibonacci.push(nextNumber);

        //Si el último número es igual al introducido por parámetros paramos el bucle
        if (nextNumber === number) {
            break;
        }
    }

    //Comprobamos si el último número es igual al introducido por parámetros
    if(fibonacci[fibonacci.length-1] === number) {
        result += ", es fibonacci";
    }else {
        result += ", no es fibonacci";
    }

    console.log(number+" es "+result);
}

whatIsIt(2);
whatIsIt(7);
whatIsIt(13);
whatIsIt(113);