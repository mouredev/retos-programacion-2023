/*
 * Crea una función que encuentre todos los triples pitagóricos
 * (ternas) menores o iguales a un número dado.
 * - Debes buscar información sobre qué es un triple pitagórico.
 * - La función únicamente recibe el número máximo que puede
 *   aparecer en el triple.
 * - Ejemplo: Los triples menores o iguales a 10 están
 *   formados por (3, 4, 5) y (6, 8, 10).
 */

const pythagoreanTriples = (max) => {
    const result = []   
    for (let i = max; i > 0; i--) {
        for (let j = i - 1; j > 0; j--) {
            const k = Math.sqrt(Math.pow(i, 2) + Math.pow(j, 2))
            Number.isInteger(k) && k<= max && result.push([j, i, k])        
        }
    }
    return result
}

console.log(pythagoreanTriples(10)) // --> [ [ 6, 8, 10 ], [ 3, 4, 5 ] ]
console.log(pythagoreanTriples(15)) // --> [ [ 9, 12, 15 ], [ 5, 12, 13 ], [ 6, 8, 10 ], [ 3, 4, 5 ] ]
console.log(pythagoreanTriples(25)) // --> [ [ 7, 24, 25 ], [ 15, 20, 25 ], [ 12, 16, 20 ], [ 8, 15, 17 ], [ 9, 12, 15 ], [ 5, 12, 13 ], [ 6, 8, 10 ], [ 3, 4, 5 ] ]
