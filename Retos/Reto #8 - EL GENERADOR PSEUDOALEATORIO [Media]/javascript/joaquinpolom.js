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
let i = 5;
//var x = 0.0;
// var x = Date.now().GetMilliseconds() / 10;
var x = () => {
  // Get the time
  const ahora = new Date.now();
  return (ahora.GetMilliseconds() / 10);
}

function initSeed() {
  // Init the seed
  // Get the time
  const ahora = new Date.now();
  var x = (ahora.GetMilliseconds()) / 10;
  return x;
}

function genNumRandom(x) {
  while (i > 0) {
    i --;
    var x = (a * x + b) % m;
    genNumRandom(x);
  }
}

initSeed();
genNumRandom(x);
console.log(x);
