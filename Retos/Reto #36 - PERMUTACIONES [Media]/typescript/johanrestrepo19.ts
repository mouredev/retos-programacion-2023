/*
 * Crea un programa que sea capaz de generar e imprimir todas las
 * permutaciones disponibles formadas por las letras de una palabra.
 * - Las palabras generadas no tienen por qué existir.
 * - Deben usarse todas las letras en cada permutación.
 * - Ejemplo: sol, slo, ols, osl, los, lso
 */

const addPermutations = (
  letter: string,
  currentPermutations: string[][]
): string[][] => {
  let result: string[][] = [];
  currentPermutations.forEach((permutation) => {
    for (let index = 0; index < permutation.length + 1; index++) {
      const newPerm = [...permutation];
      newPerm.splice(index, 0, letter);
      result.push(newPerm);
    }
  });
  return result;
};

const getPermutations = (word: string): string[][] => {
  const letters = word.split("");
  // Caso base
  if (letters.length === 2) return [[...letters], [...letters.reverse()]];

  // Caso recursivo
  return addPermutations(letters[0], getPermutations(word.slice(1)));
};

const printPermutations = (word: string): void => {
  const permutations = getPermutations(word).map((perm) => perm.join(""));
  console.table(permutations);
};

printPermutations("sol");
printPermutations("sola");
printPermutations("sun");
printPermutations("johan");
