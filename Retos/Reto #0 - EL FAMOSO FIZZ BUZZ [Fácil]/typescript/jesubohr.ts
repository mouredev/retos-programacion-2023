// @ts-ignore
function FizzBuzz (limit: number) {
  return Array.from({ length: limit }, (_, i) => i + 1)
    .map((num) => {
      return (num % 15 === 0) ? 'fizzbuzz'
        : (num % 5 === 0) ? 'buzz'
        : (num % 3 === 0) ? 'fizz'
        : num
    })
    .join(' ')
}

console.log(FizzBuzz(100))
