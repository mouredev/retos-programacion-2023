/*
 Crea un generador de números pseudoaleatorios entre 0 y 100.
 - No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
 
  Es más complicado de lo que parece...
*/

let valor_semilla = Date.now(); 
let a = 1103515245;
let c = 12345;
let m = Math.pow(2, 31)-1;

function numero_ramdom() {
  valor_semilla = (a * valor_semilla + c) % m;
  let respuesta = Math.floor(valor_semilla / (m / 101));
  return respuesta;
}

console.log(numero_ramdom());

