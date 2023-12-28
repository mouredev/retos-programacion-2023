// Reto #4: PRIMO, FIBONACCI Y PAR

// Resources used to check if a number is prime and/or fibonacci

// Prime: https://sciencing.com/calculate-coprime-6921150.html

// Fibonacci: https://www.quora.com/It-is-easy-to-demonstrate-that-a-number-n-belongs-to-the-Fibonacci-sequence-if-and-only-if-one-or-both-of-5n-2-4-or-5n-2-4-is-a-perfect-square-is-true-How-was-this-discovered-and-can-it-be-algebraically-proved-to-be

function isEven(n) {
  return n % 2 === 0
}

function isFibonacci(n) {
  return (Math.sqrt(5 * n * n + 4) % 1 === 0 ||
          Math.sqrt(5 * n * n - 4) % 1 === 0)
}

function isPrime(n) {
  let k = 2
  while (k <= Math.sqrt(n)) {
    if (n % k === 0) {
      return false
    }
    k++
  }
  return true
}

function main(n) {
  const prime = {true: "es primo", false: "no es primo"}
  const fibonacci = {true: "es fibonacci", false: "no es fibonacci"}
  const even = {true: "es par", false: "es impar"}

  return `${n} ${prime[isPrime(n)]}, ${fibonacci[isFibonacci(n)]} y ${even[isEven(n)]}`
}

console.log(main(2))
console.log(main(5))
console.log(main(7))
console.log(main(8))
console.log(main(11))
console.log(main(13))
console.log(main(21))
console.log(main(22))
