'use strict';

function staircase(steps) {
  if (!Number.isInteger(steps)) throw new Error('El número de escalones debe ser entero');
  if (steps === 0) return '__';
  const size = Math.abs(steps);
  const lines = [];
  if (steps > 0) {
    lines.push(`${' '.repeat(size * 2)}_`);
    for (let row = 0; row < size; row++) lines.push(`${' '.repeat((size - row - 1) * 2)}_|`);
  } else {
    lines.push('_');
    for (let row = 0; row < size; row++) lines.push(`${' '.repeat((row + 1) * 2)}|_`);
  }
  return lines.join('\n');
}

module.exports = { staircase };

if (require.main === module) console.log(staircase(Number(process.argv[2] ?? 4)));
