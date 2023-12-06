/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */

const generatePassword = ({
  length = 8, upperCase = true, numbers = true, symbols = true,
}) => {
  const alphabet = 'abcdefghijklmnopqrstuvwxyz';
  const numbersString = '0123456789';
  const symbolsString = '!@#$%^&*()_+-=[]{}/<>?';
  if (length < 8 || length > 16) return 'Invalid length';
  let password = '';
  let characters = alphabet;
  if (upperCase) characters += alphabet.toUpperCase();
  if (numbers) characters += numbersString;
  if (symbols) characters += symbolsString;
  while (password.length < length) {
    password += characters[Math.floor(Math.random() * characters.length)];
  }
  return password;
};

// Visita mi repo en GitHub para ver y correr los tests de este código --> https://github.com/marcode24/weekly-challenges
