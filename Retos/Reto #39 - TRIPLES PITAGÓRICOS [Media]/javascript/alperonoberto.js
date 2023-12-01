/*
 * Crea una función que encuentre todos los triples pitagóricos
 * (ternas) menores o iguales a un número dado.
 * - Debes buscar información sobre qué es un triple pitagórico.
 * - La función únicamente recibe el número máximo que puede
 *   aparecer en el triple.
 * - Ejemplo: Los triples menores o iguales a 10 están
 *   formados por (3, 4, 5) y (6, 8, 10).
 */

// Creamos dos punteros, uno para el primer elemento y otro para el segundo.
// Dada la fórmula de Pitágoras, a^2 + b^2 = c^2, de modo que c será igual a
// sqrt(a^2 + b^2). Para todos los números que encontremos que cumplan esta ecuación,
// comprobaremos si son enteros, menores o iguales al máximo dado y si i y j son iguales.
// Tras descartar todos los casos que no sirven, los agregamos al array que devolvemos.

function findPythagoreanTriples(max) {
    const triples = [];
    for (let i = 1; i <= max; i++) {
      for (let j = i + 1; j <= max; j++) {
        const maxCandidate = Math.sqrt(Math.pow(i, 2) + Math.pow(j, 2));
        if (Number.isInteger(maxCandidate) && maxCandidate <= max && i !== j) {
          triples.push([i, j, maxCandidate]);
        }
      }
    }
  
    return triples;
  }
  
  console.log(findPythagoreanTriples(5));
  console.log(findPythagoreanTriples(10));
  console.log(findPythagoreanTriples(15));
  console.log(findPythagoreanTriples(20));