'use strict';

const ALPHABET = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ';

function caesar(text, shift, decrypt = false) {
  if (!Number.isInteger(shift)) throw new Error('El desplazamiento debe ser entero');
  const movement = ((decrypt ? -shift : shift) % ALPHABET.length + ALPHABET.length) % ALPHABET.length;
  return [...String(text)].map(character => {
    const upper = character.toLocaleUpperCase('es');
    const index = ALPHABET.indexOf(upper);
    if (index === -1) return character;
    const result = ALPHABET[(index + movement) % ALPHABET.length];
    return character === upper ? result : result.toLocaleLowerCase('es');
  }).join('');
}

module.exports = { caesar };

if (require.main === module) {
  const encrypted = caesar(process.argv.slice(2).join(' ') || 'Hola Mundo', 3);
  console.log(encrypted);
  console.log(caesar(encrypted, 3, true));
}
