for (let i = 1; i <= 100; i++) {

  if (i % 3 === 0 && i % 5 === 0) {
    console.log('fizzbuzz' + '\n')
  } else if (i % 3 === 0 && i % 5 != 0) {
    console.log('fizz' + '\n')
  } else if (i % 3 != 0 && i % 5 === 0) {
    console.log('buzz' + '\n')
  } else {
    console.log(i + '\n')
  }

}
