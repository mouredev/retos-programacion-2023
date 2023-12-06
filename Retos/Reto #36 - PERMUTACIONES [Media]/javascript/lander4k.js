/*
 * Crea un programa que sea capaz de generar e imprimir todas las 
 * permutaciones disponibles formadas por las letras de una palabra.
 * - Las palabras generadas no tienen por qué existir.
 * - Deben usarse todas las letras en cada permutación.
 * - Ejemplo: sol, slo, ols, osl, los, lso 
 */

function generarPermutaciones(palabra) {
    function permutar(prefix, str) {
        const n = str.length;
        if (n === 0) {
            console.log(prefix);
        } else {
            for (let i = 0; i < n; i++) {
                permutar(prefix + str.charAt(i), str.substring(0, i) + str.substring(i + 1, n));
            }
        }
    }

    permutar('', palabra);
}

const palabra = 'sol';

generarPermutaciones(palabra);

