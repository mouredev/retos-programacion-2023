const stringFeatures = (inputString) => {
  if (inputString.length == 0) return [false, false, false];

  const hash = countChars(normalizeText(inputString));
  return [heterogram(hash), isogram(hash), pangram(hash)];
};

const countChars = (input) => {
  let chars = {};

  for (let index = 0; index < input.length; index++) {
    if (!Object.keys(chars).includes(input[index])) {
      chars[input[index]] = 0;
    }
    chars[input[index]] += 1;
  }
  return chars;
};

const normalizeText = (input) => {
  let text = input
    .toLowerCase()
    .split("")
    .filter((elem) => !".,;: ".split("").includes(elem))
    .join("");

  const specialVowels = "áéíóúüñ";
  const chars = "aeiouun";
  for (let index = 0; index < specialVowels.length; index++) {
    text = text.replaceAll(specialVowels[index], chars[index]);
  }

  return text;
};

const heterogram = (input) => {
  if (Object.keys(input).length == 0) return false;

  return Object.values(input).every((element) => element == 1);
};

const isogram = (input) => {
  if (Object.keys(input).length == 0) return false;

  const minVal = Math.min.apply(Math, Object.values(input));
  return Object.values(input).every((element) => element == minVal);
};

const pangram = (input) => {
  const alphabet = "abcdefghijklmnopqrstuvwxyz".split("");
  return JSON.stringify(Object.keys(input).sort()) == JSON.stringify(alphabet);
};

const tests = {
  input: [
    "centrifugadlos",
    "shanghaiings",
    "nana",
    "a",
    "",
    "Benjamín pidió una bebida de kiwi y fresa. Noé, sin vergüenza, la más exquisita champaña del menú",
  ],
  output: [
    [true, true, false],
    [false, true, false],
    [false, true, false],
    [true, true, false],
    [false, false, false],
    [false, false, true],
  ],
};

let errors = 0;
tests.input.forEach((test, index) => {
  let resp = stringFeatures(test);
  let expected = tests.output[index];
  if (JSON.stringify(resp) != JSON.stringify(expected)) {
    errors += 1;
    console.log("\noriginal: ", test);
    console.log(resp);
    console.log("expected:", expected);
  }
});

console.log(`Tests${errors != 0 ? " not " : " "}passed, ${errors} errors`);
