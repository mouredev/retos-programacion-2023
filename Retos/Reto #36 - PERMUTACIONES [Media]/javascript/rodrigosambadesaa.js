'use strict';

function permutations(word) {
  const characters = [...String(word)];
  if (characters.length === 0) return [''];
  const result = [];
  const build = (prefix, remaining) => {
    if (remaining.length === 0) {
      result.push(prefix);
      return;
    }
    const used = new Set();
    for (let index = 0; index < remaining.length; index++) {
      if (used.has(remaining[index])) continue;
      used.add(remaining[index]);
      build(prefix + remaining[index], remaining.slice(0, index).concat(remaining.slice(index + 1)));
    }
  };
  build('', characters);
  return result;
}

module.exports = { permutations };

if (require.main === module) console.log(permutations(process.argv[2] ?? 'sol').join(', '));
