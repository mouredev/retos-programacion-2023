'use strict';

function convertBase(number, base) {
  if (!Number.isInteger(number) || !Number.isInteger(base) || base < 2 || base > 16) {
    throw new Error('Número o base no válidos');
  }
  if (number === 0) return '0';
  const digits = '0123456789ABCDEF';
  const sign = number < 0 ? '-' : '';
  let value = Math.abs(number);
  let result = '';
  while (value > 0) {
    result = digits[value % base] + result;
    value = Math.floor(value / base);
  }
  return sign + result;
}

function toOctalAndHex(number) {
  return { octal: convertBase(number, 8), hexadecimal: convertBase(number, 16) };
}

module.exports = { convertBase, toOctalAndHex };

if (require.main === module) console.log(toOctalAndHex(Number(process.argv[2] ?? 100)));
