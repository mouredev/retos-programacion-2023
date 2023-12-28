// prettier-ignore
const ALPHABET = [
  "a", "b", "c", "d", "e",
  "f", "g", "h", "i", "j",
  "k", "l", "m", "n", "o",
  "p", "q", "r", "s", "t",
  "u", "v", "w", "x", "y",
  "z",
];

const excelColToNumber = (input: string): number => {
  const letters = input.toLocaleLowerCase().split("").reverse();
  const result = letters.reduce((prev, current, currentIndex) => {
    const result =
      (ALPHABET.indexOf(current) + 1) * ALPHABET.length ** currentIndex;
    return result + prev;
  }, 0);
  return result;
};

console.log(excelColToNumber("A"));
console.log(excelColToNumber("Z"));
console.log(excelColToNumber("aa"));
console.log(excelColToNumber("ca"));
console.log(excelColToNumber("bc"));
console.log(excelColToNumber("jc"));
console.log(excelColToNumber("ABc"));
console.log(excelColToNumber("AAA"));
