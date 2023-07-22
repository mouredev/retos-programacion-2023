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

const findCharInfiltrated = (str1, str2) => {
  if (str1.length !== str2.length) {
    return 'Las cadenas no tienen la misma longitud';
  }

  const charInfiltrated = [];
  str1.split('').forEach((char, index) => {
    if (char !== str2[index]) {
      charInfiltrated.push(str2[index]);
    }
  });

  return charInfiltrated;
};

// Visita mi repo en GitHub para ver y correr los tests de este código --> https://github.com/marcode24/weekly-challenges
