/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */

const isEven = (number) => {
   if (number % 2 === 0) {
      return "Es par"
   } else {
      return "Es impar"
   }
}

const isFibonacci = (number) => {
   let previusNumber = 0;
   let nextNumber = 1;
   while (previusNumber < number) {
      const temp = previusNumber;
      previusNumber = nextNumber;
      nextNumber = temp + nextNumber;
   }
   if (previusNumber === number) {
      return "es fibonacci"
   } else {
      return "no es fibonacci"
   }
}

const isPrime = (number) => {
   // los numeros menores que 1 no son primos
   if (number <= 1) {
      return "no es primo"
   }
   // comprueba que es divisible por un numero desde 2 hasta la raiz cuadrada del numero
   for (let i = 2; i <= Math.sqrt(number); i++) {
      if (number % i === 0) {
         return 'no es primo'
      }
   }
   return "es primo"
}

// genera valores enteros aleatorios entre 0 y 1000
const number = Math.floor(Math.random() * 1000)

console.log(`El numero ==> ${number} ${isEven(number)}, ${isFibonacci(number)} y ${isPrime(number)}.`)




