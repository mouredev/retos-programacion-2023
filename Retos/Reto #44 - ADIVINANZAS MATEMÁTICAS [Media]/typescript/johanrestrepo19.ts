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
  private _nextIncrement: "x" | "y";
  private _digitsX: number;
  private _digitsY: number;

  constructor() {
    this._answeredQuestionAmm = 0;
    this._digitsX = this._digitsY = 10;
    this._nextIncrement = "x";
  }

  get currentQuestion() {
    return this._currentQuestion;
  }

  get answeredQuestionAmm() {
    return this._answeredQuestionAmm;
  }

  private calculateDigists() {
    if (this._answeredQuestionAmm > 0 && this._answeredQuestionAmm % 5 === 0) {
      if (this._nextIncrement === "x") {
        this._digitsX = this._digitsX * 10;
        this._nextIncrement = "y";
      } else if (this._nextIncrement === "y") {
        this._digitsY = this._digitsY * 10;
        this._nextIncrement = "x";
      }
    }
  }

  generateQuestion(): void {
    this.calculateDigists();

    const x = Math.floor(Math.random() * this._digitsX);
    const y = Math.floor(Math.random() * this._digitsY);
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
        result = Number(result.toFixed(2));
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

const showGameOver = (answeredQuestions: number) => {
  console.log();
  console.log("No has respondido correctamente ");
  console.log(
    `Lograste responder correctamente ${answeredQuestions} preguntas`,
  );
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
    console.log();
  }

  showGameOver(game.answeredQuestionAmm);
};

main();
