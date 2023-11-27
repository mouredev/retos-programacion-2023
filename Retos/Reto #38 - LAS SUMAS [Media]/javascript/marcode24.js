/*
 * Crea una función que encuentre todas las combinaciones de los números
 * de una lista que suman el valor objetivo.
 * - La función recibirá una lista de números enteros positivos
 *   y un valor objetivo.
 * - Para obtener las combinaciones sólo se puede usar
 *   una vez cada elemento de la lista (pero pueden existir
 *   elementos repetidos en ella).
 * - Ejemplo: Lista = [1, 5, 3, 2],  Objetivo = 6
 *   Soluciones: [1, 5] y [1, 3, 2] (ambas combinaciones suman 6)
 *   (Si no existen combinaciones, retornar una lista vacía)
 */

const getCombinations = ({ values, target }) => {
  const combinations = [];
  const find = (index, sum, combination) => {
    if (sum === target) {
      combinations.push(combination);
      return;
    }
    if (sum > target || index >= values.length) {
      return;
    }
    find(index + 1, sum, combination);
    find(index + 1, sum + values[index], [...combination, values[index]]);
  };
  find(0, 0, []);
  return combinations;
};

// Visita mi repo en GitHub para ver y correr los tests de este código --> https://github.com/marcode24/weekly-challenges
