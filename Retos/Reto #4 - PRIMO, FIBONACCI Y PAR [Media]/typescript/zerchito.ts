/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */
class NumberChecker {

  fibonacciNumbers: number[] = [1 , 1];
  
  checkNummber(num: number) {
    const primeCheck = this.#isPrime(num);
    const fibonacciCheck = this.#isFibonacci(num);
    const evenCheck = this.#isEven(num);
    return `${num} ${primeCheck}, ${fibonacciCheck} y ${evenCheck}`;
  }

  #isPrime(num: number): string{
    let primeCheck = true;
    for (let div = 2; num<= Math.sqrt(num); div++) {
      if(num%div === 0){
        primeCheck = false;
        break;
      }
    }
    return primeCheck ? 'es primo': 'no es primo';
  }

  #isFibonacci(num: number): string {
    let lastIndex = this.fibonacciNumbers.length - 1;
    let lastFibonacci = this.fibonacciNumbers[lastIndex];
    let fiboCheck = false;
    if (this.fibonacciNumbers.includes(num)) {
      fiboCheck = true;
    } else if (num > lastFibonacci) {
      while (num > lastFibonacci) {
        const newFibonacci = lastFibonacci + this.fibonacciNumbers[lastIndex-1];
        lastFibonacci = newFibonacci;
        this.fibonacciNumbers.push(newFibonacci);
        lastIndex++;
        fiboCheck = num === newFibonacci;
      }
    }

    return fiboCheck ? 'es fibonacci' : 'no es fibonacci';
  }

  #isEven(num: number): string {
    return num % 2 ? 'es par' : 'es impar'; 
  }
}

const checker = new NumberChecker();
console.log(checker.checkNummber(2))
console.log(checker.checkNummber(7))