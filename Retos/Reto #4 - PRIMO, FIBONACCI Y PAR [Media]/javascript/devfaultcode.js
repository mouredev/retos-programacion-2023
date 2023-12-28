/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */

const prompt = require('prompt-sync')();

function primeNumber(number) {
	// Special Cases
	if (number == 0 || number == 1 || number == 4) return false;
	for (let x = 2; x < number / 2; x++) {
		if (number % x == 0) return false;
	}
	// If it could not be divided by any of the above, it is prime
	return true;
}

function fibonacciNumber(number) {
    let fibo1 = 0
    let fibo2 = 1
    let fibo3 = 0

    if(number === 0 || number === 1){ 
        return true
    } else

    while(fibo3 <= number){
        if(fibo3 === number){
            return true
        } else {
            fibo3 = fibo1 + fibo2
            fibo1 = fibo2
            fibo2 = fibo3
        }
    }
    return false
}

function evenNumber(number) {
    if(number % 2 === 0) {
        return true
    } else {
        return false
    }
}

function menu() {

    while (1 === 1) {
        let answer = prompt ('Do you wish to find out if a number is: prime, fibonacci and even? (y or n): ')

        if (answer === 'y' || answer === 'Y') {
            let primeNum
            let fibonacciNum
            let evenNum

            while (1 === 1) {
                let number = prompt('Enter a number: ')

                if (isNaN(number)) {
                    console.log('Please enter a valid number');
                } else {
                    number = parseInt(number)
                    if(primeNumber(number)) {
                        primeNum = 'Is prime'
                    } else {
                        primeNum = 'Is not prime'
                    }

                    if(fibonacciNumber(number)) {
                        fibonacciNum = 'is fibonacci'
                    } else {
                        fibonacciNum = 'is not fibonacci'
                    }

                    if(evenNumber(number)) {
                        evenNum = 'is even'
                    } else {
                        evenNum = 'is odd'
                    }
                    

                    console.log('\n'+ number + ' ' + primeNum + ', ' + fibonacciNum + ', '+ evenNum +'\n'); 
                    break
                }
            }

        } else if (answer === 'n' || answer === 'N'){
            break
        }
    }
}

menu()