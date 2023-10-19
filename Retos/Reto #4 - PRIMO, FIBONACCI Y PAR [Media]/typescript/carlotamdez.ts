/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */

const validateNum = (num: number): void => {
  let primo: boolean = false;
  let fibonacci: boolean = false;
  let par: boolean = false;
  let impar: boolean = false;

  if(num%2) par = true;
  else impar = true;
  if(isFibonacci(num)) fibonacci = true;
  if(isPrimo(num)) primo = true;

  const enumPrimo = primo == true? ' es primo': ' no es primo';
  const enumPar = par == true? ' y es par ': ' y es impar';
  const enumFibonacci = fibonacci==true? ', fibonacci ' :', no es fibonacci ';
  
  console.log(`El numero ${num} ${enumPrimo} ${enumFibonacci} ${enumPar}`)
}


function isFibonacci(number :number): boolean {
  function isPerfectSquare(x: number) {
    const sqrt = Math.sqrt(x);
    return sqrt === Math.floor(sqrt);
  }

  return (
    isPerfectSquare(5 * number * number + 4) ||
    isPerfectSquare(5 * number * number - 4)
  );
}

function isPrimo(num : number) {
  if (num <= 1) return false; 
  if (num <= 3) return true;
  if (num % 2 === 0 || num % 3 === 0) return false;

  for (let i = 5; i * i <= num; i += 6) {
    if (num % i === 0 || num % (i + 2) === 0) {
      return false; 
    }
  }
  return true; 
}


validateNum(57465345)
