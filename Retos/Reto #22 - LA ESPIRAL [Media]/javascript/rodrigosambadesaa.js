'use strict';

function spiral(size) {
  if (!Number.isInteger(size) || size < 1) throw new Error('El lado debe ser un entero positivo');
  if (size === 1) return '═';
  const path = [{ row: 0, column: 0 }];
  let top = 0;
  let left = 0;
  let right = size - 1;
  let bottom = size - 1;
  let current = path[0];
  const add = (row, column) => {
    current = { row, column };
    path.push(current);
  };

  while (top <= bottom && left <= right) {
    for (let column = current.column + 1; column <= right; column++) add(current.row, column);
    for (let row = current.row + 1; row <= bottom; row++) add(row, current.column);
    for (let column = current.column - 1; column >= left; column--) add(current.row, column);
    for (let row = current.row - 1; row >= top + 1; row--) add(row, current.column);
    top++;
    left++;
    right--;
    bottom--;
    if (top > bottom || left > right) break;
  }

  const grid = Array.from({ length: size }, () => Array(size).fill(' '));
  const connection = (cell, neighbor) => {
    if (neighbor.row < cell.row) return 'U';
    if (neighbor.row > cell.row) return 'D';
    if (neighbor.column < cell.column) return 'L';
    return 'R';
  };
  const glyphs = {
    LR: '═', DU: '║', DR: '╔', DL: '╗', RU: '╚', LU: '╝'
  };

  path.forEach((cell, index) => {
    const directions = new Set();
    if (path[index - 1]) directions.add(connection(cell, path[index - 1]));
    if (path[index + 1]) directions.add(connection(cell, path[index + 1]));
    if (index === 0) directions.add('L');
    if (index === path.length - 1) {
      const previous = path[index - 1];
      if (previous.row === cell.row) directions.add(previous.column < cell.column ? 'D' : 'U');
      else directions.add(previous.row < cell.row ? 'L' : 'R');
    }
    const key = [...directions].sort().join('');
    grid[cell.row][cell.column] = glyphs[key] ?? (directions.has('L') || directions.has('R') ? '═' : '║');
  });
  return grid.map(row => row.join('')).join('\n');
}

module.exports = { spiral };

if (require.main === module) console.log(spiral(Number(process.argv[2] ?? 5)));
