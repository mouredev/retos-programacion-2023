FROM_NUMBER = 1
TO_NUMBER = 100
FIZZBUZZ_MAP = {
  3: 'fizz',
  5: 'buzz',
}

const showFizzBuzzOrNumber = (multipleToTextMap, number) => {
  const result = Object.keys(multipleToTextMap)
    .reduce((text, multiple) => {
      if (number % multiple === 0) {
        return text + multipleToTextMap[multiple]
      } 
      return text
    }, '')

  return result || number
}

const main = () => {
  const numbers = Array.from({length: TO_NUMBER - FROM_NUMBER + 1}, (_, i) => i + FROM_NUMBER)
  const log = numbers.map((number) => showFizzBuzzOrNumber(FIZZBUZZ_MAP, number)).join('\n')
  console.log(log)
}

main()