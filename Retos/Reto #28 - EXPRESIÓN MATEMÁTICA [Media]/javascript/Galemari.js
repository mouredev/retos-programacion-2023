const readline = require("readline");

function checkExpression(expression) {
  const validOperators = ["+", "-", "*", "/", "%"];
  const expressionArray = expression.split(" ");

  if (expressionArray.length < 3) return false;

  for (const char of expressionArray) {
    if (!validOperators.includes(char) && !/^([0-9])*$/.test(char)) {
      return false;
    }
  }

  return true;
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.question("Ingrese una expresión matemática: ", (expression) => {
  rl.close();
  const isCorrect = checkExpression(expression);
  console.log(`La expresión es ${isCorrect ? "correcta" : "incorrecta"}`);
});
