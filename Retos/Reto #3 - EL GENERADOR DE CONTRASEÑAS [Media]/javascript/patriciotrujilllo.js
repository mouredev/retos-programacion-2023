/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */

function generatePassword(a) {
    if (typeof (a) !== 'number') return "Parameters must be a number"

    let password = ''
    const characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+[]{}|;:,.<>?';
    for (let i = 0; i < a; i++) {
        const position = Math.floor(Math.random() * characters.length)
        random = characters[position]
        password = `${password}${random}`
    }

    return password
}

console.log(generatePassword(7))
console.log(generatePassword(17))
console.log(generatePassword(9))
console.log(generatePassword(14))