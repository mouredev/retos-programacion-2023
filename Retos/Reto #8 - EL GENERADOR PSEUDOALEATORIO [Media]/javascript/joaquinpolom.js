// Reto 8 joaquinpolom

/*
 * Crea un generador de números pseudoaleatorios entre 0 y 100.
 * - No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
 *
 * Es más complicado de lo que parece...
 */

// Xn = (aXn-1 + b)mod m

let a = 5;
let b = 20;
let m = 100;
let i = Date.now() % 2500;
var x = Date.now() % 100;

function genNumRandom(x) {
  while (i > 0) {
    i --;
    var x = (a * x + b) % m;
    genNumRandom(x);
  }
  return x;
}

//console.log(x);
var x = genNumRandom(x);
console.log(x);
