// Clase para verificar si un número es par o impar
class ParImparChecker {
    esParImpar(numero) {
      return numero % 2 === 0 ? "Es Par" : "Es Impar";
    }
  }
  
  // Clase para verificar si un número es primo
  class PrimoChecker {
    esPrimo(numero) {
      if (numero <= 1) {
        return "No es primo";
      }
      for (let i = 2; i < numero; i++) {
        if (numero % i === 0) {
          return "No es primo";
        }
      }
      return "Es primo";
    }
  }
  
  // Clase para verificar si un número es parte de la secuencia Fibonacci
  class FibonacciChecker {
    esFibonacci(numero) {
      let a = 0;
      let b = 1;
      while (a < numero) {
        let temp = a;
        a = b;
        b = temp + b;
      }
      return a === numero ? "Es parte de la secuencia Fibonacci" : "No es parte de la secuencia Fibonacci";
    }
  }
  
  const parImparChecker = new ParImparChecker();
  const primoChecker = new PrimoChecker();
  const fibonacciChecker = new FibonacciChecker();
  
  const numero1 = 2;
  const numero2 = 7;
  
  console.log(`El numero ${numero1}: ${primoChecker.esPrimo(numero1)}, ${fibonacciChecker.esFibonacci(numero1)}, ${parImparChecker.esParImpar(numero1)}`);
  console.log(`El numero ${numero2}: ${primoChecker.esPrimo(numero2)}, ${fibonacciChecker.esFibonacci(numero2)}, ${parImparChecker.esParImpar(numero2)}`);