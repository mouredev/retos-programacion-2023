/*
 si un numero es par su reciduo de división modular es 0,
 sino es impar.

 para determinar un número fibonacci se puede usar la formula
 test de la raiz cuadrada de 5° o el criterio de la suma  
 de cuadrados.
 
 Un número n es número fibonacci si y solo si uno de los 
 siguientes es verdadero: 
 5n^2 + 4  ó  5n^2 - 4
*/



/**
 * Comprueba si un número es par.
 * @param {number} num - El número a evaluar.
 * @returns {boolean} - Devuelve true si el número es par, false si es impar.
 */
function isPar(num){
    return num % 2 === 0; 
}
/**
 * Comprueba si un número es primo.
 * @param {number} num - El número a evaluar.
 * @returns {boolean} - Devuelve true si el número es primo, false si no lo es.
 */
function isPrime(num){
    let sqrt = Math.floor(Math.sqrt(num));
    
    if(num <= 1){
        return false; // uno no es ni primo ni par
    }
    
    for(let i = 2; i <= sqrt; i++){
        if(num % i === 0){
            return false;
        }
    }
    
    return true;
}
/**
 * Comprueba si un numero pertenece a la secuencia de Fibonacci
 * @param {number} num - El número a evaluar
 * @returns {boolean} - Devuelve true si el numero cumple una de las dos condiciones, sino devuelve false
 */
function isFibonacci(num){
    // Calcula dos posibles resultados de la fórmula que indica la pertenencia a la secuencia de Fibonacci.
    const firstResult = 5 * num**2 + 4;
    const secondResult = 5 * num**2 - 4;

    // Calcula las raíces cuadradas de los resultados y verifica si son números enteros.
    const firstSqrt = Math.sqrt(firstResult);
    const secondSqrt = Math.sqrt(secondResult);
    
    // Devuelve true si al menos uno de los resultados es un número entero.
    return Number.isInteger(firstSqrt) || Number.isInteger(secondSqrt);
}


/**
 * Analiza un número e imprime mensajes que indican si es primo, pertenece a la secuencia de Fibonacci y si es par o impar.
 * @param {number} num - El número a analizar.
 */
const numberIs = (num) =>{
    let result = "";

    if(isPrime(num)){
        result += `${num} es primo, `;
    }else{
        result += `${num} no es primo, `;
    }

    if(isFibonacci(num)){
        result += "fibonacci, ";
    }
    else{
        result += "no es fibonacci, "
    }

    if(isPar(num)){
        result += "y es par";
    }
    else{
        result += "y es impar";
    }

    console.log(result);

}

const num = 2;
numberIs(num);