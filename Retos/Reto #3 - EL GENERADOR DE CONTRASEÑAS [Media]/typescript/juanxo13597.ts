/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */

export function generatePassword(length: number, upperCase: boolean, numbers: boolean, symbols: boolean): string {
    const alphabet = 'abcdefghijklmnopqrstuvwxyz';
    const numbersStr = '0123456789';
    const symbolsStr = '!@#$%^&*()_+~`|}{[]:;?><,./-=';
    let password = '';

    for (let i = 0; i < length; i++) {
        let char = alphabet[Math.floor(Math.random() * alphabet.length)];
        if (upperCase) {
            char = Math.random() > 0.5 ? char.toUpperCase() : char;
        }
        if (numbers) {
            char = Math.random() > 0.5 ? numbersStr[Math.floor(Math.random() * numbersStr.length)] : char;
        }
        if (symbols) {
            char = Math.random() > 0.5 ? symbolsStr[Math.floor(Math.random() * symbolsStr.length)] : char;
        }
        password += char;
    }

    return password;
}
