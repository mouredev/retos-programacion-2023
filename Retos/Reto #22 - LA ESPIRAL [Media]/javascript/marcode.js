/*
 * Crea una función que dibuje una espiral como la del ejemplo.
 * - Únicamente se indica de forma dinámica el tamaño del lado.
 * - Símbolos permitidos: ═ ║ ╗ ╔ ╝ ╚
 *
 * Ejemplo espiral de lado 5 (5 filas y 5 columnas):
 * ════╗
 * ╔══╗║
 * ║╔╗║║
 * ║╚═╝║
 * ╚═══╝
 */

const drawSpiral = (size) => {
  const up = Math.ceil(size / 2);
  let result = `${'═'.repeat(size - 1)}╗\n`;
  for (let row = 1; row < up; row++) {
    result += `${'║'.repeat(row - 1)}╔${'═'.repeat(size - (2 * row) - 1)}╗${'║'.repeat(row)}\n`;
  }
  for (let row = up; row < size; row++) {
    result += `${'║'.repeat(size - row - 1)}╚${'═'.repeat((2 * row) - size)}╝${'║'.repeat(size - row - 1)}\n`;
  }
  return result.slice(0, -1);
};

// Visita mi repo en GitHub para ver y correr los tests de este código --> https://github.com/marcode24/weekly-challenges
