/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */

const generatePassword = (uppercases, numbers, symbols, len) => {
  if (len >= 8 && len <= 16) {
    let password = "";
    let characters = "abcdefghijklmnopqrstuvwxyz";
    characters +=
      (uppercases ? "ABCDEFGHIJKLMNOPQRSTUVWXYZ" : "") +
      (numbers ? "0123456789" : "") +
      (symbols ? "!@#$%&*()_+" : "");

    for (let i = 0; i < len; i++) {
      password += characters.charAt(Math.random() * characters.length);
    }
    return password;
  }
};

console.log(generatePassword(false, true, true, 10));
