// Run it yourself
// =========================================================
// https://replit.com/@luishendrix92/Reto44MoureDev#index.ts

import * as readline from "readline";
import { exit } from "process";

const STATISTICS_MSG = (correct: number, total: number) =>
  `You answered ${correct}/${total} questions correctly!`;
const WRONG_ANSWER_MSG = "❌ Your answer is wrong; better luck next time.";
const RIGHT_ANSWER_MSG = "✅ Congratulations! your answer was correct.";
const TIMEOUT_MSG = "⌛ Sorry, you took more than 3 seconds to answer.";
const TIME_BETWEEN_QUESTIONS = 1_500;
const MAX_TIME = 3_000;

type BinaryOp = (a: number, b: number) => number;
type Operator = "+" | "-" | "*" | "/";

interface Question {
  operator: Operator;
  argA: number;
  argB: number;
}

const operations: Record<Operator, BinaryOp> = {
  "+": (a, b) => a + b,
  "-": (a, b) => a - b,
  "/": (a, b) => a / b,
  "*": (a, b) => a * b,
};

const sleep = (time: number) =>
  new Promise((resolve) => setTimeout(resolve, time));

const choice = <T>(items: T[]): T => {
  const randomIndex = Math.floor(Math.random() * items.length);

  return items[randomIndex];
};

const randInt = (digits: number) =>
  Math.floor(Math.random() * Math.pow(10, digits));

const digitsPair = (rightAnswersCount: number) => {
  const digCount = Math.floor(rightAnswersCount / 5) + 1;
  const turn = digCount % 2 === 0;

  /**
   * Every 5 right answers, digCount will grow by 1, and whether digit A
   * or B grow by 1 depends on if digCount is odd or pair. And since
   * we're working with 2 values, we divide by 2. */
  return [
    (digCount + Number(turn) + 1) / 2,
    (digCount + Number(!turn)) / 2
  ];
};

function* questionGenerator(): Generator<Question, any, number> {
  let rightAnswerCount = 0;

  while (true) {
    const [argA, argB] = digitsPair(rightAnswerCount).map(randInt);
    const operator = choice(Object.keys(operations)) as Operator;

    rightAnswerCount = yield { argA, operator, argB };
  }
}

const formatQuestion = ({ argA, operator, argB }: Question) => {
  const prompt = `How much is ${argA} ${operator} ${argB}?`;

  return `
 .${"_".repeat(prompt.length)}.
{ ${prompt} }
 \\${"-".repeat(prompt.length)}/
  \\
   \\   \\_\\_    _/_/
    \\      \\__/
           (oo)\\_______
           (__)\\       )\\/\\
               ||----w |
               ||     ||

Your answer: `;
};

function askQuestion({ argA, operator, argB }: Question): Promise<boolean> {
  const rightAnswer = Math.floor(operations[operator](argA, argB));
  const promptMsg = formatQuestion({ operator, argA, argB });

  /**
   * NOTE: Readline and cancellation mechanism sources
   * =================================================
   * https://stackoverflow.com/questions/66318202/how-to-abort-a-readline-interface-question
   * https://nodejs.org/api/readline.html#rlquestionquery-options-callback
   */
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
  });

  return new Promise((resolve, reject) => {
    const ac = new AbortController();
    const signal = ac.signal;
    const timeout = setTimeout(() => ac.abort(), MAX_TIME);

    signal.addEventListener('abort', () => {
      rl.close();
      reject(new Error(TIMEOUT_MSG));
    });

    rl.question(promptMsg, { signal }, (answer: string) => {
      clearTimeout(timeout);
      rl.close();
      resolve(Number(answer) === rightAnswer);
    });
  });
}

// NOTE: Bear in mind emojis use variable charater spaces.
const fmtMsg = (msg: string) => `
┌─${"─".repeat(msg.length)}──┐
│ ${msg} │
└─${"─".repeat(msg.length)}──┘
`;

async function main() {
  let [questionCount, rightAnswerCount] = [0, 0];
  const questions = questionGenerator();

  while (true) {
    console.clear();

    try {
      const isRightAnswer = await askQuestion(
        questions.next(rightAnswerCount).value
      );

      questionCount++;
      console.log(fmtMsg(isRightAnswer ? RIGHT_ANSWER_MSG : WRONG_ANSWER_MSG));
      isRightAnswer && rightAnswerCount++;

      await sleep(TIME_BETWEEN_QUESTIONS);
    } catch (error) {
      // HACK: Typescript needs the IF in order to access .message
      if (error instanceof Error) console.log(fmtMsg(error.message));

      console.log(STATISTICS_MSG(rightAnswerCount, questionCount));
      exit(0);
    }
  }
}

main();
