const multiples = (i) => {
  return {
    multiple15: i % 15 === 0,
    multiple3: i % 3 === 0,
    multiple5: i % 5 === 0,
  };
};

for (let i = 1; i <= 100; i++) {
  const { multiple15, multiple3, multiple5 } = multiples(i);
  if (multiple15) {
    console.log("fizzbuzz");
  } else if (multiple3) {
    console.log("fizz");
  } else if (multiple5) {
    console.log("buzz");
  } else {
    console.log(i);
  }
}
