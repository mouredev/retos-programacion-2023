
const alphabetLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];

const leetLetters = ['4', 'I3', '[', ')', '3', '|=', '&', '#', '1', ',_|', '>|', '|_', '|V|', '^/', '0', '|*', '(_,)', 'I2', '5', '7', '(_)', '|/', 'VV', '><', '`/', 2];

const textTransformToLeet = ( text ) => {

  return text.toUpperCase().split('').map( letter => {

    if( alphabetLetters.includes(letter) ) { 

      const index = alphabetLetters.indexOf(letter); 
      return leetLetters[index];

    } 

    return letter;

  }).join('');

}