const friday13 = (date) => {
  const [year, month] = date;
  return new Date(year, month - 1, 13).getDay() == 5;
};

const tests = {
  input: [
    [2023, 3],
    [2023, 10],
    [2024, 9],
    [2023, 2],
  ],
  output: [false, true, true, false],
};

let errors = 0;

tests["input"].forEach((test, index) => {
  const resp = friday13(test);
  const expected = tests["output"][index];
  if (resp == expected) return;

  errors += 1;
  console.log(`\n\noriginal: ${test}`);
  console.log(resp);
  console.log(`expected: ${expected}`);
});

console.log(`\nTests${errors != 0 ? " not " : " "}passed, ${errors} errors\n`);
