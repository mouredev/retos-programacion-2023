
const alphabet = [
  'A',
  'B',
  'C',
  'D',
  'E',
  'F',
  'G',
  'H',
  'I',
  'J',
  'K',
  'L',
  'M',
  'N',
  'O',
  'P',
  'Q',
  'R',
  'S',
  'T',
  'U',
  'V',
  'W',
  'X',
  'Y',
  'Z',
];

const leetLetters = [
  '4',
  'I3',
  '[',
  ')',
  '3',
  '|=',
  '&',
  '#',
  '1',
  ',_|',
  '>|',
  '1',
  '/\\/\\',
  '^/',
  '0',
  '|*',
  '(_,)',
  'I2',
  '5',
  '7',
  '(_)',
  '\\/',
  '\\/\\/',
  '><',
  'j',
  '2',
];

const translateToleet = (word: string) => {
  const translatableW = word.split('');
const translate = translatableW.map(a => {
  const character = a.toUpperCase();
  const letterPosition = alphabet.indexOf(character);
  const leetCharacter = leetLetters[letterPosition];
  a = leetCharacter
  return a
})

const finalWord = translate.join('');
return finalWord
};

translateToleet('hola');
