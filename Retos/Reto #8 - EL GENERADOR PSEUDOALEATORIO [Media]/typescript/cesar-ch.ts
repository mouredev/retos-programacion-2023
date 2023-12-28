/*
 * Crea un generador de números pseudoaleatorios entre 0 y 100.
 * - No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
 *
 * Es más complicado de lo que parece...
 */

let timeNow: number = new Date().getMilliseconds();

function random(timeNow: number): number {
  return Math.ceil(timeNow / 10);
}

console.log(random(timeNow));
