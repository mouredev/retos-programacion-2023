/*
 * Crea un programa que sea capaz de generar e imprimir todas las 
 * permutaciones disponibles formadas por las letras de una palabra.
 * - Las palabras generadas no tienen por qué existir.
 * - Deben usarse todas las letras en cada permutación.
 * - Ejemplo: sol, slo, ols, osl, los, lso 
 */

const getPermutations = (str) => {
  if (str.length <= 1) return [str];
  const permutations = [];
  for (let i = 0; i < str.length; i++) {
    const char = str[i];
    const remaining = str.slice(0, i) + str.slice(i + 1);
    const remainingPermutations = getPermutations(remaining);
    for (let j = 0; j < remainingPermutations.length; j++) {
      const permutation = char + remainingPermutations[j];
      permutations.push(permutation);
    }
  }
  return permutations;
};

// Visita mi repo en GitHub para ver y correr los tests de este código --> https://github.com/marcode24/weekly-challenges
