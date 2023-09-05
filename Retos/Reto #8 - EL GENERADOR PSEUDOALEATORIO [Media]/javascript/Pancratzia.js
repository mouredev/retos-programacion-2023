/*
 * Crea un generador de números pseudoaleatorios entre 0 y 100.
 * - No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
 *
 * Es más complicado de lo que parece...
 * 
 * 
 * 
 * CREADO POR PANCRATZIA - 25/08/2023
 */

const random = () => parseInt(new Date().getMilliseconds() * (performance.now() + performance.timeOrigin) % 101);

console.log(random())
console.log(random())
console.log(random())
console.log(random())