//prettier-ignore
const HEXAREF = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"];

type RGB = [number, number, number];
type HEXA = `#${string}`;

const numberToHexa = (num: number): string[] => {
  let dividend = num;
  const divisor = HEXAREF.length;
  const hexaValues: string[] = [];

  if (dividend < divisor) return ["0", HEXAREF[dividend]];

  while (dividend >= divisor) {
    const quotient = Math.floor(dividend / divisor);
    const remainder = dividend % divisor;
    hexaValues.push(HEXAREF[remainder]);
    dividend = quotient;
    if (dividend < divisor) {
      hexaValues.push(HEXAREF[dividend]);
      break;
    }
  }

  return hexaValues.reverse();
};

const rgbToHex = (rgbColor: RGB) => {
  let hexaLetters: string[] = [];
  rgbColor.forEach((decimal) => {
    hexaLetters = [...hexaLetters, ...numberToHexa(decimal)];
  });
  return ["#", ...hexaLetters].join("");
};

const hexToRgb = (hexaColor: HEXA): RGB => {
  const hexaValue = hexaColor.substring(1).toLowerCase();
  const pairs: string[] = [];
  let count = 0;
  let pair = "";

  for (let i = 0; i < hexaValue.length; i++) {
    pair += hexaValue[i];
    count++;
    if (count === 2) {
      pairs.push(pair);
      count = 0;
      pair = "";
    }
  }

  const rgb: RGB = pairs.map(
    (pair) => HEXAREF.indexOf(pair[0]) * 16 + HEXAREF.indexOf(pair[1]),
  ) as RGB;

  return rgb.length === 3 ? rgb : [0, 0, 0];
};

console.log(hexToRgb("#4b0082"));
console.log(hexToRgb("#FFFFFF"));
console.log(rgbToHex([75, 0, 130]));
console.log(rgbToHex([255, 255, 255]));
