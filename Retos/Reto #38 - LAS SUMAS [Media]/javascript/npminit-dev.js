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

function getSumsLists(list, target) {
  let sList = list.filter(num => num <= target).sort()
  let result = []

  function backTracking(sub, start, sum) {
    if(sum === target) result.push(sub)
    for(let i = start; i < sList.length; i++) 
      if(sum + list[i] <= target) backTracking([...sub, list[i]], i + 1, sum + list[i])
  }

  for(let i = 0; i < sList.length - 1; i++) 
    backTracking([list[i]], i + 1, list[i])
  return result
}

/* TEST */
console.log(getSumsLists([1, 5, 3, 2], 6)) 
/* result = [[1, 5], [1, 3, 2]] */
console.log(getSumsLists([3, 2, 1, 6, 8, 4, 3, 10], 12)) 
/* result = [[ 3, 2, 1, 6 ], [ 3, 2, 4, 3 ], [ 3, 1, 8 ], [ 3, 6, 3 ], [ 2, 1, 6, 3 ], [ 2, 6, 4 ], [ 2, 10 ], [ 1, 8, 3 ], [ 8, 4 ]] */
console.log(getSumsLists([3, 6, 9, 12, 15], 30)) 
/* result = [[ 3, 6, 9, 12 ], [ 3, 12, 15 ], [ 6, 9, 15 ]] */
console.log(getSumsLists([15, 10, 5, 2, 8, 10], 50)) 
/* result = [[15, 10, 5, 2, 8, 10]] */
console.log(getSumsLists([1, 2, 3, 2, 1], 3)) 
/* result = [[ 1, 2 ], [ 1, 2 ], [ 2, 1 ], [ 3 ], [ 2, 1 ]] */
