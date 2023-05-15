const TEST_NUMBER = Math.floor(Math.random() * 150);

function fibonacci(fibonacci = 0) {
  let n1 = 0,
    n2 = 1,
    nextTerm,
    find;
  const arr = [0];
  for (let i = 1; i <= fibonacci + 1; i++) {
    nextTerm = n1 + n2;
    n1 = n2;
    n2 = nextTerm;
    arr.push(n1);
    find = arr.some((element) => element === fibonacci);
    if (find) {
      return find ? ", es fibonacci" : null;
    }
  }
  return !find ? ", no es fibonacci" : null;
}

function primeNumber(primeNumber) {
  let prime = 0,
    primeCounter = 0;
  for (let i = 1; i <= primeNumber; i++) {
    prime = primeNumber % i;
    if (!prime) {
      primeCounter++;
    }
  }
  return primeCounter === 2 ? ", es primo" : ", no es primo";
}

function evaluate(testNumber) {
  let response =
    `${testNumber}` + primeNumber(testNumber) + fibonacci(testNumber);

  response += testNumber % 2 === 0 ? " y es par" : " y es impar";

  return response;
}

console.log(evaluate(TEST_NUMBER));
