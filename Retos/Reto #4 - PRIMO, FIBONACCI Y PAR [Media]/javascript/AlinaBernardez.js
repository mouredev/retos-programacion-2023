// Función para comprobar si el número es primo:
function checkPrimo(number) {
    let isPrime = true;
    if(number === 1) {
        return 'Introducir un número mayor que 1'
    }
    else if(number > 1) {
        for(let i = 2; i < number; i++) {
            if(number % i == 0) {
                isPrime = false;
                return `${number} no es primo,`
            }
            else {
                return `${number} es primo,`
            }
        }
    }
}

//Función para comprobar si el número es Fibonacci (primero si es cuadrado perfecto):
function checkSquare(x) {
    let s = parseInt(Math.sqrt(x));
    return (s * s == x);
}

function checkFibo(number) {
    return checkSquare(5 * number * number + 4) || 
    checkSquare(5 * number * number - 4) ? 
    ' fibonacci ' : 
    ' no es fibonacci ';
}

//Función para comprobar si el número es par o impar:
function checkPar(number) {
    return number % 2 == 0 ? 'y es par.' : 'y es impar.';
}


function checkNumber(number) {
    return `${checkPrimo(number)}${checkFibo(number)}${checkPar(number)}`
}

checkNumber(13);