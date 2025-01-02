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

const trifuerza = (n) => {
  if (n < 1) {
    console.log(
      "\nEl número ingresado debe ser mayor que 0:\n   ingresaste " + n + "\n"
    );
  } else {
    for (let i = 0; i < n * 2; i++) {
      if (i < n) {
        let startSpace = " ".repeat(n * 2 - 1 - i);
        let printRow = "*".repeat(2 * (i + 1) - 1);
        console.log(`${startSpace}${printRow}`);
      } else {
        let currentRow = i - n;
        let startSpace = " ".repeat(n - currentRow - 1);
        let middlespace = " ".repeat(2 * (n - currentRow) - 1);
        let printRow = "*".repeat(2 * (currentRow + 1) - 1);
        console.log(`${startSpace}${printRow}${middlespace}${printRow}`);
      }
    }
  }
};

trifuerza(2);
trifuerza(3);
trifuerza(10);
trifuerza(0);
trifuerza(-20);
