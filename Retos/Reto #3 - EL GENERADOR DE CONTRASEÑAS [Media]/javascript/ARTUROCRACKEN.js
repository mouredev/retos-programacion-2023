/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */

// Create a function to generate random passwords

const charactersAlpha = "abcdefghijklmnopqrstuvwxyz";
const numericCharacters = "1234567890";
const specialCharacters = "!@#$%^&*{}?:-+";

const randomPassword = ({
  length = 8,
  mayus = false,
  numbers = false,
  symbols = false,
}) => {
  if (
    typeof length !== "number" ||
    typeof mayus !== "boolean" ||
    typeof numbers !== "boolean" ||
    typeof symbols !== "boolean"
  ) {
    console.error(
      "Error: Invalid input.\n    Input must be: ({ int, boolean, boolean, boolean })"
    );
    return "";
  } else if (length < 8 || length > 16) {
    console.error(
      "Error: Invalid input.\n    The number must be between 8 and 16."
    );
    return "";
  }

  let validCharacters = "";
  validCharacters += charactersAlpha;
  let password = "";

  // TODO: Agregar los caracteres validos a la variable
  if (mayus) {
    validCharacters += charactersAlpha.toUpperCase();
  }
  if (numbers) {
    validCharacters += numericCharacters;
  }
  if (symbols) {
    validCharacters += specialCharacters;
  }

  let max = validCharacters.length - 1;
  let min = 0;

  // TODO: Crear un bucle que me devuelva entre 8 y 16 caracteres
  for (let i = 0; i < length; i++) {
    let randomNum = Math.round(Math.random() * (max - min) + min);
    password += validCharacters[randomNum];
  }

  return password;
};

console.log("\nPassword 1:\n");

console.log(
  randomPassword({ length: 16, mayus: true, numbers: true, symbols: true })
);

console.log("\nPassword 2:\n");

console.log(
  randomPassword({ length: 8, mayus: true, numbers: true, symbols: true })
);

console.log("\nPassword 3:\n");

console.log(
  randomPassword({ length: 1, mayus: true, numbers: true, symbols: true })
);

console.log("\nPassword 4:\n");

console.log(
  randomPassword({ length: 10, mayus: true, numbers: 4, symbols: "yes" })
);

console.log("\nPassword 5:\n");

console.log(randomPassword({ length: 13, numbers: true, symbols: true }));
