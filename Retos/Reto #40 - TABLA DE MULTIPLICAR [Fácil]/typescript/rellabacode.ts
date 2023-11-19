import {createInterface, Interface} from 'readline';
const util = require('util');

const rl: Interface = createInterface({
  input: process.stdin,
  output: process.stdout,
});

const questionAsync = util.promisify(rl.question).bind(rl);

async function readNumber(): Promise<number> {
  let number: number;
  do {
    const answer: string = await questionAsync('Insert an integer number: ');
    number = parseInt(answer, 10);
    if (isNaN(number)) {
      console.log('Error: This is not a valid integer. Try Again');
    }
  } while (isNaN(number));

  return number;
}

async function main() {
  const number: number = await readNumber();
  for (let i = 1; i <= 10; i++) {
    console.log(`${number} x ${i} = ${number * i}`);
  }

  process.exit(0);
}

main();
