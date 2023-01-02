const isMultiple = (number, multiple) => number % multiple === 0

for (let number = 1; number <= 100; number++) {
  if (isMultiple(number, 3) && isMultiple(number, 5)) {
    console.log('buzzfizz')
  } else if (isMultiple(number, 3)){
    console.log('buzz')
  } else if (isMultiple(number, 5)) {
    console.log('fizz')
  } else {
  	console.log(number)
  }
}