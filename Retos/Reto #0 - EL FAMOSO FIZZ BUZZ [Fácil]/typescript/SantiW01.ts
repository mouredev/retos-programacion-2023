function FizzBuzz(): void {
  for (let i: number = 0; i <= 100; i++) {
    let fizzOrBuzz: string = "";
    if (i % 3 == 0 && i % 5 == 0) {
      fizzOrBuzz = "fizzbuzz";
    } else if (i % 5 == 0) {
      fizzOrBuzz = "buzz";
    } else if (i % 3 == 0) {
      fizzOrBuzz = "fizz";
    } else {
      continue;
    }
    console.log(fizzOrBuzz);
  }
}

console.log(FizzBuzz());
