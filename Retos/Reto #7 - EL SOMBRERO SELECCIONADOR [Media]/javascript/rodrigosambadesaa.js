'use strict';

const QUESTIONS = [
  ['¿Qué cualidad valoras más?', ['valor', 'ambición', 'lealtad', 'sabiduría']],
  ['¿Cómo afrontas un problema?', ['actúo', 'busco ventaja', 'ayudo', 'investigo']],
  ['¿Qué objeto escogerías?', ['espada', 'corona', 'copa', 'libro']],
  ['¿Qué te gustaría aprender?', ['duelo', 'liderazgo', 'sanación', 'hechizos']],
  ['¿Cómo te describen?', ['valiente', 'astuto', 'paciente', 'curioso']]
];
const HOUSES = ['Gryffindor', 'Slytherin', 'Hufflepuff', 'Ravenclaw'];

function selectHouse(answers) {
  if (!Array.isArray(answers) || answers.length < 5) throw new Error('Se necesitan cinco respuestas');
  const points = [0, 0, 0, 0];
  for (const answer of answers) {
    if (!Number.isInteger(answer) || answer < 0 || answer > 3) throw new Error('Respuesta no válida');
    points[answer]++;
  }
  return HOUSES[points.indexOf(Math.max(...points))];
}

async function askQuestions(input = process.stdin, output = process.stdout) {
  const readline = require('node:readline/promises');
  const terminal = readline.createInterface({ input, output });
  const answers = [];
  for (const [question, options] of QUESTIONS) {
    const answer = await terminal.question(`${question}\n${options.map((item, index) => `${index + 1}. ${item}`).join('\n')}\n> `);
    const index = Number(answer) - 1;
    if (!Number.isInteger(index) || index < 0 || index > 3) {
      terminal.close();
      throw new Error('Cada respuesta debe estar entre 1 y 4');
    }
    answers.push(index);
  }
  terminal.close();
  return selectHouse(answers);
}

module.exports = { QUESTIONS, selectHouse, askQuestions };

if (require.main === module) askQuestions().then(house => console.log(`Tu casa es ${house}`)).catch(console.error);
