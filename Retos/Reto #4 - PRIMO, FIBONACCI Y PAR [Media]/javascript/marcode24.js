/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */

const isPrimeFibonnaciEven = (n) => {
  const isPrime = (num) => {
    for (let i = 2; i < num; i++) {
      if (num % i === 0) return false;
    }
    return num > 1;
  };

  const isFibonnaci = (num) => {
    const fibonnaci = [0, 1];
    let i = 2;
    while (fibonnaci[i - 1] < num) {
      fibonnaci.push(fibonnaci[i - 1] + fibonnaci[i - 2]);
      i += 1;
    }
    return fibonnaci.includes(num);
  };

  const isEven = (num) => num % 2 === 0;

  return {
    prime: isPrime(n),
    fibonnaci: isFibonnaci(n),
    even: isEven(n),
  };
};

// Visita mi repo en GitHub para ver y correr los tests de este código --> https://github.com/marcode24/weekly-challenges
