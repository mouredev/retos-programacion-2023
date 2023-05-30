function checkPrimoFibonacciAndPar(number) { 
  let result = "";
  let fibonacci = [1, 1];

  // primo 
  if (number % 2 === 0 && number % 3 === 0 && number % 5 === 0 && number % 7 === 0 && number % 11 === 0) {
    result += ' no es primo, '
  } else {
    result += ' es primo, '
  }

  // fibonacci
  for (let i = 1; i < number; i++) {
    let nextNumber = fibonacci[i] + fibonacci[i - 1];
    fibonacci.push(nextNumber);
    if (nextNumber === number) {
      break;
    }
    console.log(fibonacci.length);
  }
  if (fibonacci[fibonacci.length - 1] === number) {
    result += 'es fibonacci y'
  } else {
    result += 'no es fibonacci y'
  }

  // par
  if (number % 2 === 0) {
    result += ' es par'
  } else {
    result += ' es impar'
  }
  console.log(number + result);
};

checkPrimoFibonacciAndPar(2);
checkPrimoFibonacciAndPar(7);
