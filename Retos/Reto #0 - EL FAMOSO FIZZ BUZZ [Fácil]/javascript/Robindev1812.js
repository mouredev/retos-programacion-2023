for (let i = 1; i <= 100; i++) {
  let output;

  if (i % 3 == 0 && i % 5 == 0) {
    output = "fizzbuzz";
    console.log(output);
  } else if (i % 3 == 0) {
    output = "fizz";
    console.log(output);
  } else if (i % 5 == 0) {
    output = "buzz";
    console.log(output);
  } else {
    console.log(i);
  }
}
