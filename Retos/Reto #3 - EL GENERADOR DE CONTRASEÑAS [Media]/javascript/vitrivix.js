/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
*/

const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-_+=[]{}|;:,.<>?';

function passwordGenerator() {
    const useCharacters = characters.split(''), newPassword = [];
    for (let i = 0; i < 16; i++) {
        newPassword.push(useCharacters[Math.floor(Math.random() * 88 + 1)])
    }
    return newPassword.join('')
}
console.log(`Your new password is: ${passwordGenerator()}`)