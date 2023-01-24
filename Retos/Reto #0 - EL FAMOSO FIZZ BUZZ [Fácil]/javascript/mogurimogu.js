for (let i = 0; i < 100; i++) {
  const v = i + 1;
  let fizzbuzz = "";

  if (v % 3 === 0) {
    fizzbuzz = fizzbuzz + "fizz";
  }
  if (v % 5 === 0) {
    fizzbuzz = fizzbuzz + "buzz";
  }

  if (fizzbuzz) {
    console.log(fizzbuzz);
  } else {
    console.log(v);
  }
}
