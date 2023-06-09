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

const row = "═";
const column = "║";
const topRight = "╗";
const bottomRight = "╝";
const bottomLeft = "╚";
const topLeft = "╔";


function dibujarEspiral(size){
  if(size < 1){
    console.error(`La espiral debe ser de tamaño positivo`);
    return;
  }
  
  for(let line = 0; line < size; line ++){
    let result = "";

    if(line*2 < size) {
      result += (column.repeat(line > 1 ? line - 1 : 0) + 
                 topLeft.repeat(line > 0 ? 1 : 0) + 
                 row.repeat(size - line * 2 - 1 ) + 
                 topRight + 
                 column.repeat(line));
    } else {
      result += (column.repeat(size - line - 1) + 
                 bottomLeft + 
                 row.repeat(line * 2 - size) + 
                 bottomRight + 
                 column.repeat(size - line -1));
    }
    
    console.log(result);
  }
  
     
  
  
}

dibujarEspiral(3);
dibujarEspiral(4);
dibujarEspiral(5);
dibujarEspiral(10);
dibujarEspiral(20);
