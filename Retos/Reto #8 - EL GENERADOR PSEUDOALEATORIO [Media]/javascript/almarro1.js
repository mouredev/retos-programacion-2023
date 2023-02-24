/*
 * Crea un generador de números pseudoaleatorios entre 0 y 100.
 * - No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
 *
 * Es más complicado de lo que parece...
 */

// obtenemos la fecha actual en millis
const now = Date.now().toString();

// nos quedamos con las partes inicial y final
const segment1 = Number(now.slice(0, 6));
const segment2 = Number(now.slice(-3));

// obtenemos el restos de dividir ambas partes
const mod = segment1 % segment2;

// Aplicamos una fórmula que altere use los tres valores anteriores usando operaciones no lineales
const rand = Math.round((100 * ((segment2 * mod) / (segment1 - mod)))) % 101

console.log(rand)