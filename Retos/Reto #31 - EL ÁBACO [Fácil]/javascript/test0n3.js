const abacusNumber = (input) => {
  function validString(str) {
    return str.length == 12 && str.includes("---");
  }

  if (input.length == 0) return "Invalid input";
  let stringNumber = "";

  for (let i = 0; i < input.length; i++) {
    if (!validString(input[i])) {
      stringNumber = "Invalid input";
      break;
    }
    stringNumber = `${stringNumber}${
      input[i].slice(0, input[i].indexOf("---")).length
    }`;
    if (i % 3 == 0 && input.length - 1 != i) {
      stringNumber = `${stringNumber}.`;
    }
  }
  return stringNumber;
};

const tests = {
  inputs: [
    ["000---000000", "00000---0000", "000000---000", "---000000000"],
    [
      "O---OOOOOOOO",
      "OOO---OOOOOO",
      "---OOOOOOOOO",
      "OO---OOOOOOO",
      "OOOOOOO---OO",
      "OOOOOOOOO---",
      "---OOOOOOOOO",
    ],
    [],
    ["0--0-0000000", "0000000000"],
  ],
  outputs: ["3.560", "1.302.790", "Invalid input", "Invalid input"],
};

let errors = 0;
tests.inputs.forEach((input, index) => {
  const result = abacusNumber(input);
  if (result != tests.outputs[index]) {
    errors += 1;
    console.log(
      `Error - input: ${input}, expected: ${tests.outputs[index]}, result: ${result}`
    );
  }
});
console.log(`Errors: ${errors}`);
