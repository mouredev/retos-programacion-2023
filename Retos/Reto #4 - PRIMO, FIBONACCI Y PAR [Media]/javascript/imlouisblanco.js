function buildAnswer(n) {
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
    let count = fibonacci.length;

    while (fibonacci[count-1] < n){
        let newPosition = fibonacci[count-1] + fibonacci[count-2];

        fibonacci.push(newPosition);
        count += 1;
    }

    return fibonacci;
}

function isEven(n){
   return n % 2 === 0;
}

// Examples
console.log(buildAnswer(0)) // "el número ingresado no es válido"
console.log(buildAnswer(1)) // "no es primo, es fibonacci y no es par"
console.log(buildAnswer(2)) // "es primo, es fibonacci y es par"
console.log(buildAnswer(13)) // "es primo, es fibonacci y no es par"
console.log(buildAnswer(16)) // "no es primo, no es fibonacci y es par"
console.log(buildAnswer(21)) // "no es primo, es fibonacci y no es par"
