/*
 * Crea un generador de números pseudoaleatorios entre 0 y 100.
 * - No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
 *
 * Es más complicado de lo que parece...
 */

type Input = void;
type Output = number;

let seed = Date.now() % 100;

function random(): Output {
  const newSeed = (seed * seed + seed + 4321).toString().padStart(4, '0').slice(1, 3);
  seed = Number(newSeed);
  return seed;
}

Array.from({ length: 10 }).forEach(() => console.log(random()));
