const ERROR_LENGTH_NOT_IN_THRESHOLD = 'Password length must be between 8 or 16'

const LETTERS = 'abcdefghijklmnopqrstuvwxyz'
const NUMBERS = '0123456789'
const SYMBOLS = '!#@~$%&/()=^*.,-_'

const lengthIsBetweenThresholds = (length) => {
  const MIN_LENGTH = 8
  const MAX_LENGTH = 16
  return length >= MIN_LENGTH && length <= MAX_LENGTH
}

const getRandomIdx = (max) => Math.floor(Math.random() * max)

const generatePassword = ({
  length = 8,
  upper = false,
  numbers = false,
  symbols = false,
}) => {
  if (!lengthIsBetweenThresholds(length))
    throw new Error(ERROR_LENGTH_NOT_IN_THRESHOLD)

  let password = ''
  let values = LETTERS
  if (upper) {
    password += LETTERS.charAt(getRandomIdx(LETTERS.length)).toUpperCase()
    values += LETTERS.toUpperCase()
  }

  if (numbers) {
    password += NUMBERS.charAt(getRandomIdx(NUMBERS.length))
    values += NUMBERS
  }

  if (symbols) {
    password += SYMBOLS.charAt(getRandomIdx(SYMBOLS.length))
    values += SYMBOLS
  }

  for (let i = password.length; i < length; i++) {
    const idx = getRandomIdx(values.length)
    password += values.charAt(idx)
  }

  return password
}

// Test Sandbox block
const testSamples = [
  {
    testName: 'Should throw Error length above the thresholds',
    input: {
      length: 17,
      upper: true,
      numbers: true,
      symbols: true,
    },
    expectedOutput: ERROR_LENGTH_NOT_IN_THRESHOLD,
  },
  {
    testName: 'Should throw Error length below the thresholds',
    input: {
      length: 7,
      upper: true,
      numbers: true,
      symbols: true,
    },
    expectedOutput: ERROR_LENGTH_NOT_IN_THRESHOLD,
  },
  {
    testName:
      'Should return password without upper letters, numbers and symbols',
    input: {
      length: 8,
      upper: false,
      numbers: false,
      symbols: false,
    },
    regex: /^[a-z]+$/g,
    expectedOutput: true,
  },
  {
    testName:
      'Should return password with upper and lower letters and without numbers and symbols',
    input: {
      length: 8,
      upper: true,
      numbers: false,
      symbols: false,
    },
    regex: /^[a-z]+$/gi,
    expectedOutput: true,
  },
  {
    testName:
      'Should return password with upper and lower letters and without numbers and symbols',
    input: {
      length: 8,
      upper: true,
      numbers: false,
      symbols: false,
    },
    regex: /^[a-z]+$/gi,
    expectedOutput: true,
  },
  {
    testName:
      'Should return password with upper and lower letters, numbers and without symbols',
    input: {
      length: 8,
      upper: true,
      numbers: true,
      symbols: false,
    },
    regex: /(?=.*[a-zA-Z])(?=.*[0-9])/g,
    expectedOutput: true,
  },
  {
    testName:
      'Should return password with upper and lower letters, numbers and symbols',
    input: {
      length: 8,
      upper: true,
      numbers: true,
      symbols: true,
    },
    regex: /(?=.*[a-zA-Z])(?=.*[0-9])(?=.*[!#@~$%&\/()=^*.,\-_])/g,
    expectedOutput: true,
  },
]

const runTests = () => {
  const passedTests = testSamples.filter((test) => {
    const { testName, input, expectedOutput, regex } = test
    let output = ''
    let IS_EXPECTED_RESULT = false
    let LOG_TEST_RESULT_GOT = ''
    try {
      output = generatePassword(input)
      IS_EXPECTED_RESULT = output.match(regex).length > 0
      LOG_TEST_RESULT_GOT = `\n\tGot: ${IS_EXPECTED_RESULT},\n\tPassword generated: ${output}`
    } catch (e) {
      output = e.message
      IS_EXPECTED_RESULT = output === expectedOutput
      LOG_TEST_RESULT_GOT = `\n\tGot: ${output}`
    }
    const LOG_TEST_NAME = `Test ${testName}`
    const LOG_TEST_RESULT = IS_EXPECTED_RESULT ? 'PASSED' : 'FAILED'
    console.log(
      `${LOG_TEST_NAME}: ${LOG_TEST_RESULT}\n\tInput: ${JSON.stringify(
        input
      )}\n\tExpected: ${expectedOutput}${LOG_TEST_RESULT_GOT}`
    )

    return IS_EXPECTED_RESULT
  }).length

  console.log(`Tests ${passedTests} of ${testSamples.length} passed`)
}

runTests()
