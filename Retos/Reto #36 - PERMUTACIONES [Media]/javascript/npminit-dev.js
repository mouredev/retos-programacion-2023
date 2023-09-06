/*
 * Crea un programa que sea capaz de generar e imprimir todas las 
 * permutaciones disponibles formadas por las letras de una palabra.
 * - Las palabras generadas no tienen por qué existir.
 * - Deben usarse todas las letras en cada permutación.
 * - Ejemplo: sol, slo, ols, osl, los, lso 
 */

/* Algoritmo de Heap */

const word = 'holas'
const word2 = 'miercoles'
const word3 = 'camisetas'
let permutations = new Set()

function getPermutations(targetWord, inBuildWord, permutations) {
  if(!targetWord.length) {
    permutations.add(inBuildWord)
    return
  }
  
  for(let i = 0; i < targetWord.length; i++) {
    let prevValues = [targetWord, inBuildWord]
    inBuildWord += targetWord.slice(i, i + 1)
    targetWord = [...targetWord]
    targetWord.splice(i, 1)
    targetWord = targetWord.join('')
    getPermutations(targetWord, inBuildWord, permutations)
    targetWord = prevValues[0]
    inBuildWord = prevValues[1]
  }
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