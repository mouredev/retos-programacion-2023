/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */

function isPrime(number){
	if(number > 1){

		for(let i = 2; i < number; i++){
			if (number % i === 0){
				return false;
			}
		}
		return true;
	}
	else {
		return false;
	}
}
  
function fibonacci(number){
	if (number === 0){
		return 0;
	}
	else if (number === 1){
		return 1;
	} 
	else{
		return fibonacci(number-1) + fibonacci(number-2);
	}
}
  
function isFibonacci(number){
	var sequence = [fibonacci(0)];
	let counter = 0;
	
	while(sequence[counter] < number){
		counter++;
		sequence.push(fibonacci(counter));
	}
	
	if(sequence[counter] === number){
		return true;
	}
	
	return false;
}
  
function isEven(number){
	if(number % 2 === 0){
		return true;
	}
	return false;
}
  
  
function checkNumber(number){
	let text;
	if(number > -1){
		text = number + " is ";

		if(!isPrime(number)){
			text += "not ";
		}
		
		text += "prime, ";

		if(!isFibonacci(number)){
			text += "is not ";
		}
		text += "fibonacci and is ";

		if(isEven(number)){
			text += "even";
		}
		else{
			text += "odd";
		} 
	}
	else{
		text = "Negative number";
	}
	return text;	
}

console.log(checkNumber(2));
console.log(checkNumber(7));
console.log(checkNumber(8));
console.log(checkNumber(16));
console.log(checkNumber(17));
console.log(checkNumber(0));
console.log(checkNumber(89));
console.log(checkNumber(97));
console.log(checkNumber(100));
console.log(checkNumber(1));
console.log(checkNumber(-1));