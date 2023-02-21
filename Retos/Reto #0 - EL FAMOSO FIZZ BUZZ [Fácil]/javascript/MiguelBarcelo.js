const fizzBuzz = () => {
  const NEW_LINE = '\n';

  return Array.from({ length: 100 }, (_, i) => {
    const number = i + 1;
    if (number % 3 == 0) return 'fizz';
    if (number % 5 == 0) return 'buzz';
    if (number % 15 == 0) return 'fizzbuzz';
    return number;
  }).join(NEW_LINE)
}
console.log(fizzBuzz())