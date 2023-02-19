/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */

const letterSet = [
    'a',
    'b',
    'c',
    'd',
    'e',
    'f',
    'g',
    'h',
    'i',
    'j',
    'k',
    'l',
    'm',
    'n',
    'o',
    'p',
    'q',
    'r',
    's',
    't',
    'u',
    'v',
    'w',
    'x',
    'y',
    'z',
  ]
  
  const capitalLettersSet = [
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
  ]
  
  const symbolsSet = [
    '!',
    '"',
    '#',
    '$',
    '%',
    '&',
    "'",
    '(',
    ')',
    '*',
    '+',
    ',',
    '-',
    '.',
    '/',
    ':',
    ';',
    '<',
    '=',
    '>',
    '?',
    '@',
    '[',
    '\\',
    ']',
    '^',
    '_',
    '`',
    '{',
    '|',
    '}',
    '~',
  ]
  
  const numbersSet = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  
  // refactoriza este codigo
  
  function setNumbersCharacteres(expressionInputNumbersCharacters) {
    let numberCharacters
    while (true) {
      numberCharacters = prompt(expressionInputNumbersCharacters)
      if (numberCharacters === null) {
        return null
      }
  
      if (parseInt(numberCharacters)) {
        numberCharacters = parseInt(numberCharacters)
        if (numberCharacters > 7 && numberCharacters < 17) {
          console.log(numberCharacters)
          console.log('>>> OK! \n')
          return numberCharacters
        } else {
          console.log('>>> ERROR! Only accept numbers from 8 to 16.\n')
        }
      } else {
        console.log('>>> ERROR! Only accept numbers from 8 to 16.\n')
      }
    }
  }
  
  function checkYesOrNot(expresionInput) {
    let valueInput
    while (true) {
      valueInput = prompt(expresionInput)
  
      if (valueInput === null) {
        return null
      }
  
      if (valueInput !== 'yes' && valueInput !== 'no') {
        console.log('>>> ERROR! Only accept "yes" or "no".\n')
      } else {
        console.log(valueInput)
        console.log('>>> OK! \n')
        if (valueInput === 'yes') {
          return true
        } else {
          return false
        }
      }
    }
  }
  
  function setPassword() {
    let characterSet = [].concat(letterSet)
    let textCanceled = '>>> Canceled by user!\n'
    console.log('>>> Choose the options:')
    console.log('>>> To exit press CANCEL\n')
  
    console.log('>>> 1 - Number of characters? (min 8 // max 16)\n')
    let numbersCharacters = setNumbersCharacteres(
      '>>> 1 - Number of characters? (min 8 // max 16)\n'
    )
  
    if (numbersCharacters === null) {
      console.log(textCanceled)
      return
    }
  
    console.log('>>> 2 - Include CAPITAL LETTERS? (yes/no)\n')
    let capitalLetters = checkYesOrNot(
      '>>> 2 - Include CAPITAL LETTERS? (yes/no)\n'
    )
  
    if (capitalLetters === null) {
      console.log(textCanceled)
      return
    }
  
    console.log('>>> 3 - Include NUMBERS? (yes/no)\n')
    let numbers = checkYesOrNot('>>> 3 - Include NUMBERS? (yes/no)\n')
    if (numbers === null) {
      console.log(textCanceled)
      return
    }
  
    console.log('>>> 4 - Include SYMBOLS? (yes/no)\n')
    let symbols = checkYesOrNot('>>> 4 - Include SYMBOLS? (yes/no)\n')
    if (symbols === null) {
      console.log(textCanceled)
      return
    }
  
    if (capitalLetters) {
      characterSet = characterSet.concat(capitalLettersSet)
    }
    if (numbers) {
      characterSet = characterSet.concat(numbersSet)
    }
    if (symbols) {
      characterSet = characterSet.concat(symbolsSet)
    }
  
    let password = Array.from(
      { length: numbersCharacters },
      () => characterSet[Math.floor(Math.random() * characterSet.length)]
    ).join('')
  
    return password
  }
  
  let password = setPassword()
  console.log(password)
  