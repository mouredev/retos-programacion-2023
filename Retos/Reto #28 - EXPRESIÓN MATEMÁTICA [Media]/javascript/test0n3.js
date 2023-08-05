//
// Crea una función que reciba una expresión matemática (String)
// y compruebe si es correcta. Retornará true o false.
// - Para que una expresión matemática sea correcta debe poseer
//   un número, una operación y otro número separados por espacios.
//   Tantos números y operaciones como queramos.
// - Números positivos, negativos, enteros o decimales.
// - Operaciones soportadas: + - * / %
//
// Ejemplos:
// "5 + 6 / 7 - 4" -> true
// "5 a 6" -> false
//

const validOperation = (operation) => {
  let operationArray = operation.split(" ");
  if (invalid(operationArray)) {
    return false;
  }

  for (let i = 0; i < operationArray.length; i++) {
    if (!isNumber(operationArray[i]) && !isOperator(operationArray[i])) {
      console.log("inside conditional");
      return false;
    }
  }
  return true;
};

const invalid = (operationArray) => {
  const operationLength = operationArray.length;
  return operationLength < 3 || operationLength % 2 === 0;
};

const isNumber = (value) => {
  return !isNaN(value);
};

const isOperator = (value) => {
  return value.match(/[+\-*\/%]/) && value.length == 1;
};

const tests = {
  input: ["-5 + 12%3", "-5", "5 / 3", "5 / -3 * 2"],
  expecteds: [false, false, true, true],
};

let errors = 0;
tests.input.forEach((test, index) => {
  const result = validOperation(test);
  if (result == tests.expecteds[index]) {
    console.log(
      `Success - input: ${test}, expected: ${tests.expecteds[index]}`
    );
  }
  if (result != tests.expecteds[index]) {
    errors += 1;
    console.log(
      `Error - input: ${test}, expected: ${tests.expecteds[index]}, result: ${result}`
    );
  }
});

console.log(`Errors: ${errors}`);
