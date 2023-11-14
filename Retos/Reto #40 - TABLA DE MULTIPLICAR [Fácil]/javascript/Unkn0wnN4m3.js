import * as readline from "node:readline/promises";
import { stdin as input, stdout as output } from "node:process";

/**
  * @param {number} number number to get the table
  * @returns {void} returns nothing, just prints to console
  */
function m_table(number) {
  if ((typeof number) !== "number")
    throw new Error(`${number} is not number`);

  if (number % 1 !== 0)
    throw new Error(`${number} is not integer`);

  let i, result;

  for (i = 1; i <= 10; i++) {
    result = number * i;
    console.log(`${number} x ${i} = ${result}`);
  }
}

async function main() {
  const rl = readline.createInterface({ input, output });

  try {
    const n = await rl.question("Give me a number: ");
    m_table(parseInt(n));
  } catch (e) {
    console.error(e.message);
  }
  finally {
    rl.close();
  }
}

main();
