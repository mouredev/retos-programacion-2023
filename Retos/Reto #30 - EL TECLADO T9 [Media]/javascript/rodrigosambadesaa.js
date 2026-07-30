'use strict';

const T9 = {
  0: ' ', 1: '.,?!', 2: 'ABC', 3: 'DEF', 4: 'GHI',
  5: 'JKL', 6: 'MNO', 7: 'PQRS', 8: 'TUV', 9: 'WXYZ'
};

function fromT9(presses) {
  if (presses === '') return '';
  return String(presses).split('-').map(block => {
    if (!block || !/^\d+$/.test(block) || ![...block].every(digit => digit === block[0])) {
      throw new Error(`Bloque no válido: ${block}`);
    }
    const letters = T9[block[0]];
    if (!letters || block.length > letters.length) throw new Error(`Pulsación no válida: ${block}`);
    return letters[block.length - 1];
  }).join('');
}

module.exports = { fromT9 };

if (require.main === module) console.log(fromT9(process.argv[2] ?? '6-666-88-777-33-3-33-888'));
