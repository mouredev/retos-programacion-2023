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

function drawTriforce(n) {
    let whiteSpace = 2 * n - 1
    let start = 1
    const rows = n * 2
    let res = ""

    for (let i = 0; i < n; i++) {
        res += " ".repeat(whiteSpace) + "*".repeat(start) + "\n";
        start += 2;
        whiteSpace--;
    }
    start = 1

    let whiteSpace2 = whiteSpace + n
    for (let i = 0; i < rows / 2; i++) {
        res += " ".repeat(whiteSpace) + "*".repeat(start) + " ".repeat(whiteSpace2) + "*".repeat(start) + "\n"
        start += 2
        whiteSpace--
        whiteSpace2 -= 2
    }

    return res

}



console.log(drawTriforce(4));