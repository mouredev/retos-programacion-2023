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
 {
  function triforceDraw(floors: number): void {
    const length: number = 2 * floors;
    for (let level = 1; level <= floors; level++) {
      let line: string = '*'.repeat(2 * level - 1);
      const spaces = ' '.repeat((length + line.length /2 )  - line.length)
      line = spaces + line;
      console.log(line);
    }
  
    for (let level = 1; level <= floors; level++) {
      let line: string = '*'.repeat(2 * level - 1);
      let spaces = ' '.repeat(floors - level);
      line = spaces + line + spaces + spaces + ' ' + line;
      console.log(line);
    }
  }
  triforceDraw(9)
}