/*
 * Crea un generador de números pseudoaleatorios entre 0 y 100.
 * - No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
 *
 * Es más complicado de lo que parece...
*/

class RandomGenerator {
  #counter = 1;
  #previousRandom = 1;

  constructor() {
  }

  rand (max: number = 100) {
    const time = new Date().getTime();
    const randValue = ((time / this.#counter) / (this.#previousRandom + 1 )) % max;
    this.#counter++;
    this.#previousRandom = randValue;
    return randValue;
  } 
}

const randomG = new RandomGenerator();
console.log(randomG.rand());
console.log(randomG.rand());
console.log(randomG.rand());
console.log(randomG.rand());
console.log(randomG.rand());
console.log(randomG.rand());
console.log(randomG.rand());