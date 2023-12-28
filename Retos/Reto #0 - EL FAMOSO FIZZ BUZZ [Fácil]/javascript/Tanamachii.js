const fizzBuzz = () => {
  for (let i = 1; i <= 100; i++) {
    let varPrint = i;
    if (i % 3 == 0 && i % 5 == 0) {
      varPrint = "fizzbuzz";
    } else if (i % 3 == 0) {
      varPrint = "fizz";
    } else if (i % 5 == 0) {
      varPrint = "buzz";
    }
    console.log(varPrint);
  }
};

fizzBuzz();
