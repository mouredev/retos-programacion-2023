'use strict';

function combinationsThatSum(numbers, target) {
  if (!Array.isArray(numbers) || !numbers.every(number => Number.isInteger(number) && number > 0)) {
    throw new Error('La lista debe contener enteros positivos');
  }
  const values = [...numbers].sort((a, b) => a - b);
  const result = [];
  const search = (start, sum, combination) => {
    if (sum === target) {
      result.push([...combination]);
      return;
    }
    for (let index = start; index < values.length; index++) {
      if (index > start && values[index] === values[index - 1]) continue;
      const next = sum + values[index];
      if (next > target) break;
      combination.push(values[index]);
      search(index + 1, next, combination);
      combination.pop();
    }
  };
  search(0, 0, []);
  return result;
}

module.exports = { combinationsThatSum };

if (require.main === module) console.log(combinationsThatSum([1, 5, 3, 2], 6));
