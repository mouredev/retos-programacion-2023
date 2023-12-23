/*
 * Crea una función que calcule el número de la columna de una hoja de Excel
 * teniendo en cuenta su nombre.
 * - Las columnas se designan por letras de la "A" a la "Z" de forma infinita.
 * - Ejemplos: A = 1, Z = 26, AA = 27, CA = 79.
 */

const columnToNumber = (column) => {
  let number = 0;
  for (let i = 0; i < column.length; i++) {
    number = number * 26 + column.charCodeAt(i) - 64;
  }
  return number;
};

// Visita mi repo en GitHub para ver y correr los tests de este código --> https://github.com/marcode24/weekly-challenges
