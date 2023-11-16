const fizzBuzz = (limit: number): void => {
  const numbers = Array.from({ length: limit }, (_, index) => index + 1)
  for (const number of numbers) {
    if (number % 3 === 0) console.log("fizz")
    if (number % 5 === 0) console.log("buzz")
    if (number % 3 === 0 && number % 5 === 0) console.log("fizzbuzz")
    else console.log(number)
  }
}

fizzBuzz(100)
