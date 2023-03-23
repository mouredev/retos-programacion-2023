// fizzbuzz de numeros del 1 al 100

const fizzbuzz = (num) => {
  let output = "";
  if (num % 3 === 0) output += "fizz";
  if (num % 5 === 0) output += "buzz";
  return output || num;
};

for (let i = 1; i <= 100; i++) {
  console.log(fizzbuzz(i));
}