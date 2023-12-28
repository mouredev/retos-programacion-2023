/*
 * Crea un generador de números pseudoaleatorios entre 0 y 100.
 * - No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
 *
 * Es más complicado de lo que parece...
 */

const random = (): number => {
  const date = new Date();
  const time = date.getTime();
  const seed = time.toString().split('').map(Number);
  const random = seed.reduce((acc, curr, idx) => acc + curr * idx, 0);
  return random % 100;
}


console.log(random());
console.log(random());
console.log(random());