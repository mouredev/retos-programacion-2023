const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('Ingresa una palabra: ', (word) => {
  const points = word
    .split('')
    .map((char) => char.charCodeAt(0) - 96)
    .map((point) => (point >= 15 ? point + 1 : point))
    .reduce((acc, curr) => acc + curr, 0);

  console.log(`Puntos: ${points}`);

  rl.close();
});
