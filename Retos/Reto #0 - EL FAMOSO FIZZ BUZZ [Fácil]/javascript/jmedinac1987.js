function fizzbuzz() {
  let serie = [];

  for (let i = 1; i <= 100; i++) {
    serie.push(isMultiple(i));
  }

  return serie;
}

function isMultiple(number) {
  if (typeof number != "number") return "";

  if (number === 0) return number;

  if (number % 3 == 0 && number % 5 == 0) return "fizzbuzz";

  if (number % 3 == 0) return "fizz";

  if (number % 5 == 0) return "buzz";

  return number;
}

console.table(fizzbuzz());