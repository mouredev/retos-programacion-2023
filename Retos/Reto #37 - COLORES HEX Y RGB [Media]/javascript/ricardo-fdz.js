/*
 * Crea las funciones capaces de transformar colores HEX
 * a RGB y viceversa.
 * Ejemplos:
 * RGB a HEX: r: 0, g: 0, b: 0 -> #000000
 * HEX a RGB: hex: #000000 -> (r: 0, g: 0, b: 0)
 */

const hex = [0, 1]


function hexToRgb(hex) {
  hex = hex.slice(1);
  const hexArray = [hex.slice(0, 2), hex.slice(2, 4), hex.slice(4, 6)]
  return `(r: ${parseInt(hexArray[0], 16)}, g:${parseInt(hexArray[1], 16)}, b:${parseInt(hexArray[2], 16)} )`;
}

function rgbToHex(rgb) {
  const array = rgb
  .slice(1, -1)
  .split(',')
  .map(x => parseInt(x.split(':')[1]).toString(16) == '0' ? '00' : parseInt(x.split(':')[1]).toString(16))
  console.log('#'+array.join(''))

}


hexToRgb('#aa7800')
rgbToHex('(r:170, g:120, b:0 )')





