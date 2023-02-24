/*
 * Crea un generador de números pseudoaleatorios entre 0 y 100.
 * - No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
 *
 * Es más complicado de lo que parece...
 */

const numberRandom = () => {
  let nowTime = Date.now();
  return Math.floor(nowTime * 1000000) % 101;
};
console.log(numberRandom());
