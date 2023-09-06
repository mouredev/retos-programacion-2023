/*
 * Crea un programa que sea capaz de generar e imprimir todas las 
 * permutaciones disponibles formadas por las letras de una palabra.
 * - Las palabras generadas no tienen por qué existir.
 * - Deben usarse todas las letras en cada permutación.
 * - Ejemplo: sol, slo, ols, osl, los, lso 
 */

/* Algoritmo de Heap */

let word = 'holas'
let word2 = 'miercoles'
let word3 = 'camisetas'
let permutations = new Set()

function getPermutations(targetWord, inBuildWord, permutations) {
  if(!targetWord.length) {
    permutations.add(inBuildWord)
    console.log(inBuildWord)
  }
  
  for(let i = 0; i < targetWord.length; i++) 
    getPermutations(targetWord.slice(0, i) + targetWord.slice(i + 1), 
      inBuildWord + targetWord.slice(i, i + 1), 
    permutations)
}

console.time()
getPermutations(word, '', permutations)
console.log(permutations)
permutations = new Set()
getPermutations(word2, '', permutations)
console.log(permutations)
permutations = new Set()
getPermutations(word3, '', permutations)
console.log(permutations)
console.timeEnd()