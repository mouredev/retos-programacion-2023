const isMultiple = (number: number, multiple: number): boolean =>
  number % multiple === 0;

const fizzBuzz = (number: number): string | number => {
  const dict = {
    "3": "fizz",
    "5": "buzz",
  };
  const word = Object.keys(dict)
    .filter((multiple) => isMultiple(number, Number(multiple)))
    .map((multiple) => dict[multiple as keyof typeof dict])
    .join("");

  return word || number;
};

const runTests = () => {
  const numbers = Array.from({ length: 100 }, (_, idx) => idx + 1);

  numbers.forEach((number) => {
    console.log(fizzBuzz(number));
  });
};

runTests();
