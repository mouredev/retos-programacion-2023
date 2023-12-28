const findDiff = (sentence1, sentence2) => {
  let diff = [];
  if (sentence1.length != sentence2.length) {
    return false;
  }
  for (let i = 0; i < sentence1.length; i++) {
    if (sentence1[i] != sentence2[i]) {
      diff.push(sentence2[i]);
    }
  }
  return diff;
};

const tests = {
  input: [
    ["Me llamo mouredev", "Me llemo mouredov"],
    ["Me llamo.Brais Moure", "Me llamo brais moure"],
    ["first sentence", "second sentence"],
    ["first  sentence", "second sentence"],
  ],
  expecteds: [
    ["e", "o"],
    [" ", "b", "m"],
    false,
    ["s", "e", "c", "o", "n", "d"],
  ],
};

let errors = 0;
tests.input.forEach((test, index) => {
  const result = findDiff(test[0], test[1]);
  if (JSON.stringify(result) == JSON.stringify(tests.expecteds[index])) {
    console.log(
      `Success - input: ${test[0]}, ${test[1]}, expected: ${tests.expecteds[index]}`
    );
  }
  if (JSON.stringify(result) != JSON.stringify(tests.expecteds[index])) {
    errors += 1;
    console.log(
      `Error - input: ${test[0]},${test[1]}, expected: ${tests.expecteds[index]}, result: ${result}`
    );
  }
});
console.log(`Errors: ${errors}`);
