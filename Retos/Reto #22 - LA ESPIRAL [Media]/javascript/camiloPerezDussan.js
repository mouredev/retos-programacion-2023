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

let espiral = size => {
    let espiral = '═'.repeat(size - 1) + '╗'
    for (let row = 1; row < size; row++) {
        espiral += row < size / 2 ?
            `\n${'║'.repeat(row - 1)}╔${'═'.repeat(size - (row * 2 + 1))}╗${'║'.repeat(row)}` :
            `\n${'║'.repeat(size - row - 1)}╚${'═'.repeat(row * 2 - size)}╝${'║'.repeat(size - row - 1)}`
    }
    console.log(espiral)
};

espiral(1)
espiral(3)
espiral(5)
espiral(8)
espiral(10)
espiral(20)