/*
 * Crea una función que encuentre todos los triples pitagóricos
 * (ternas) menores o iguales a un número dado.
 * - Debes buscar información sobre qué es un triple pitagórico.
 * - La función únicamente recibe el número máximo que puede
 *   aparecer en el triple.
 * - Ejemplo: Los triples menores o iguales a 10 están
 *   formados por (3, 4, 5) y (6, 8, 10).
 */

const pythagoreanTriple = (n) => {
  const triples = [];

  for (let a = 1; a <= n; a++) {
    const aSquared = a * a;

    for (let b = a + 1; b <= n; b++) {
      const bSquared = b * b;
      const cSquared = aSquared + bSquared;
      const c = Math.sqrt(cSquared);

      if (c <= n && c === Math.floor(c)) {
        triples.push([a, b, c]);
      }
    }
  }

  return triples;
};

// Visita mi repo en GitHub para ver y correr los tests de este código --> https://github.com/marcode24/weekly-challenges
