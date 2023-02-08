/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */

interface IOptions {
  length: number;
  hasUppercase: boolean;
  hasNumbers: boolean;
  hasSymbols: boolean;
}

function generatePassword({length, hasNumbers, hasUppercase, hasSymbols }: IOptions): string {
  if (length < 8 || length > 16) {
    throw new Error('Invalid Length (8-16)');
  }

  let password = '';
  const uppercaseChars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
  const numbers = '0123456789';
  const symbols = '!#@$%*&~$*()_-+=|<>?/\\';
  const allChars = `abcdefghijklmnopqrstuvwxyz${numbers ? numbers : ''}${symbols ? symbols : ''}${uppercaseChars ? uppercaseChars : ''}`

  for (let i = 0; i < length; i++) {
    password += allChars.charAt(Math.floor(Math.random() * allChars.length));
  }

  return password;
}

console.log(generatePassword({
  length: 10,
  hasNumbers: true,
  hasUppercase: true,
  hasSymbols: true
}));
