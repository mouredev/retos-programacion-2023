const findPythaTriple = (max: number): Array<number[]> => {
  const results: Array<number[]> = [];

  for(let a = 1; a <= max; a++) {
    for(let b = a; b <= max; b++) {
      const c = Math.sqrt((a*a) + (b*b));
      if (c <= max && c === Math.floor(c)) {
        results.push([a, b, c]);
      }
    }
  }

  return results;
};

console.log(findPythaTriple(100))