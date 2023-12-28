const checkNumber = (number) => {
    let isPrime = true;
    let isFibonacci = false;
    let isEven = false;
    
    for (i = 2; i < number; i++) {
        if (number % i == 0) {
            isPrime = false;
            break;
        }
    }
    console.log(isPrime ? "Es un número primo" : "No es un número primo");
    
    
    const firstDifferenceSquare = Math.round(Math.sqrt(5 * number * number + 4));
    const secondDifferenceSquare = Math.round(Math.sqrt(5 * number * number - 4));
    
    isFibonacci = firstDifferenceSquare * firstDifferenceSquare == (5 * number * number + 4) ||  secondDifferenceSquare * secondDifferenceSquare == (5 * number * number - 4);
    console.log(isFibonacci ? "Es un número de fibonacci" : "No es un número de fibonacci");
    
    
    
    if (number % 2 == 0) isEven = true;
    console.log(isEven ? "Es un número par" : "No es un número par");        
}

checkNumber(22);
