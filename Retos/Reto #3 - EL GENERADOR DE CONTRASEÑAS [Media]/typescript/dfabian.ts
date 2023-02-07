/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */
type PasswordConfig = {
  length: number;
  hasUpperCase?: boolean;
  hasNumbers?: boolean;
  hasSymbols?: boolean;
}

const passwordGenerator = (passwordConfig: PasswordConfig = {length: 8, hasUpperCase: false, hasNumbers: false, hasSymbols: false}): string => {
  const {length, hasUpperCase, hasNumbers, hasSymbols} = passwordConfig;
  const characters: string = 'abcdefghijklmnopkrstuvwxyz';
  const numbers: string = '1234567890';
  const symbols: string = '!@#%&/()=?';
  let validLength: number = length;
  let validCharacters: string = characters;

  if (length < 8) validLength = 8;
  if (length > 16) validLength = 16;

  if (hasUpperCase) validCharacters += characters.toUpperCase();
  if (hasNumbers) validCharacters += numbers;
  if (hasSymbols) validCharacters += symbols;

  const passwordCharacters: string[] = Array.from(validCharacters);
  const pwdLength: number = passwordCharacters.length;
  let password: string = '';

  for (let i = 0; i < validLength; i++) {
    const random: number = Math.random() * passwordCharacters.length;
    const randomInt: number = Math.floor(random);
    password += passwordCharacters[randomInt];
  }

  return password;
}

console.log(passwordGenerator());
console.log(passwordGenerator({length: 3, hasUpperCase: true}));
console.log(passwordGenerator({length: 10, hasUpperCase: true}));
console.log(passwordGenerator({length: 22, hasNumbers: true}));
console.log(passwordGenerator({length: 16, hasSymbols: true}));
console.log(passwordGenerator({length: 16, hasUpperCase: true, hasNumbers: true, hasSymbols: true}));