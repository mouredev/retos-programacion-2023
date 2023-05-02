/*
 * Crea un generador de números pseudoaleatorios entre 0 y 100.
 * - No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
 *
 * Es más complicado de lo que parece...
 */

const numbers = Array.from({ length: 101 }, (_, index) => ({
  index,
}));
// get random number from array
function getNumber() {
  return numbers[Math.floor(Math.random() * numbers.length)].index;
}

console.log(getNumber());
