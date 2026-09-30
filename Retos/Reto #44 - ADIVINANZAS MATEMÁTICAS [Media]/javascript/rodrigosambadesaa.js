'use strict';

const OPERATIONS = ['+', '-', '*', '/'];

function digitsForScore(score) {
  const level = Math.floor(score / 5);
  return { left: 1 + Math.ceil(level / 2), right: 1 + Math.floor(level / 2) };
}

function generateProblem(score, random = Math.random) {
  const digits = digitsForScore(score);
  const maximum = count => 10 ** count - 1;
  const operation = OPERATIONS[Math.floor(random() * OPERATIONS.length)];
  let left = Math.floor(random() * (maximum(digits.left) + 1));
  let right = Math.floor(random() * (maximum(digits.right) + 1));
  let answer;
  if (operation === '/') {
    right = Math.max(1, right);
    const quotient = Math.floor(left / right);
    left = quotient * right;
    answer = quotient;
  } else if (operation === '+') answer = left + right;
  else if (operation === '-') answer = left - right;
  else answer = left * right;
  return { expression: `${left} ${operation} ${right}`, answer };
}

async function play(input = process.stdin, output = process.stdout) {
  const readline = require('node:readline/promises');
  const terminal = readline.createInterface({ input, output });
  let score = 0;
  while (true) {
    const problem = generateProblem(score);
    let response;
    try {
      response = await terminal.question(`${problem.expression} = `, { signal: AbortSignal.timeout(3000) });
    } catch (error) {
      if (error.name !== 'AbortError') throw error;
      response = null;
    }
    if (response === null || Number(response) !== problem.answer) break;
    score++;
  }
  terminal.close();
  console.log(`Aciertos: ${score}`);
  return score;
}

module.exports = { digitsForScore, generateProblem, play };

if (require.main === module) play().catch(console.error);
