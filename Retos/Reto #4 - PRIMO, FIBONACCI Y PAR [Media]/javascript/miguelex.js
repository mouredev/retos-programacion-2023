const CheckNumber = (number) => {
    let isPrime = isPrimeNumber(number) ? "es primo, " : "no es primo, ";
    let isEven = isEvenNumber(number) ? "es par y " : "no es par y ";
    let isFibonacci = isFibonacciNumber(number) ? "es un numero de Fibonacci" : "no es numero de Fibonacci";

    return "El numero " + number + " " + isPrime + isEven + isFibonacci;
}

const isPrimeNumber = (number) => {
    let isPrime = true;
    for (let i = 2; i < number; i++) {
        if (number % i == 0) {
            isPrime = false;
        }
    }
    return isPrime;
}

const isEvenNumber = (number) => {
    return number % 2 == 0;
}

const isFibonacciNumber = (number) => {
    let a = 0;
    let b = 1;
    let c = 0;
    while (c < number) {
        c = a + b;
        a = b;
        b = c;
    }
    return c == number;
}

console.log(CheckNumber(1));
console.log(CheckNumber(2));
console.log(CheckNumber(3));
console.log(CheckNumber(4));
console.log(CheckNumber(5));
console.log(CheckNumber(6));
console.log(CheckNumber(7));
console.log(CheckNumber(8));
console.log(CheckNumber(9));
console.log(CheckNumber(10));
console.log(CheckNumber(1024));
console.log(CheckNumber(358742586));
