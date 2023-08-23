/*
 *	¡El nuevo "The Legend of Zelda: Tears of the Kingdom" ya está disponible! 
 *
 * Crea un programa que dibuje una Trifuerza de "Zelda"
 * formada por asteriscos.
 * - Debes indicarle el número de filas de los triángulos con un entero positivo (n).
 * - Cada triángulo calculará su fila mayor utilizando la fórmula 2n-1.
 *
 * Ejemplo: Trifuerza 2
 * 
 *    *
 *   ***
 *  *   *
 * *** ***
 *
*/
"use strict"

function trifuerza(filas) {
  let dobleFilas = filas * 2;
  let asterisco = '';
  let espacio = '';
  let espacio2 = ''; 
  for(let nFila = 1; nFila <= dobleFilas; nFila++) {
    if(nFila <= filas){
      asterisco = '*'.repeat(nFila * 2 - 1);
      espacio = ' '.repeat(dobleFilas - nFila);
      console.log(espacio + asterisco);
    } else {
      asterisco = '*'.repeat((nFila - filas) * 2 - 1);
      espacio = ' '.repeat(dobleFilas - nFila);
      espacio2 = ' '.repeat((dobleFilas - (nFila - 1)) * 2 - 1);
      console.log(espacio + asterisco + espacio2 + asterisco);
    }
  }
}

trifuerza(1);
trifuerza(2);
trifuerza(4);
trifuerza(8);
trifuerza(16);