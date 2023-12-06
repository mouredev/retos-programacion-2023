/*
 * Crea un generador de números pseudoaleatorios entre 0 y 100.
 * - No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
 *
 * Es más complicado de lo que parece...
 */

/**
 *  Retrieves a random number between 0 and 100
 *  @returns {number} Random number between 0 and 100
 */

function pseudoRandom(){
  const random = Date.now().toString().slice(-3)
  return Math.round(Number(random)/10);
}

console.log(pseudoRandom());