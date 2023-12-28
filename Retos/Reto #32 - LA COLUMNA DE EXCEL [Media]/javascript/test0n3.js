const columnCounter = (input) => {
  const newInput = input.toUpperCase();
  if (!newInput.match(/^[A-Z]+$/)) {
    return "invalid input";
  }
  return newInput
    .split("")
    .reverse()
    .reduce((accum, digit, index) => {
      return accum + (digit.charCodeAt(0) - 64) * 26 ** index;
    }, 0)
    .toString();
};

/* Testing */
const tests = {
  inputs: ["A", "CA", "zza", "", "1A"],
  expected: ["1", "79", "18253", "invalid input", "invalid input"],
};

let errors = 0;
tests.inputs.forEach((digit, index) => {
  const result = columnCounter(digit);
  console.log(`digit: ${digit}, result: ${result}`);
  if (result != tests.expected[index]) {
    errors += 1;
    console.log(
      `Error - input: ${digit}, expected: ${tests.expected[index]}, result: ${result}`
    );
  }
});
console.log(`Errors: ${errors}`);
