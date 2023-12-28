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


function combinations(list, target) {
    const result = []
    
    function combine(subArray, startIndex, sum) {
      if (sum === target) {
        result.push([...subArray])
        return
      }  
      if (sum > target || startIndex === list.length) return 
    
      for (let i = startIndex; i < list.length; i++) {
        subArray.push(list[i])
        combine(subArray, i + 1, sum + list[i])
        subArray.pop()
  
        while (i < list.length - 1 && list[i] === list[i + 1]) {
          i++
        }
      }
    }  
    list.sort((a, b) => a - b)
    combine([], 0, 0)
    return result
  }

console.log(combinations([1, 5, 3, 2], 6)) // -> [[1, 5] , [1, 3, 2]]
console.log(combinations([1, 2, 3, 4, 5], 7)); // -> [[1, 2, 4], [2, 5], [3, 4]]
console.log(combinations([2, 2, 3, 4, 5], 6)); // -> [[2, 4]]
console.log(combinations([1, 2, 3, 4, 5], 10)); // -> [[1, 2, 3, 4], [1, 4, 5], [2, 3, 5]]
console.log(combinations([1, 2, 3, 4, 5], 11)); // -> [[1, 2, 3, 5], [2, 4, 5]]

