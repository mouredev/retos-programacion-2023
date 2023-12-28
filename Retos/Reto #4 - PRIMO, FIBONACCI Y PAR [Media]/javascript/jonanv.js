function checkPrimeFibonacciEven(number) {
  let numberPrime = isPrime(number);
  let evenOrOdd = isEvenOrOdd(number);
  let fibonacci = isFibonacci(number);

  return `${ number }` + 
          ` ${ numberPrime ? 'es primo' : 'no es primo' },` +
          ` ${ fibonacci ? 'es fibonacci' : 'no es fibonacci' } y es` +
          ` ${ evenOrOdd ? 'par' : 'impar' }`;
}

function isPrime(number) {
  for (let i = 2; i < number; i++) {
    if (number % i === 0) {
      return false;
    }
  }
  return number !== 1;
}

function isEvenOrOdd(number) {
  if (number % 2 == 0) {
    return true;
  } else {
    return false;
  }
}

function fibonacci(number) {
  if (number > 1) {
    return fibonacci(number - 1) + fibonacci(number - 2);
  } else if (number === 1) {
    return 1;
  } else {
    return 0;
  }
}

function isFibonacci(number) {
  let list = [];
  for (let index = 0; index < number + 2; index++) {
    list.push(fibonacci(index));
  }
  return list.includes(number);
}

console.log(checkPrimeFibonacciEven(0));
console.log(checkPrimeFibonacciEven(1));
console.log(checkPrimeFibonacciEven(2));
console.log(checkPrimeFibonacciEven(7));
console.log(checkPrimeFibonacciEven(8));
console.log(checkPrimeFibonacciEven(14));