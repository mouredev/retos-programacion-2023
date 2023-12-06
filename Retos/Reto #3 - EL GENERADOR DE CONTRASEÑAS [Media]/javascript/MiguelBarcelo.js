const randomPassword = ({ length, hasUpperCase, hasDigits, hasSymbols }) => {
  const NUM_LETTERS_ALPHABET = 26;
  const A = 65;
  const a = 97;
  const EXCLAMATION_SYMBOL = 33;

  const alphabetLowerCase = Array.from({ length: NUM_LETTERS_ALPHABET }, 
    (_, i) => String.fromCharCode(i + a))
  
  const options = [];
  options.push(...alphabetLowerCase);
  
  if (hasUpperCase) {
    const alphabetUpperCase = Array.from({ length: NUM_LETTERS_ALPHABET }, 
      (_, i) => String.fromCharCode(i + A))
    options.push(...alphabetUpperCase)
  }
  
  if (hasDigits) {
    const digits = Array.from({ length: 10 }, (_, i) => ''+i);
    options.push(...digits);
  }
  
  if (hasSymbols) {
    const symbols = Array.from({ length: 15 }, 
      (_, i) => String.fromCharCode(i + EXCLAMATION_SYMBOL));
    options.push(...symbols);
  }

  const getChar = (options) => options[Math.floor(Math.random() * options.length)]

  return Array.from({ length }, () => getChar(options)).join('');
}