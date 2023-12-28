const isEven = (number) => number % 2 === 0
const isPrime = (number) => {
  for (let i = 2; i < number / 2; i++) {
    if (number % i === 0) return false
  }
  return true
}

const isFibonacci = (number) => {
  return number === getFibonacci(number)
}

const getFibonacci = (limit) => {
  let prev = 0
  let next = 1
  let fibonacci = prev + next

  while (fibonacci < limit) {
    prev = next
    next = fibonacci
    fibonacci = prev + next
  }

  return fibonacci
}

const printEvenPrimeFibonacciNumber = (number) => {
  const prime = { true: 'is prime', false: 'is not prime' }
  const fibonacci = { true: 'is fibonacci', false: 'is not fibonacci' }
  const even = { true: 'is even', false: 'is odd' }

  return `${number} ${prime[isPrime(number)]}, ${
    fibonacci[isFibonacci(number)]
  } and ${even[isEven(number)]}`
}

const testSamples = [
  {
    testName: 'Should be prime, odd and fibonacci',
    input: 1,
    expectedOutput: '1 is prime, is fibonacci and is odd',
  },
  {
    testName: 'Should be prime, even and fibonacci',
    input: 2,
    expectedOutput: '2 is prime, is fibonacci and is even',
  },
  {
    testName: 'Should not be prime, even and not fibonacci',
    input: 14,
    expectedOutput: '14 is not prime, is not fibonacci and is even',
  },
  {
    testName: 'Should be prime, odd and not fibonacci',
    input: 17,
    expectedOutput: '17 is prime, is not fibonacci and is odd',
  },
  {
    testName: 'Should not be prime, odd and fibonacci',
    input: 21,
    expectedOutput: '21 is not prime, is fibonacci and is odd',
  },
]

const runTests = () => {
  const passedTests = testSamples.filter((sample, idx) => {
    const { testName, input, expectedOutput } = sample

    const printOutput = printEvenPrimeFibonacciNumber(input)
    const areEquals = expectedOutput === printOutput

    const LOG_TEST_NUMBER = `Test ${idx + 1}: ${testName}`
    const LOG_TEST_RESULT = areEquals ? 'PASSED' : 'FAILED'
    console.log(
      `${LOG_TEST_NUMBER}: ${LOG_TEST_RESULT}\n\tInput: ${input}\n\tExpected: ${expectedOutput}\n\tGot: ${printOutput}\n`
    )

    return areEquals
  }).length

  console.log(`Tests ${passedTests} of ${testSamples.length} passed`)
}

runTests()
