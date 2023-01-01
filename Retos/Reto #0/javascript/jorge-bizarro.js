const listOfNumbers = Array.from({ length: 100 }, (_, i) => i + 1);

listOfNumbers.forEach(valueNumber => {
  let valueToPrint = '';

  if (valueNumber % 3 === 0)
    valueToPrint += 'Fizz';

  if (valueNumber % 5 === 0)
    valueToPrint += 'Buzz';

  valueToPrint ||= valueNumber;

  console.log(valueToPrint);
});
