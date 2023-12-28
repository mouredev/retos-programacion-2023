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

function drawSpiral(size) {
    let horizontalUp = size - 2
    let horizontalDown = size % 2 === 0 ? 0 : 1
    let spiral = "═".repeat(size - 1) + "╗\n"

    for (let row = 1; row < size; row++) {
        let vertical
        if (row < size / 2) {
            vertical = row + row - 1
            spiral += "║".repeat(vertical - row) + "╔" + "═".repeat(horizontalUp - vertical) + "╗" + "║".repeat(vertical - row + 1) + "\n"
        } else {
            vertical = (size - horizontalDown - 2) / 2;
            spiral += "║".repeat(vertical) + "╚" + "═".repeat(horizontalDown) + "╝" + "║".repeat(vertical) + "\n"
            horizontalDown += 2
        }
    }
    return spiral
}

console.log(drawSpiral(5))

console.log(drawSpiral(7))

console.log(drawSpiral(9))

console.log(drawSpiral(6))

console.log(drawSpiral(8))

console.log(drawSpiral(10))