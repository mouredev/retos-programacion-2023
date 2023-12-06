/*
 * Crea una función que dibuje una escalera según su número de escalones.
 * - Si el número es positivo, será ascendente de izquiera a derecha.
 * - Si el número es negativo, será descendente de izquiera a derecha.
 * - Si el número es cero, se dibujarán dos guiones bajos (__).
 *
 * Ejemplo: 4
 *         _
 *       _|
 *     _|
 *   _|
 * _|
 *
 */

const buildStairs = (n) => {
  let stairs = '_';
  if (n < 0) {
    Array.from({ length: Math.abs(n) }, (_, i) => i).forEach((i) => {
      stairs += `\n${' '.repeat(1 + i * 2)}|_`;
    });
    return stairs;
  }
  if (n > 0) {
    let spaces = ' '.repeat(n * 2);
    stairs = `${spaces}${stairs}`;
    Array.from({ length: n }, (_, i) => i + 1).forEach(() => {
      spaces = spaces.slice(0, -2);
      stairs += `\n${spaces}_|`;
    });
    return stairs;
  }
  return `${stairs}_`;
};

// Visita mi repo en GitHub para ver y correr los tests de este código --> https://github.com/marcode24/weekly-challenges
