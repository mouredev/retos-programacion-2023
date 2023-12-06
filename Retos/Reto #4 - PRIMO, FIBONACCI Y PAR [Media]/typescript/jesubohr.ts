function numberIsTypes(number: number) {
  let result = `${number}`
  result += (isPrime(number) ? " es primo" : " no es primo") + ","
  result += (isFibonacci(number) ? " es fibonacci" : " no es fibonacci") + " y"
  result += number % 2 === 0 ? " es par" : " es impar"
  return result
}

function isPrime(number: number) {
  if (number < 2) return false
  for (let i = 2; i < number; i++) {
    if (number % i === 0) return false
  }
  return true
}

const isFibonacci = (number: number) => 
  isPerfectSquare(5 * (number ** 2) + 4) ||
  isPerfectSquare(5 * (number ** 2) - 4)
  
const isPerfectSquare = (number: number) =>
  Math.sqrt(number) === Math.floor(Math.sqrt(number))


// Test
for (let i = 0; i < 10; i++) {
  const random = Math.floor(Math.random() * 100)
  console.log(numberIsTypes(random))
}
