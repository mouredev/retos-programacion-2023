/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */

function generatePassword({
  hasUppercase,
  hasNumbers,
  hasSymbols,
  length = 8,
} = {}) {
  // Lowercase letters (a-z)
  let characters = Array.from({ length: 26 }, (_, i) =>
    String.fromCodePoint(97 + i)
  );

  if (hasUppercase) {
    // Uppercase letters (A-Z)
    const uppercaseLetters = Array.from({ length: 26 }, (_, i) =>
      String.fromCodePoint(65 + i)
    );

    characters.push(...uppercaseLetters);
  }

  if (hasNumbers) {
    // Numbers (0-9)
    const numbers = Array.from({ length: 10 }, (_, i) =>
      String.fromCodePoint(48 + i)
    );

    characters.push(...numbers);
  }

  if (hasSymbols) {
    // Symbols
    const symbols = Array.from("!@#$%^&*()-_=+[]{}|;:'\",.<>?/");
    characters.push(...symbols);
  }

  let password = "";

  for (let i = 0; i < length; i++) {
    password += characters[Math.floor(Math.random() * characters.length)];
  }

  return password;
}

generatePassword({
  hasUppercase: true,
  hasNumbers: true,
  hasSymbols: true,
  length: 10,
});
