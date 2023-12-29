/*
 * Crea una función que encuentre todos los triples pitagóricos
 * (ternas) menores o iguales a un número dado.
 * - Debes buscar información sobre qué es un triple pitagórico.
 * - La función únicamente recibe el número máximo que puede
 *   aparecer en el triple.
 * - Ejemplo: Los triples menores o iguales a 10 están
 *   formados por (3, 4, 5) y (6, 8, 10).
 */


const pythagoreanTriples = maxNum => {
    // Check if given data is correct
    if (typeof maxNum !== "number") {
        console.log('Given data must be a number');
        return [];
    }

    if (maxNum <= 1) {
        console.log('Given number must be greater than 1');
        return [];
    }

    // Find pythagorean triples
    const triples = [];
    for (let a = 1; a <= maxNum; a++) {
        for (let b = a; b <= maxNum; b++) {
            const abSquare = a**2 + b**2;
            const c = abSquare**0.5;

            if (c > maxNum) {
                break;
            }

            if (abSquare == parseInt(c)**2) {
                triples.push([a, b, c]);
            }
        }
    }

    return triples;
};


console.log(pythagoreanTriples(10));        // [[3, 4, 5], [6, 8, 10]]