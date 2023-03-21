function generatorPassWord(
  long,
  hasUpperCase,
  hasNumber,
  hasSymbols,
  min = 8,
  max = 16
) {
  let upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  let lowerCase = "abcdefghijklmnopqrstuvwxyz";
  let number = "0123456789";
  let symbols = "@#$!~%/?";
  let accString = lowerCase;
  let passWord = "";

  if (long < min || long > max) {
    return `tu longitud es erronea, debe de estar entre ${min} y ${max}`;
  }
  if (hasUpperCase) {
    accString += upperCase;
  }
  if (hasNumber) {
    accString += number;
  }
  if (hasSymbols) {
    accString += symbols;
  }

  for (let i = 0; i < long; i++) {
    ramdon = Math.floor(Math.random() * accString.length);
    passWord += accString.charAt(ramdon);
  }
  return passWord;
}
generatorPassWord(16, true, true, true);
generatorPassWord(8, true, true);
generatorPassWord(14, false, false, true);
generatorPassWord(2, true, true, true);
generatorPassWord(20, true, true, true, 20, 30);
generatorPassWord(2, true, true, true, 20, 30);
