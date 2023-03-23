const leetAlphabet = {
  a: "4",
  b: "I3",
  c: "[",
  d: ")",
  e: "3",
  f: "|=",
  g: "&",
  h: "#",
  i: "1",
  j: ",_|",
  k: ">|",
  l: "1",
  m: "/\\/\\",
  n: "^/",
  o: "0",
  p: "|*",
  q: "(_,)",
  r: "I2",
  s: "5",
  t: "7",
  u: "(_)",
  v: "\\/",
  w: "\\/\\/",
  x: "><",
  y: "j",
  z: "2",
  0: "0",
  1: "L",
  2: "R",
  3: "E",
  4: "A",
  5: "S",
  6: "b",
  7: "T",
  8: "B",
  9: "g",
};

const mapToLeet = (word) => leetAlphabet[word.toLowerCase()] || word;

const convertToLeet = (text) => text.split("").map(mapToLeet).join("");

const textSamples = [
  {
    input: "Hola mundo, reto de programación 1 en lenguaje leet! :D",
    expectedOutput:
      "#014 /\\/\\(_)^/)0, I2370 )3 |*I20&I24/\\/\\4[1ó^/ L 3^/ 13^/&(_)4,_|3 1337! :)",
  },
  {
    input: "hola HOLA",
    expectedOutput: "#014 #014",
  },
  {
    input: "0123456789",
    expectedOutput: "0LREASbTBg",
  },
  {
    input: "mM",
    expectedOutput: "/\\/\\/\\/\\",
  },
  {
    input: "vV",
    expectedOutput: "\\/\\/",
  },
  {
    input: "wW",
    expectedOutput: "\\/\\/\\/\\/",
  },
];

const runTests = () => {
  const passedTests = textSamples.filter((sample, idx) => {
    const { input, expectedOutput } = sample;

    const leetInput = convertToLeet(input);
    const isWellConverted = expectedOutput === leetInput;

    const LOG_TEST_NUMBER = `Test ${idx + 1}:`;
    const LOG_TEST_RESULT = isWellConverted ? "PASSED" : "FAILED";
    console.log(
      `${LOG_TEST_NUMBER}: ${LOG_TEST_RESULT}\n\tInput: ${input}\n\tExpected: ${expectedOutput}\n\tGot: ${leetInput}\n`
    );

    return isWellConverted;
  }).length;

  console.log(`Tests ${passedTests} of ${textSamples.length} passed`);
};

runTests();
