function fizzBuzz(number) {
    const isFizz = number % 3 === 0;
    const isBuzz = number % 5 === 0;
    const isFizzBuzz = isFizz && isBuzz;
    if (isFizzBuzz) {
        return 'FizzBuzz';
    }
    if (isFizz) {
        return 'Fizz';
    }
    if (isBuzz) {
        return 'Buzz';
    }
    return number.toString();
}
// Create range from 1 to 100
const numbers = Array.from(Array(100).keys()).map(n => n + 1);
// Iterate over list
const fizzBuzzList = numbers.map(number => fizzBuzz(number));
console.log(fizzBuzzList.join('\n'));
