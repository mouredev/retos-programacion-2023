import { stdin as input, stdout as output } from "node:process";
import { createInterface } from "node:readline/promises";
const rl = createInterface({ input, output });

const printMultiplicationTable = async (): Promise<void> => {
  const num = Number(await rl.question("Ingresa un número: "));
  for (let i = 1; i <= 10; i++) {
    console.log(`${num} x ${i} = ${num * i}`);
  }
};

printMultiplicationTable();
