const toOctal = decimal => (toBase(decimal, 8))
const toBinary = decimal => (toBase(decimal, 2))

const toBase = (decimal, base = 8) => {
  return decimal < base ? decimal : toBase(Math.floor(decimal / base), base) * 10 + decimal % base
}

const tests8 = [ 
  { input: 0, expectedOutput: 0 },
  { input: 7, expectedOutput: 7 },
  { input: 8, expectedOutput: 10 },
  { input: 9, expectedOutput: 11 },
  { input: 34, expectedOutput: 42 },
  { input: 312, expectedOutput: 470 },
  { input: 670, expectedOutput: 1236 },
]

for (const { input, expectedOutput } of tests8) {
  console.log(toOctal(input) === expectedOutput ? 
    'toOctal:PASS' : 
    `toOctal:FAIL, for input ${input} expected was ${expectedOutput} but got ${toOctal(input)}`
  )
}

const tests2 = [ 
  { input: 0, expectedOutput: 0 },
  { input: 1, expectedOutput: 1 },
  { input: 2, expectedOutput: 10 },
  { input: 4, expectedOutput: 100 },
  { input: 9, expectedOutput: 1001 },
  { input: 43, expectedOutput: 101011 },
  { input: 1234, expectedOutput: 10011010010 },
]

for (const { input, expectedOutput } of tests2) {
  console.log(toBinary(input) === expectedOutput ? 
    'toBinary:PASS' : 
    `toBinary:FAIL, for input ${input} expected was ${expectedOutput} but got ${toOctal(input)}`
  )
}