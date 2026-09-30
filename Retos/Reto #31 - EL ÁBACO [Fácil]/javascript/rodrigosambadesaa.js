'use strict';

function readAbacus(rows) {
  if (!Array.isArray(rows) || rows.length !== 7) throw new Error('El ábaco debe tener siete filas');
  const digits = rows.map(row => {
    if (!/^O{0,9}---O{0,9}$/.test(row) || row.replace('---', '').length !== 9) {
      throw new Error(`Fila no válida: ${row}`);
    }
    return row.indexOf('---');
  });
  return Number(digits.join(''));
}

module.exports = { readAbacus };

if (require.main === module) {
  console.log(readAbacus([
    'O---OOOOOOOO', 'OOO---OOOOOO', '---OOOOOOOOO', 'OO---OOOOOOO',
    'OOOOOOO---OO', 'OOOOOOOOO---', '---OOOOOOOOO'
  ]).toLocaleString('es-ES'));
}
