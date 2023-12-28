function evalNumber(number: number): string {
  let outSentence: string = `${number} `;
  outSentence += isPrime(number) ? "es primo, " : "no es primo, ";
  outSentence += isFibbonacci(number) ? "fibonacci " : "no es fibbonacci ";
  outSentence += isEven(number) ? "y es par" : "y es impar";
  return outSentence;
}

const isPrime = (number: number): boolean => {
  if (number === 2) return true;
  for (let i: number = 2; i < number; i++) {
    if (number % i === 0) return false;
  }
  return true;
};

const isFibbonacci = (
  number: number,
  a: number = 0,
  b: number = 1
): boolean => {
  if (number === 0 || number === 1) return true;
  let nextNumber = a + b;
  if (nextNumber === number) return true;
  if (nextNumber > number) return false;
  return isFibbonacci(number, b, nextNumber);
};

const isEven = (number: number): boolean => {
  return number % 2 === 0;
};

const start = (): void => {
  console.log(evalNumber(2));
  console.log(evalNumber(7));
  console.log(evalNumber(13));
  console.log(evalNumber(8));
  console.log(evalNumber(49));
};

start();
