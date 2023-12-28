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

 function dibujarTriFuerza(n = 1) {

    baseTriangulo = 2*n - 1;
    let trifuerza = "";

    for (let i = 0; i < n; i++) {
        trifuerza += " ".repeat(baseTriangulo - i) + "*".repeat(2 * i + 1) + "\n";
    }


    let espaciosDer = n-1;
    let espaciosIzq = 2*n - 1;

    //Dibujo los dos triangulos inferiores
    for (let i = 0; i < n; i++) {

        trifuerza += " ".repeat(espaciosDer) + "*".repeat(2 * i + 1) + " ".repeat(espaciosIzq) + "*".repeat(2 * i + 1) + "\n";

        espaciosDer--;
        espaciosIzq-=2;
    }

    console.log(trifuerza);
 }

 dibujarTriFuerza(2);
 dibujarTriFuerza(3);
 dibujarTriFuerza(10);
 