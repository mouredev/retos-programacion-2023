'use strict';

function infiltratedCharacters(first, second) {
  const left = [...String(first)];
  const right = [...String(second)];
  if (left.length !== right.length) throw new Error('Las cadenas deben tener la misma longitud');
  const differences = [];
  for (let index = 0; index < left.length; index++) {
    if (left[index] !== right[index]) differences.push(right[index]);
  }
  return differences;
}

module.exports = { infiltratedCharacters };

if (require.main === module) console.log(infiltratedCharacters('Me llamo mouredev', 'Me llemo mouredov'));
