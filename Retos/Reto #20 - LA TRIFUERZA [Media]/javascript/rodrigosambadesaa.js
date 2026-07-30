'use strict';

function triforce(rows) {
  if (!Number.isInteger(rows) || rows < 1) throw new Error('El número de filas debe ser positivo');
  const lines = [];
  for (let row = 0; row < rows; row++) {
    lines.push(' '.repeat(rows * 2 - row - 1) + '*'.repeat(row * 2 + 1));
  }
  for (let row = 0; row < rows; row++) {
    const triangle = '*'.repeat(row * 2 + 1);
    lines.push(' '.repeat(rows - row - 1) + triangle + ' '.repeat((rows - row) * 2 - 1) + triangle);
  }
  return lines.join('\n');
}

module.exports = { triforce };

if (require.main === module) console.log(triforce(Number(process.argv[2] ?? 2)));
