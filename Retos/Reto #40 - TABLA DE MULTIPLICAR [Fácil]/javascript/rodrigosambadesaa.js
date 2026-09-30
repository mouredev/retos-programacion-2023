'use strict';

function multiplicationTable(number) {
  if (!Number.isFinite(number)) throw new Error('Se esperaba un número');
  return Array.from({ length: 10 }, (_, index) => {
    const factor = index + 1;
    return `${number} x ${factor} = ${number * factor}`;
  });
}

module.exports = { multiplicationTable };

if (require.main === module) multiplicationTable(Number(process.argv[2] ?? 1)).forEach(console.log);
