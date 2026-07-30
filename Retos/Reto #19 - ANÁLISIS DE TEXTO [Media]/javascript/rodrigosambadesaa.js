'use strict';

function analyzeText(text) {
  const value = String(text);
  let current = '';
  let totalLength = 0;
  let sentences = 0;
  const words = [];
  for (let index = 0; index <= value.length; index++) {
    const character = value[index] ?? ' ';
    if (/[\p{L}\p{N}]/u.test(character)) {
      current += character;
    } else {
      if (current) {
        words.push(current);
        totalLength += current.length;
        current = '';
      }
      if (character === '.') sentences++;
    }
  }
  return {
    words: words.length,
    averageLength: words.length ? totalLength / words.length : 0,
    sentences,
    longestWord: words.reduce((longest, word) => word.length > longest.length ? word : longest, '')
  };
}

module.exports = { analyzeText };

if (require.main === module) console.log(analyzeText(process.argv.slice(2).join(' ')));
