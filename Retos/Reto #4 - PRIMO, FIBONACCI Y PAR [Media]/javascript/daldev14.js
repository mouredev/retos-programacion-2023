/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo,
 * fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */

const isPar = (number) => number % 2 === 0

const isPrime = (number) => {
  if (number <= 1 || number == 4) return false

  for (let i = 2; i < number / 2; i++) {
    if (number % i === 0) return false
  }

  return true
}

const isFibonacci = (number) => {
  if (number < 0) return false

  let a = 0
  let b = 1

  while (b < number) {
    const aux = a
    a = b
    b = aux + b
  }

  return number === b
}

function compareNumber(number) {
  let response = `${number}`
  response += isPrime(number) ? " es primo," : " no es primo,"
  response += isFibonacci(number) ? " fibonacci" : " no es fibonacci"
  response += isPar(number) ? " y es par" : " y no es par"

  return response
}

console.log(compareNumber(2)) // 2 es primo, fibonacci y es par
console.log(compareNumber(7)) // 7 es primo, no es fibonacci y no es par
console.log(compareNumber(9)) // 9 no es primo, no es fibonacci y no es par
