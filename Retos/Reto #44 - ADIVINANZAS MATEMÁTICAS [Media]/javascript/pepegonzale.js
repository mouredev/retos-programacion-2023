/*
 * Crea un juego interactivo por terminal en el que tendrás que adivinar
 * el resultado de diferentes
 * operaciones matemáticas aleatorias (suma, resta, multiplicación
 * o división de dos números enteros).
 * - Tendrás 3 segundos para responder correctamente.
 * - El juego finaliza si no se logra responder en ese tiempo.
 * - Al finalizar el juego debes mostrar cuántos cálculos has acertado.
 * - Cada 5 aciertos debes aumentar en uno el posible número de cifras
 *   de la operación (cada vez en un operando):
 *   - Preguntas 1 a 5: X (entre 0 y 9) operación Y (entre 0 y 9)
 *   - Preguntas 6 a 10: XX (entre 0 y 99) operación Y (entre 0 y 9)
 *   - Preguntas 11 a 15: XX operación YY
 *   - Preguntas 16 a 20: XXX (entre 0 y 999) operación YY
 *   ...
 */
let correct = 0;
let questions = 0;
let digits_number = 0;
let x = 9;
let y = 9;
let myTimeout;
const rl = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});
const generateOperator = () => {
  let operators = ["+", "-", "/", "*"];
  let operator = Math.floor(operators.length * Math.random());
  return operators[operator];
};
generateOperator();
const generateRandomNumbers = () => {
  if (correct % 5 === 0 && correct != 0) {
    digits_number++;
    if (!(digits_number % 2 === 0)) {
      x = parseInt(x + "9");
    } else {
      y = parseInt(y + "9");
    }
  }

  let first = Math.floor(Math.random() * x);
  let second = Math.floor(Math.random() * y);
  return {
    first,
    second,
  };
};
const adivinanzas_matematicas = () => {
  let { first, second } = generateRandomNumbers(correct);
  let operator = generateOperator();
  myTimeout = timeout();
  rl.question(
    `What is the result of this ${first} ${operator} ${second} => `,
    (user_result) => {
      questions++;
      console.log(`Question number ${questions}`);
      let result = eval(`${first} ${operator} ${second}`);
      console.log(
        `The correct result is: ${result}, and your result is ${user_result}`
      );
      if (
        result === parseInt(user_result) ||
        result === parseFloat(user_result)
      ) {
        correct++;
        console.log(`Correct answer!`);
        clearTimeout(myTimeout);
        adivinanzas_matematicas();
      } else {
        console.log(
          `You solved ${correct} questions, try again to beat your record!`
        );
        rl.close();
      }
    }
  );
};
const timeout = () => {
  return setTimeout(() => {
    console.log(
      `You solved ${correct} questions, try again to beat your record!`
    );
    rl.close();
  }, 3000);
};

adivinanzas_matematicas();
