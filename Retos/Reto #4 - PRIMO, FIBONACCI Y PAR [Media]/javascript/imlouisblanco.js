function getValidation(n) {
    if (!isValidInput(n)){
        return 'el número ingresado no es válido';
    }

    const translations = [
        isPrime(n) ? 'es primo,' : 'no es primo,',
        isFibonacci(n) ? 'es fibonacci' : 'no es fibonacci',
        isEven(n) ? 'y es par' : 'y no es par'
    ]

    return translations.join(' '); 
}

function isValidInput(n) {
    //I decided to accept only natural numbers
    return n >= 1;
}

function isPrime(n) {
    if (n === 1){
        return false;
    }

    if (n === 2){
        return true;
    }

    for (let i = 2; i < n; i++){
        if (n % i === 0) return false;
    }

    return true;
}

function isFibonacci(n) {
    if (n < 4){
        return true;
    }

    return getFibonacciNumbers(n).includes(n);
}

function getFibonacciNumbers(n) {
    let fibonacci = [0, 1];

    while (fibonacci[fibonacci.length - 1] < n){
        let newPosition = fibonacci[fibonacci.length - 1] + fibonacci[fibonacci.length - 2];

        fibonacci.push(newPosition);
    }

    return fibonacci;
}

function isEven(n) {
   return n % 2 === 0;
}

// Examples
console.log(getValidation(0)); // "el número ingresado no es válido"
console.log(getValidation(1)); // "no es primo, es fibonacci y no es par"
console.log(getValidation(2)); // "es primo, es fibonacci y es par"
console.log(getValidation(13)); // "es primo, es fibonacci y no es par"
console.log(getValidation(16)); // "no es primo, no es fibonacci y es par"
console.log(getValidation(21)); // "no es primo, es fibonacci y no es par"
