const fizzbuzz = () => {
  const initialNumber = 1;
  const finalNumber = 100;

  for (let index = initialNumber; index < finalNumber; index++) {
    if (index % 3 === 0 && index % 5 === 0) console.log("fizzbuzz");
    else if (index % 3 === 0) console.log("fizz");
    else if (index % 5 === 0) console.log("buzz");
    else console.log(index);
  }
};

fizzbuzz();
