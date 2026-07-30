'use strict';

function pythagoreanTriples(limit) {
  if (!Number.isInteger(limit) || limit < 1) throw new Error('El límite debe ser un entero positivo');
  const triples = [];
  for (let first = 1; first <= limit; first++) {
    for (let second = first + 1; second <= limit; second++) {
      const third = Math.sqrt(first * first + second * second);
      if (Number.isInteger(third) && third <= limit) triples.push([first, second, third]);
    }
  }
  return triples;
}

module.exports = { pythagoreanTriples };

if (require.main === module) console.log(pythagoreanTriples(Number(process.argv[2] ?? 10)));
