const listOfNumbers: Array<number> = Array.from({ length: 100 }, (_, i) => i + 1);

listOfNumbers.forEach((valueNumber) => {
  let valueString: string = '';

  if (valueNumber % 3 === 0)
    valueString += 'Fizz';

  if (valueNumber % 5 === 0)
    valueString += 'Buzz';

  console.log(valueString || valueNumber);
});

export { };

