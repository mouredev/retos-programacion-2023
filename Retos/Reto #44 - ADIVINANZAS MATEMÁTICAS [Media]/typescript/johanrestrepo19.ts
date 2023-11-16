//@ts-ignore
import { stdin as input, stdout as output } from "node:process";
//@ts-ignore
import { createInterface } from "node:readline/promises";

const readLine = createInterface({ input, output });

enum Operations {
  ADD = "add",
  SUBTRAC = "subtrac",
  MULTIPLY = "multiply",
  DIVIDE = "divide",
}

type Question = {
  x: number;
  y: number;
  operation: Operations;
  operationSign?: string;
  result: number;
};

const getRandomEnumKey = <T extends object>(someEnum: T): T[keyof T] => {
  const enumKeys = Object.values(someEnum);
  const randomIndex = Math.floor(Math.random() * enumKeys.length);
  return enumKeys[randomIndex];
};

class Game {
  private _answeredQuestionAmm: number;
  private _currentQuestion?: Question;

  constructor() {
    this._answeredQuestionAmm = 0;
  }

  get currentQuestion() {
    return this._currentQuestion;
  }

  get answeredQuestionAmm () {
    return this._answeredQuestionAmm
  }

  generateQuestion(): void {
    //TODO: Incrementar el número de digitos segun las respuestas acertadas

    const x = Math.floor(Math.random() * 10);
    const y = Math.floor(Math.random() * 10);
    const operation = getRandomEnumKey(Operations);
    let operationSign = "";
    let result = 0;

    switch (operation) {
      case Operations["ADD"]:
        result = x + y;
        operationSign = "+";
        break;
      case Operations["SUBTRAC"]:
        result = x - y;
        operationSign = "-";
        break;
      case Operations["MULTIPLY"]:
        result = x * y;
        operationSign = "*";
        break;
      case Operations["DIVIDE"]:
        result = x / y;
        operationSign = "/";
        break;
    }

    this._currentQuestion = { x, y, operation, result, operationSign };
  }

  validateAnswer(answer: number): boolean {
    if (this.currentQuestion?.result === answer) {
      this._answeredQuestionAmm++;
      return true;
    }
    return false;
  }
}

//-------------------------------
// Metodos de vista
//-------------------------------
const showQuestion = (question: Question): void => {
  console.log(
    `Resultado de la siguiente operación: ${question.x} ${question.operationSign} ${question.y}?`,
  );
};

const waitAnswerForAmmTime = (
  timeToWait = 3000,
): Promise<{ value: number; hasAnswered: boolean }> => {
  const ac = new AbortController();

  return new Promise(async (resolve) => {
    const timeOutId = setTimeout(() => ac.abort(), timeToWait);

    try {
      const userAnswer = Number(
        await readLine.question("Ingrese su respuesta: ", {
          signal: ac.signal,
        }),
      );
      clearTimeout(timeOutId);
      if (isNaN(userAnswer)) throw Error;
      resolve({ value: userAnswer, hasAnswered: true });
    } catch {
      resolve({ value: NaN, hasAnswered: false });
    }
  });
};

const main = async () => {
  console.clear();
  const game = new Game();

  while (true) {
    game.generateQuestion();
    if (game.currentQuestion) showQuestion(game.currentQuestion);

    try {
      const userAnswer = await waitAnswerForAmmTime();
      if (!userAnswer.hasAnswered) break;
      const isValidAnswer = game.validateAnswer(userAnswer.value);
      if (!isValidAnswer) break;
    } catch (error) {
      console.error(error);
    }
  }

  //Mostrar resultados

  console.clear();
  console.log("No has respondido correctamente ");
  console.log(`Lograste responder correctamente ${game.answeredQuestionAmm} preguntas`);
};

main();
