/*
 * Crea una función que dibuje una espiral como la del ejemplo.
 * - Únicamente se indica de forma dinámica el tamaño del lado.
 * - Símbolos permitidos: ═ ║ ╗ ╔ ╝ ╚
 *
 * Ejemplo espiral de lado 5 (5 filas y 5 columnas):
 * ════╗
 * ╔══╗║
 * ║╔╗║║
 * ║╚═╝║
 * ╚═══╝
*/
"use strict"

function espiral(lado) {
  let guion = '';
  let cornerI = '';
  let cornerD = '';
  let pipeF = '';
  let pipeC = '';
  for(let fila = 0; fila < lado; fila++){
    if(fila * 2 < lado) {
      guion = '═'.repeat((lado - 1) - (fila * 2));
      if(fila === 0){
        cornerD = '╗'
      } else {
        cornerI = '╔';
        cornerD = '╗'
        pipeF = '║'.repeat(fila);
        pipeC = '║'.repeat(fila - 1);
      }
      console.log(pipeC + cornerI + guion + cornerD + pipeF);
    } else {
      guion = '═'.repeat(fila * 2 - lado);
      cornerI = '╚'
      cornerD = '╝'
      pipeF = '║'.repeat(lado - (fila + 1));
      pipeC = '║'.repeat(lado - (fila + 1));
      console.log(pipeC + cornerI + guion + cornerD + pipeF);
    }
  }
}

espiral(1);
espiral(3);
espiral(5);
espiral(10);
espiral(20);
