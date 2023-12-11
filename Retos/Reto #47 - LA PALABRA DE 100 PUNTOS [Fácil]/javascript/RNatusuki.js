const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.question("Ingresa una palabra: ", (word) => {
  const points = [...word].reduce((acc, char) => {
    if (char === "ñ") {
      return acc + 15;
    } else {
      const point = char.charCodeAt(0) - 96;
      return acc + (point >= 15 ? point + 1 : point);
    }
  }, 0);

  console.log(`Puntos: ${points}`);

  rl.close();
});