'use strict';

class TetrisPiece {
  constructor(size = 10) {
    if (!Number.isInteger(size) || size < 4) throw new Error('Tablero demasiado pequeño');
    this.size = size;
    this.row = 0;
    this.column = 0;
    this.shape = [[0, 0], [1, 0], [1, 1], [1, 2]];
  }

  cells(shape = this.shape, row = this.row, column = this.column) {
    return shape.map(([r, c]) => [r + row, c + column]);
  }

  fits(shape, row, column) {
    return this.cells(shape, row, column).every(([r, c]) => r >= 0 && c >= 0 && r < this.size && c < this.size);
  }

  move(action) {
    const movement = {
      derecha: [0, 1], right: [0, 1], izquierda: [0, -1], left: [0, -1],
      abajo: [1, 0], down: [1, 0]
    }[String(action).toLowerCase()];
    if (movement) {
      const nextRow = this.row + movement[0];
      const nextColumn = this.column + movement[1];
      if (this.fits(this.shape, nextRow, nextColumn)) {
        this.row = nextRow;
        this.column = nextColumn;
        return true;
      }
      return false;
    }
    if (['rotar', 'rotate'].includes(String(action).toLowerCase())) {
      const rotated = this.shape.map(([row, column]) => [column, -row]);
      const minRow = Math.min(...rotated.map(cell => cell[0]));
      const minColumn = Math.min(...rotated.map(cell => cell[1]));
      const normalized = rotated.map(([row, column]) => [row - minRow, column - minColumn]);
      if (this.fits(normalized, this.row, this.column)) {
        this.shape = normalized;
        return true;
      }
      return false;
    }
    throw new Error(`Acción no válida: ${action}`);
  }

  render() {
    const occupied = new Set(this.cells().map(([row, column]) => `${row},${column}`));
    return Array.from({ length: this.size }, (_, row) =>
      Array.from({ length: this.size }, (_, column) => occupied.has(`${row},${column}`) ? '🔳' : '🔲').join('')
    ).join('\n');
  }
}

module.exports = { TetrisPiece };

if (require.main === module) {
  const piece = new TetrisPiece();
  for (const action of process.argv.slice(2)) piece.move(action);
  console.log(piece.render());
}
