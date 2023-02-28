const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let seed = Date.now();

const randomNumber = (a, m) => {
  let q = Math.floor(m / a);
  let r = m % a;

  seed = a * (seed % q) - r * Math.floor(seed / q);

  if (seed <= 0) {
    seed += m;
  }

  return Math.floor(seed);
}

rl.question("Cuantos numeros quieres generar?: ", async function(countStr) {
  const count = parseInt(countStr);
  const a = Date.now();
  const m = Date.now() * 10000;

  for (let i = 1; i <= count; i++) {
    console.log(`Número aleatorio ${i} es: ${1 + randomNumber(a, m) % 100}`);
    await new Promise(resolve => setTimeout(resolve, 3000));
  }

  rl.close();
});
