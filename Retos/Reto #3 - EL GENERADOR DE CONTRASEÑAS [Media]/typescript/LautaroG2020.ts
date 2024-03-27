/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */
const RULES = {
    maxLength: 16,
    minLength: 8
}

const lowercaseChars = "abcdefghijklmnopqrstuvwxyz";
const uppercaseChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
const numericChars = "0123456789";
const symbolChars = "!@#$%^&*()_+-=[]{}|;:,.<>?";

const GeneratePassword = (lengthPassword: number, uppercase: boolean = true, allowNumber: boolean = true, specialCharacter: boolean = true) => {
    let newPassword : string = "";
    let result : string = "";
    if (!ValidParams(lengthPassword)) return console.log("El número de caracteres no esta dentro del mínimo o máximo permitido.");  

    if(uppercase) result += uppercaseChars;

    if(allowNumber) result += numericChars;

    if(specialCharacter) result += symbolChars;

    for (let index = 0; index < lengthPassword; index++) {
        const ramdonIndex = GenerateRandomNumber(1, result.length - 1);
        newPassword += result[ramdonIndex];
    };

    return console.log(`La contraseña generada es: ${newPassword}`)
};

const GenerateRandomNumber = (min: number, max: number): number => {
    return Math.floor(Math.random() * (max - min + 1)) + min;
};

const ValidParams = (length: number) => {
    if (length > RULES.maxLength) return false;
    if (length < RULES.minLength) return false;

    return true;
};

GeneratePassword(12);
GeneratePassword(18);
GeneratePassword(15, true, false, false);
GeneratePassword(8, false, true, true);
GeneratePassword(10, false, true, false);
