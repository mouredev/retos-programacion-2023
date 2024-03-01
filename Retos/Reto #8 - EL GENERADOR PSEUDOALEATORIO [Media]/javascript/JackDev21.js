/*
 * Crea un generador de números pseudoaleatorios entre 0 y 100.
 * - No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
 *
 * Es más complicado de lo que parece...
 */



const random = () => {
  let now = new Date();
  let time = now.getMilliseconds() % 101;
  return time;
}

const results = new Set();

while (results.size < 100) {
  results.add(random());
}

console.log(Array.from(results));