/*
 * Crea un programa que sea capaz de solicitarte un número y se
 * encargue de imprimir su tabla de multiplicar entre el 1 y el 10.
 * - Debe visualizarse qué operación se realiza y su resultado.
 *   Ej: 1 x 1 = 1
 *       1 x 2 = 2
 *       1 x 3 = 3
 *       ... 
 */

const printMutliplications = (num) => {
  const results = [];
  for (let index = 0; index < 10; index++) {
    const legend = `${num} x ${index + 1} = ${num * (index + 1)}`;
    results.push(legend);
  }
  return results;
};

// Visita mi repo en GitHub para ver y correr los tests de este código --> https://github.com/marcode24/weekly-challenges
