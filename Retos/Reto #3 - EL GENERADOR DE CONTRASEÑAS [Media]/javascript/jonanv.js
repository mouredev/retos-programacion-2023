function generatePassword(length, upperCaseLetter, number, symbol) {
  let password = '';
  let lowerCase = 'abcdefghijklmnopqrstuvwxzy';
  let upperCase = 'ABCDEFGHIJKLMNOPQRSTUVWXZY';
  let numbers = '1234567890';
  let symbols = '!·$%&/()=?¿¡#@|*{}[]+-^`\'"';

  if (length >= 8 && length <= 16) {
    let characters = lowerCase 
                    + (upperCaseLetter ? upperCase : '')
                    + (number ? numbers : '')
                    + (symbol ? symbols : '');

    [...Array(length)].map((_) => {
      password += characters.charAt(Math.random() * characters.length);
    });
    return password;
  }
  return 'La longitud mínima debe ser entre 8 y 16';
}

console.log(generatePassword(16, true, true, true));
console.log(generatePassword(10, false, true, true));
console.log(generatePassword(14, false, false, true));
console.log(generatePassword(8, false, false, false));
console.log(generatePassword(20, true, true, true));