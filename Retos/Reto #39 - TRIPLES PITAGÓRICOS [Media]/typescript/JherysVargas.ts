const generateNumbers = (limit: number): number[] => {
  return Array.from({ length: limit }, (_, index) => index + 1);
};

const searchForPythagoreanTriples = (limit: number): number[][] => {
  const pythagoreanTriples: number[][] = [];

  if (limit <= 0) return pythagoreanTriples;

  const numbers: number[] = generateNumbers(limit);

  for (let i = 0; i < numbers.length; i++) {
    for (let j = i + 1; j < numbers.length; j++) {
      const a: number = numbers[i];
      const b: number = numbers[j];
      const cSquared: number = Math.pow(a, 2) + Math.pow(b, 2);
      const c: number = Math.sqrt(cSquared);

      if (Number.isInteger(c)) {
        pythagoreanTriples.push([a, b, c]);
      }
    }
  }

  return pythagoreanTriples;
};

const triplesFound: number[][] = searchForPythagoreanTriples(17);
console.log(triplesFound);
