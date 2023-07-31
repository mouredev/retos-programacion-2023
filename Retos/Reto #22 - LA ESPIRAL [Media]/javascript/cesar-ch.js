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
    let spiral = ''

    spiral += '═'.repeat(size - 1) + '╗' + '\n'

    for (let i = 0; i < Math.ceil(size / 2) - 1; i++) {
        spiral += '║'.repeat(i) + '╔' + '═'.repeat(size - 3 - (2 * i)) + '╗' + '║'.repeat(i + 1) + '\n'
    }

    for (let i = Math.ceil(size / 2); i < size; i++) {
        spiral += '║'.repeat(size - i - 1) + '╚' + '═'.repeat(2 * i - size) + '╝' + '║'.repeat(size - i - 1) + '\n'
    }

    return spiral
}

console.log(drawSpiral(3))
