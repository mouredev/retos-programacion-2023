function fizzbuzz(number) {
  if (!number || !Number(number) || (number < 0) || (number > 100)) {
    console.error('Invalid number');
  };

  for (let n = 1; n <= number; n++) {
    validateNumber(n);
  }
}

function validateNumber(number) {
  if (((number % 3) === 0) && ((number % 5) === 0)) {
    console.log('fizzbuzz');
  } else if ((number % 3) === 0) {
    console.log('fizz');
  } else if ((number % 5) === 0) {
    console.log('buzz');
  } else {
    console.log(number);
  }
}

fizzbuzz(100);
