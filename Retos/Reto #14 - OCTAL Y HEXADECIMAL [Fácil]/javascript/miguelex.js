const DecimalToOctal = (number) => {
  let numberOctal = "";
  let numberDec = number;
  while (number > 0) {
    const rest = number % 8;
    numberOctal = rest + numberOctal;
    number = Math.floor(number / 8);
  }
  return (
    "El numero " +
    numberDec +
    " en base decimal corresponde al numero " +
    numberOctal +
    " en base octal"
  );
};

const DecimalToHex = (number) => {
  let numberHex = "";
  let numberDec = number;
  while (number > 0) {
    const rest = number % 16;
    if (rest < 10) {
      numberHex = rest + numberHex;
    } else {
      numberHex = String.fromCharCode(65 + (rest - 10)) + numberHex;
    }
    number = Math.floor(number / 16);
  }
  return (
    "El numero " +
    numberDec +
    " en base decimal corresponde al numero " +
    numberHex +
    " en base hexadecimal"
  );
};

console.log(DecimalToOctal(25));
console.log(DecimalToHex(255));
