/*
 *	¡El nuevo "The Legend of Zelda: Tears of the Kingdom" ya está disponible! 
 *
 * Crea un programa que dibuje una Trifuerza de "Zelda"
 * formada por asteriscos.
 * - Debes indicarle el número de filas de los triángulos con un entero positivo (n).
 * - Cada triángulo calculará su fila mayor utilizando la fórmula 2n-1.
 *
 * Ejemplo: Trifuerza 2
 * 
 *    *
 *   ***
 *  *   *
 * *** ***
 *
 */

 const buildTreeForce = (n) => {
  let tree = '';
  const width = 2 * n - 1;
  for (let i = 1; i <= n; i++) {
    const upSpaces = ' '.repeat(width + 2 - i * 2);
    const upAsterisks = `${upSpaces}${'*   '.repeat(i - 1)}*${upSpaces}`;
    const downSpaces = ' '.repeat(2 * n - i * 2);
    const downAsterisks = `${`${'*'.repeat(3)} `.repeat(i - 1)}${'*'.repeat(3)}`;
    const downAsterisksCompleted = downSpaces + downAsterisks + downSpaces;
    tree += `${upAsterisks}\n${downAsterisksCompleted}\n`;
  }
  return tree.slice(0, -1);
};

// Visita mi repo en GitHub para ver y correr los tests de este código --> https://github.com/marcode24/weekly-challenges
