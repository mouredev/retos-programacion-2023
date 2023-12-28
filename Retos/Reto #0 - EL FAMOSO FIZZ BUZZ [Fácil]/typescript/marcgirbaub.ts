const fizzBuzzFunction = (number: number): string => {
  if (number % 3 === 0 && number % 5 === 0) {
    return `fizzbuzz`;
  } else if (number % 3 === 0) {
    return `fizz`;
  } else if (number % 5 === 0) {
    return `buzz`;
  } else {
    return `${number}`;
  }
};

for (let i = 1; i <= 100; i++) {
  console.log(`${fizzBuzzFunction(i)}`);
}
