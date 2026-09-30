'use strict';

function letters(text) {
  return String(text).toLowerCase()
    .replace(/ñ/g, '\u0000')
    .normalize('NFD')
    .replace(/\p{Diacritic}/gu, '')
    .replace(/\u0000/g, 'ñ')
    .match(/[a-zñ]/g) ?? [];
}

function frequencies(text) {
  return letters(text).reduce((result, letter) => {
    result.set(letter, (result.get(letter) ?? 0) + 1);
    return result;
  }, new Map());
}

function isHeterogram(text) {
  const chars = letters(text);
  return chars.length > 0 && new Set(chars).size === chars.length;
}

function isIsogram(text) {
  const counts = [...frequencies(text).values()];
  return counts.length > 0 && counts.every(count => count === counts[0]);
}

function isPangram(text) {
  return 'abcdefghijklmnñopqrstuvwxyz'.split('').every(letter => frequencies(text).has(letter));
}

module.exports = { isHeterogram, isIsogram, isPangram };
