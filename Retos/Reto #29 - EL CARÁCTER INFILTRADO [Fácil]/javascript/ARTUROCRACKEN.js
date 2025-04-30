/*
 * Crea una función que reciba dos cadenas de texto casi iguales,
 * a excepción de uno o varios caracteres. 
 * La función debe encontrarlos y retornarlos en formato lista/array.
 * - Ambas cadenas de texto deben ser iguales en longitud.
 * - Las cadenas de texto son iguales elemento a elemento.
 * - No se pueden utilizar operaciones propias del lenguaje
 *   que lo resuelvan directamente.
 * 
 * Ejemplos:
 * - Me llamo mouredev / Me llemo mouredov -> ["e", "o"]
 * - Me llamo.Brais Moure / Me llamo brais moure -> [" ", "b", "m"]
 */

function detectDifferences(txt1, txt2) {
  if (typeof txt1 !== "string" || typeof txt2 !== "string") {
    console.error("Error: Both inputs must be strings.");
    return;
  }

  if (txt1.length !== txt2.length) {
    console.error("Error: Both inputs must have the same length.");
    return;
  }

  let discrepancies = [];

  for (let c = 0; c < txt1.length; c++) {
    if (txt1[c] !== txt2[c]) {
      discrepancies.push(txt2[c]);
    }
  }

  if (discrepancies.length > 0) {
    console.log(discrepancies);
  } else {
    console.log("There are no differences between the text strings.");
  }
  
}

detectDifferences("Me llamo mouredev", "Me llemo mouredov");
detectDifferences("Me llamo.Brais Moure", "Me llamo brais moure");
