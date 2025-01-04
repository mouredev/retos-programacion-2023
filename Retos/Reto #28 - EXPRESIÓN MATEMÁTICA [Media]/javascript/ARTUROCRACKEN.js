function isMathematicalExpression(expression) {
  const regex = /^(\-?\d+(\.\d+)?(\s?[\+\-\*\/\%]\s?\-?\d+(\.\d+)?)+)*$/;
  return regex.test(expression);
}

let e1 = isMathematicalExpression("5 - e");
let e2 = isMathematicalExpression("5 - 5");
let e3 = isMathematicalExpression("5 * 8 / 2");
let e4 = isMathematicalExpression("5 + 2x");
let e5 = isMathematicalExpression("5 % 2");
let e6 = isMathematicalExpression("5 + 6 / 7 - 4");
let e7 = isMathematicalExpression("5 a 6");

console.log("Aqui inicia.\n");

console.log(
  `1: ${e1}\n2: ${e2}\n3: ${e3}\n4: ${e4}\n5: ${e5}\n6: ${e6}\n7: ${e7}\n`
);

console.log("Aqui termina.");
