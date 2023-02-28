/*
 * Crea un generador de números pseudoaleatorios entre 0 y 100.
 * - No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
 *
 * Es más complicado de lo que parece...
 */

let time = new Date().getMilliseconds();

function Random(time) {
  return Math.ceil(time / 10);
}

console.log(Random(time));
