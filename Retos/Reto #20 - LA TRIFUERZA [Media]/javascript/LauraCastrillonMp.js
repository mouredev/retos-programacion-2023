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

function dibujarTrifuerza(filas) {
    let espaciosBlancos = 2 * filas - 1
    let inicio = 1
    const rows = filas * 2
    let triFuerza = ""

    for (let i = 0; i < filas; i++) {
        triFuerza += " ".repeat(espaciosBlancos) + "*".repeat(inicio) + "\n";
        inicio += 2;
        espaciosBlancos--;
    }

    inicio = 1
    let espaciosBlancos2 = espaciosBlancos + filas
    for (let i = 0; i < rows / 2; i++) {
        triFuerza += " ".repeat(espaciosBlancos) + "*".repeat(inicio) + " ".repeat(espaciosBlancos2) + "*".repeat(inicio) + "\n"
        inicio += 2
        espaciosBlancos--
        espaciosBlancos2 -= 2
    }
    console.log(triFuerza)
}
dibujarTrifuerza(4)