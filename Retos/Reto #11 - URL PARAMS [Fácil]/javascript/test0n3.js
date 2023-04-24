const urlParams = (url) => {
  if (countSpecialChar(url, "?") != 1) return [];

  let params = divideString(url, "?");
  let values = [];
  params.split("&").forEach((param) => {
    if (param.match(/\D+(={1})\w+/g)) {
      values.push(divideString(param, "="));
    }
  });
  return values;
};

const countSpecialChar = (string, char) => {
  const regex = new RegExp("\\" + char, "g");
  return (string.match(regex) || []).length;
};

const divideString = (string, char) => {
  let paramsIdx = string.lastIndexOf(char);
  return string.slice(paramsIdx + 1);
};

const tests = {
  input: [
    "https://retosdeprogramacion.com?year=2023&challenge=0",
    "https://retosdeprogramacion.com/search?year=2023",
    "https://retosdeprogramacion.com/params/name/lastname",
    "retosdeprogramacion.com/search?",
    "",
  ],
  output: [["2023", "0"], ["2023"], [], [], []],
};

errors = 0;
tests.input.forEach((test, index) => {
  let resp = urlParams(test);
  let expected = tests.output[index];
  if (JSON.stringify(resp) == JSON.stringify(expected)) return;

  errors += 1;
  console.log(`\n\noriginal: ${test}`);
  console.log(resp);
  console.log(`expected: ${expected}`);
});

console.log(`\nTests${errors != 0 ? " not " : " "}passed, ${errors} errors\n`);
