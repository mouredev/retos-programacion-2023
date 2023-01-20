// @ts-ignore
function FizzBuzz (limit: number) {
  return Array.from({ length: limit }, (_, i) => i + 1)
    .map((num) => {
      return (num % 15 === 0) ? 'FizzBuzz'
        : (num % 5 === 0) ? 'Buzz'
        : (num % 3 === 0) ? 'Fizz'
        : num
    })
    .join(' ')
}

console.log(FizzBuzz(45))
