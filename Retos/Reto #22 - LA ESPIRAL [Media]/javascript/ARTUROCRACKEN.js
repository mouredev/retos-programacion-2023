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
 * 
 * ═╗
 * ╚╝
 * 
 * ══╗
 * ╔╗║
 * ╚═╝
 * 
 * ═══╗
 * ╔═╗║
 * ║╚╝║
 * ╚══╝
 */

function spiral(size) {
  // validations
  if (typeof size !== 'number') {
    console.error("size must be a number");
    return;
  }
  if (size < 2) {
    console.error("size must be greater than 1");
    return;
  }

  let half = (Math.ceil(size / 2));
  let pointer = 0;
  let half2 = 0;
  
  // Print spiral
  for (let r = 0; r < size; r++) {
    if (size % 2 !== 0) {
      if (r < half) {
        pointer += 1;
      } else {
        pointer -= 1;
      }
    } else {
      if (r < half) {
        pointer += 1;
      } else if (r === half) {
        if (half2 > 0) {
          pointer -= 1;
        } else {
          half2 += 1;
        }
      } else {
        pointer -= 1;
      }
    }
    let rowValue = "";
    let isUpper = (r + 1) <= half;
    
    for (let c = 0; c < size; c++) {
      let leftCorner = (c === (pointer - 2) && (r !== 0));
      if (!isUpper) {
        leftCorner = (c === (pointer - 1));
      }
      let rightCorner = (c === (size - pointer));
      

      if (r === 0) {
        if (leftCorner) {
          rowValue += "╔"
        } else if (rightCorner) {
          rowValue += "╗"
        } else {
          rowValue += "═"
        }
      } else if (isUpper && r !== 0) {
        if (leftCorner) {
          rowValue += "╔"
        } else if (rightCorner) {
          rowValue += "╗"
        } else if (c < (size - pointer) && c > (pointer - 2)) {
          rowValue += "═"
        } else {
          rowValue += "║"
        }
      } else if (r === (size - 1)) {
        if (leftCorner) {
          rowValue += "╚"
        } else if (rightCorner) {
          rowValue += "╝"
        } else {
          rowValue += "═"
        }
      } else {

        if (leftCorner) {
          rowValue += "╚"
        } else if (rightCorner) {
          rowValue += "╝"
        } else if (c < (size - pointer) && c > (pointer - 1)) {
          rowValue += "═"
        } else {
          rowValue += "║"
        }
      }
    }
    console.log(rowValue);
    
  }

}

spiral(2);
spiral(5);
spiral(10);
spiral(20);
