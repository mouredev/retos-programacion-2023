const transformToOctalHex = (number) => {
  return { octal: transformOctal(number), hex: transformHex(number) };
};

const transformOctal = (number) => {
  if (number == 0 || number % 1 != 0) return "0";

  let octal = "";
  let quotient = number;
  let remain = 0;

  while (quotient != 0) {
    remain = quotient % 8;
    quotient = Math.floor(quotient / 8);
    octal = remain + octal;
  }

  return octal;
};

const transformHex = (number) => {
  const hexValues = {
    0: "0",
    1: "1",
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10: "A",
    11: "B",
    12: "C",
    13: "D",
    14: "E",
    15: "F",
  };

  if (number == 0 || number % 1 != 0) return "0";

  let hex = "";
  let quotient = number;
  let remain = 0;

  while (quotient != 0) {
    remain = quotient % 16;
    quotient = Math.floor(quotient / 16);
    hex = hexValues[remain] + hex;
  }
  return hex;
};

// console.log("transformOctalHex 0: ", transformToOctalHex(0));
// console.log("transformOctalHex 16: ", transformToOctalHex(16));
// console.log("transformOctalHex 15: ", transformToOctalHex(15));
