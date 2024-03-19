// Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
// Ejemplos:
// - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
// - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"

function isEven(numberToCheck) {
    return (numberToCheck % 2 === 0);
}

function isPerfectSquare(numberToCheck) {
    let square = parseInt(Math.sqrt(numberToCheck));
    return (square * square == numberToCheck);
}

function isFibonacci(numberToCheck) {
    let fib1 = 0;
    let fib2 = 1;

    while (fib1 <= numberToCheck) {
        if (fib1 === numberToCheck) {
            return true;
        }
        let temp = fib1 + fib2;
        fib1 = fib2;
        fib2 = temp;
    }
}

function isPrime(numberToCheck) {
    if (numberToCheck > 1) {
        for (let i = 2; i < numberToCheck; i++) {
            if (numberToCheck % i == 0) {
                return false;
            }
        }
        return true;
    }
    return false;
}


function numberChecker(numberToCheck) {
    let evenText = isEven(numberToCheck) ? "even" : "odd";
    let fibonacciText = isFibonacci(numberToCheck) ? "Fibonacci" : "not Fibonacci";
    let primeText = isPrime(numberToCheck) ? "prime" : "not prime";

    console.log(`Your given number: ${numberToCheck}, is ${evenText}, ${fibonacciText} and ${primeText}`);
}

numberChecker(1);
numberChecker(2);
numberChecker(5);
numberChecker(7);
numberChecker(12);