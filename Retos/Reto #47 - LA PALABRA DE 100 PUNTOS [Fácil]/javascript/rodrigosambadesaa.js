'use strict';

const SPANISH_ALPHABET = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ';

function wordScore(word) {
  return [...String(word).toLocaleUpperCase('es')]
    .reduce((score, character) => {
      const normalized = character === 'Ñ'
        ? character
        : character.normalize('NFD').replace(/\p{Diacritic}/gu, '');
      const value = SPANISH_ALPHABET.indexOf(normalized);
      return score + (value === -1 ? 0 : value + 1);
    }, 0);
}

module.exports = { wordScore };

if (require.main === module) {
  const word = process.argv.slice(2).join(' ') || 'programacion';
  console.log(`${word}: ${wordScore(word)} puntos`);
}
