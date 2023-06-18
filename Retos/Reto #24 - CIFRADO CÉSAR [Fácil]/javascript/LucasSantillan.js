/*
 * Crea un programa que realize el cifrado César de un texto y lo imprima.
 * También debe ser capaz de descifrarlo cuando así se lo indiquemos.
 *
 * Te recomiendo que busques información para conocer en profundidad cómo
 * realizar el cifrado. Esto también forma parte del reto.
*/

function cifrarTexto(texto, semilla) {
  let transformer = '';
  for(let i=0; i<texto.length; i++) {
    let c = texto.charCodeAt(i)
    c = (c+semilla) > 255 ? (c + semilla + 32) - 256 : c + semilla ;
    transformer += String.fromCharCode(c)
  }
  return transformer;
}

function descifrarTexto(texto, semilla) {
  semilla = 256 - 32 - semilla;
  return cifrarTexto(texto, semilla);
}

let cifrado = cifrarTexto('¡Salve, César, los que van a morir te saludan!', 12)
let descifrado = descifrarTexto(cifrado, 12)

console.log(cifrado);
console.log(descifrado);
